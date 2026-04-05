
import discord
from discord import app_commands
from discord.ext import commands
import os
import random
import csv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
token: str | None = os.getenv('TOKEN')
if token is None:
    raise ValueError("FOUT: Kon het token niet vinden. Controleer of je .env bestand 'TOKEN=jouw_token' bevat.")

guild_id_str = os.getenv('GUILD_ID')
if guild_id_str is None:
    raise ValueError("FOUT: Kon de guild ID niet vinden. Controleer of je .env bestand 'GUILD_ID=jouw_guild_id' bevat.")
guild_id = int(guild_id_str)

# Intents (nodig voor member join en berichten)
intents = discord.Intents.default()
intents.members = True          # Voor on_member_join
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# ── Welkom bericht wanneer iemand de server joint ──
@bot.event
async def on_member_join(member):
    # Zoek het kanaal "stel-je-voor"
    welcome_channel = discord.utils.get(member.guild.text_channels, name="stel-je-voor")
   
    if welcome_channel:
        await welcome_channel.send(
            f"Welkom! Stel je voor in #{welcome_channel.name} {member.mention}. Vertel ons zeker of je (een vermoeden van) ASS hebt!"
        )
    else:
        print(f"Kanaal 'stel-je-voor' niet gevonden op server: {member.guild.name}")

# ── Slash Command: /welcome @gebruiker ──
@bot.tree.command(
    name="welcome",
    description="Verwelkom een gebruiker en geef de rol 'Actief lid'"
)
@app_commands.describe(member="De gebruiker die je wilt verwelkomen")
@app_commands.checks.has_role("Moderator")  # Alleen moderators
async def welcome(interaction: discord.Interaction, member: discord.Member):
    # Zoek de rol "Actief lid"
    role = discord.utils.get(interaction.guild.roles, name="Actief lid")
   
    if not role:
        await interaction.response.send_message(
            "❌ Rol **Actief lid** niet gevonden! Maak een rol aan met exact de naam **Actief lid**.",
            ephemeral=True
        )
        return
   
    try:
        await member.add_roles(role)

        regels_kanaal = discord.utils.get(interaction.guild.channels, name="server-regels")
        rollen_kanaal = discord.utils.get(interaction.guild.channels, name="rol-aanvragen")
        toog_kanaal = discord.utils.get(interaction.guild.channels, name="de-toog")
        regels_mention = regels_kanaal.mention if regels_kanaal else "#server-regels"
        rollen_mention = rollen_kanaal.mention if rollen_kanaal else "#rol-aanvragen"
        toog_mention = toog_kanaal.mention if toog_kanaal else "#de-toog"

        await interaction.response.send_message(
            f"Hey, {member.mention}, welkom! Je hebt nu toegang tot alle kanalen. Lees zeker nog {regels_mention} indien je dat nog niet hebt gedaan. Je kan rollen aanvragen bij {rollen_mention} als je dat wil. Mocht je met vragen, opmerkingen,... zitten, laat deze gerust weten in bv. {toog_mention} of aan één van de mods persoonlijk, mocht je dat gemakkelijker vinden. Ik wens je alvast veel chatplezier hier!",
            ephemeral=False
        )
    except discord.Forbidden:
        await interaction.response.send_message(
            "❌ Ik heb geen toestemming om rollen toe te voegen. Geef de bot hogere rechten (Manage Roles).",
            ephemeral=True
        )
    except Exception as e:
        await interaction.response.send_message(f"Er ging iets mis: {e}", ephemeral=True)

# ── Slash Command: /land ──
@bot.tree.command(
    name="land",
    description="Kies je land: België of Nederland"
)
@app_commands.describe(keuze="Kies je land")
@app_commands.choices(keuze=[
    app_commands.Choice(name="België", value="België"),
    app_commands.Choice(name="Nederland", value="Nederland"),
])
async def land(interaction: discord.Interaction, keuze: app_commands.Choice[str]):
    landen = ["België", "Nederland"]
    rol_toevoegen = discord.utils.get(interaction.guild.roles, name=keuze.value)
    if not rol_toevoegen:
        await interaction.response.send_message(f"❌ Rol **{keuze.value}** niet gevonden op de server.", ephemeral=True)
        return

    member = interaction.user
    rollen_verwijderen = [r for r in member.roles if r.name in landen and r.name != keuze.value]
    if rollen_verwijderen:
        await member.remove_roles(*rollen_verwijderen)
    await member.add_roles(rol_toevoegen)
    await interaction.response.send_message(f"✅ Je landrol is ingesteld op **{keuze.value}**.", ephemeral=True)


