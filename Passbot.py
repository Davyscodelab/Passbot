
import discord
from discord import app_commands
from discord.ext import commands
import os
import random
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
token: str | None = os.getenv('TOKEN')

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
@app_commands.checks.has_permissions(manage_roles=True)  # Alleen moderators
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
        await interaction.response.send_message(
            f"Welkom, {member.mention}, je hebt nu toegang!",
            ephemeral=False
        )
    except discord.Forbidden:
        await interaction.response.send_message(
            "❌ Ik heb geen toestemming om rollen toe te voegen. Geef de bot hogere rechten (Manage Roles).",
            ephemeral=True
        )
    except Exception as e:
        await interaction.response.send_message(f"Er ging iets mis: {e}", ephemeral=True)

# ── Bot klaar + sync slash commands ──
@bot.event
async def on_ready():
    print(f'✅ Bot is online als {bot.user}')
   
    # Sync slash commands voor jouw server (vervang JE_SERVER_ID)
    try:
        guild = discord.Object(id=GUILD_ID_REMOVED)
        synced = await bot.tree.sync(guild=guild)
        print(f"✅ {len(synced)} slash command(s) succesvol gesynced voor deze server.")
    except Exception as e:
        print(f"Sync fout: {e}")

# Start de bot
bot.run(token)
