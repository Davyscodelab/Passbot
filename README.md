# Passbot

![Banner](Banner.png)

Een Discord-bot op maat voor de vereniging — gebouwd met [discord.py](https://discordpy.readthedocs.io/). Passbot verwelkomt nieuwe leden, kent rollen toe en geeft leden de mogelijkheid om zelf hun land en contactvoorkeur in te stellen via slash commands.

---

## Functies

| Functie | Beschrijving |
|---|---|
| **Automatisch welkomstbericht** | Wanneer iemand de server joint, stuurt de bot een berichtje in `#stel-je-voor` |
| `/welcome @gebruiker` | (Mods) Geeft de rol **Actief lid** en stuurt een uitgebreid welkomstbericht |
| `/land` | Leden kiezen zelf hun landrol: **België** of **Nederland** |
| `/contact` | Leden stellen zelf in hoe ze gecontacteerd mogen worden |
| `/disclaimer` | (Mods) Stuurt een embed met de AI-disclaimer |
| `/modgids` | (Mods) Toont alle beschikbare commands met beschrijvingen — alleen in `#moderators` |
| `/regels` | (Mods) Stuurt een herinnering aan de serverregels |
| `/kanaal` | (Mods) Stuurt een herinnering om het juiste kanaal te gebruiken |
| `/wie` | Toont wie de bot ontwikkeld heeft en voor welke groep |
| **Uitleg in `#rol-aanvragen`** | Wanneer iemand een bericht typt in dat kanaal, legt de bot automatisch uit welke slash commands beschikbaar zijn |

---

## Vereisten op de Discord-server

Zorg ervoor dat de volgende **kanalen** en **rollen** aangemaakt zijn op je server (exact dezelfde naam):

### Kanalen
- `stel-je-voor`
- `server-regels`
- `rol-aanvragen`
- `de-toog`
- `moderators`

### Rollen
- `Actief lid`
- `België`
- `Nederland`
- `PB me niet`
- `Vraag voor PB`
- `PB altijd welkom`

> De bot moet hogere rechten hebben dan de rollen die hij uitdeelt. Geef de bot de permissies **Manage Roles** en **Send Messages**.

---

## Zelf hosten

### Stap 1 — Maak een Discord-bot aan

1. Ga naar de [Discord Developer Portal](https://discord.com/developers/applications)
2. Klik op **New Application** en geef het een naam
3. Ga naar **Bot** → klik op **Reset Token** → kopieer het token
4. Zet onder **Privileged Gateway Intents** de volgende aan:
   - `SERVER MEMBERS INTENT`
   - `MESSAGE CONTENT INTENT`
5. Ga naar **OAuth2 → URL Generator**:
   - Scopes: `bot`, `applications.commands`
   - Bot permissions: `Send Messages`, `Manage Roles`, `Read Message History`
6. Kopieer de gegenereerde URL en open die in je browser om de bot toe te voegen aan je server

### Stap 2 — Noteer je server-ID

Rechtermuisklik op je server in Discord → **Copy Server ID**. (Zet ontwikkelaarsmodus aan via Instellingen → Geavanceerd als de optie ontbreekt.) Je hebt dit nodig in stap 3.

### Stap 3 — Bot draaien

```bash
# 1. Kloon de repository
git clone https://github.com/Davyscodelab/Passbot.git
cd Passbot

# 2. Installeer de dependencies
pip install -r requirements.txt

# 3. Maak een .env bestand aan
echo TOKEN=jouw_discord_token_hier > .env
echo GUILD_ID=jouw_server_id_hier >> .env

# 4. Start de bot
python Passbot.py
```

> Commit je `.env` bestand **nooit** naar GitHub. Het staat al in `.gitignore`.

---

## Lokale .env structuur

```
TOKEN=jouw_discord_token_hier
GUILD_ID=jouw_server_id_hier
```

---

## Dependencies

| Package | Versie |
|---|---|
| discord.py | 2.7.1 |
| python-dotenv | 1.2.2 |

Installeren: `pip install -r requirements.txt`

---

## Licentie

[MIT](LICENSE) — vrij te gebruiken, aanpassen en verder delen.

---

Ontwikkeld door [Davyscodelab](https://github.com/Davyscodelab). Met dank aan de community voor de input en de testen.