# ── Slash Command: /contact ──
@bot.tree.command(
    name="contact",
    description="Geef aan hoe anderen je mogen contacteren"
)
@app_commands.describe(keuze="Kies je contactvoorkeur")
@app_commands.choices(keuze=[
    app_commands.Choice(name="PB me niet", value="PB me niet"),
    app_commands.Choice(name="Vraag voor PB", value="Vraag voor PB"),
    app_commands.Choice(name="PB altijd welkom", value="PB altijd welkom"),
])
async def contact(interaction: discord.Interaction, keuze: app_commands.Choice[str]):
    contactrollen = ["PB me niet", "Vraag voor PB", "PB altijd welkom"]
    rol_toevoegen = discord.utils.get(interaction.guild.roles, name=keuze.value)
    if not rol_toevoegen:
        await interaction.response.send_message(f"❌ Rol **{keuze.value}** niet gevonden op de server.", ephemeral=True)
        return

    member = interaction.user
    rollen_verwijderen = [r for r in member.roles if r.name in contactrollen and r.name != keuze.value]
    if rollen_verwijderen:
        await member.remove_roles(*rollen_verwijderen)
    await member.add_roles(rol_toevoegen)
    await interaction.response.send_message(f"✅ Je contactvoorkeur is ingesteld op **{keuze.value}**.", ephemeral=True)


# ── Slash Command: /disclaimer ──
@bot.tree.command(
    name="disclaimer",
    description="Toon de disclaimer over de AI-bot"
)
@app_commands.checks.has_role("Moderator")  # Alleen moderators
async def disclaimer(interaction: discord.Interaction):
    embed = discord.Embed(
        description="**Disclaimer:** Deze Discord-bot is gebouwd met behulp van AI, en kan fouten bevatten en maken. Als je iets merkt, kan je dan één van de moderators contacteren?",
        color=discord.Color.red()
    )
    await interaction.response.send_message(embed=embed)


# ── Slash Command: /modgids ──
@bot.tree.command(
    name="modgids",
    description="Toont alle beschikbare commands met beschrijvingen"
)
@app_commands.checks.has_role("Moderator")  # Alleen moderators
async def modgids(interaction: discord.Interaction):
    # Check if command is called in "moderators" channel
    if interaction.channel.name != "moderators":
        await interaction.response.send_message(
            "❌ Dit command kan alleen in het #moderators kanaal gebruikt worden.",
            ephemeral=True
        )
        return

    # Read commands from CSV
    try:
        commands_list = []
        with open('commands.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                commands_list.append(row)

        # Build embed message
        embed = discord.Embed(
            title="📋 Alle beschikbare Commands",
            color=discord.Color.blue()
        )

        for cmd in commands_list:
            command_name = cmd['command_name']
            description = cmd['description']
            mod_only = cmd['mod_only']

            # Add badge for mod-only commands
            badge = "🔐 MOD-ONLY" if mod_only.lower() == "ja" else "✅ Openbaar"

            embed.add_field(
                name=f"/{command_name}",
                value=f"{description}\n*{badge}*",
                inline=False
            )

        await interaction.response.send_message(embed=embed)

    except FileNotFoundError:
        await interaction.response.send_message(
            "❌ Het commands.csv bestand kon niet gevonden worden.",
            ephemeral=True
        )


# ── Slash Command: /regels ──
@bot.tree.command(
    name="regels",
    description="Herinnering aan serverregels"
)
@app_commands.checks.has_role("Moderator")  # Alleen moderators
async def regels(interaction: discord.Interaction):
    await interaction.response.send_message("Denken jullie nog even aan de serverregels?")


# ── Slash Command: /kanaal ──
@bot.tree.command(
    name="kanaal",
    description="Herinnering om het juiste kanaal te gebruiken"
)
@app_commands.checks.has_role("Moderator")  # Alleen moderators
async def kanaal(interaction: discord.Interaction):
    await interaction.response.send_message("Willen jullie wel even het juiste kanaal gebruiken?")


# ── Uitleg sturen als iemand iets typt in rol-aanvragen ──
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.name == "rol-aanvragen":
        await message.channel.send(
            f"{message.author.mention} Je kan hier enkele rollen zelf aanvragen via slash commands:\n"
            f"• **/land** — kies **België** of **Nederland**\n"
            f"• **/contact** — kies hoe anderen je mogen contacteren:\n"
            f"  - **PB me niet**: je wil geen persoonlijke berichten ontvangen\n"
            f"  - **Vraag voor PB**: men moet eerst in een kanaal vragen of ze je een PB mogen sturen\n"
            f"  - **PB altijd welkom**: iedereen mag je direct een bericht sturen\n\n"
            f"Kleurrollen en andere rollen worden door de mods toegekend."
        )
    await bot.process_commands(message)


# ── Slash Command: /wie ──
@bot.tree.command(
    name="wie",
    description="Wie heeft deze bot gemaakt?"
)
async def wie(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Deze Discord bot werd ontwikkeld door https://github.com/Davyscodelab, speciaal voor \"De PASSage\", een discordgroep voor en door mensen met ASS."
    )


# ── Bot klaar + sync slash commands ──
@bot.event
async def on_ready():
    print(f'✅ Bot is online als {bot.user}')
   
    # Sync slash commands voor jouw server (vervang JE_SERVER_ID)
    try:
        guild = discord.Object(id=guild_id)
        bot.tree.copy_global_to(guild=guild)
        synced = await bot.tree.sync(guild=guild)
        print(f"✅ {len(synced)} slash command(s) succesvol gesynced voor deze server.")
    except Exception as e:
        print(f"Sync fout: {e}")

# Start de bot
bot.run(token)
