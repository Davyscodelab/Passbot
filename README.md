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

### Rollen
- `Actief lid`
- `België`
- `Nederland`
- `PB me niet`
- `Vraag voor PB`
- `PB altijd welkom`

> De bot moet hogere rechten hebben dan de rollen die hij uitdeelt. Geef de bot de permissies **Manage Roles** en **Send Messages**.

---

## Zelf hosten (fork & deploy)

### Stap 1 — Fork de repository

Klik rechtsboven op **Fork** om een kopie te maken onder je eigen GitHub-account.

### Stap 2 — Maak een Discord-bot aan

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

### Stap 3 — Noteer je server-ID

Rechtermuisklik op je server in Discord → **Copy Server ID**. (Zet ontwikkelaarsmodus aan via Instellingen → Geavanceerd als de optie ontbreekt.) Je hebt dit nodig in stap 4.

### Stap 4 — Lokaal draaien

```bash
# 1. Kloon je fork
git clone https://github.com/JOUW_GEBRUIKERSNAAM/Passbot.git
cd Passbot

# 2. Installeer de dependencies
pip install -r requirements.txt

# 3. Maak een .env bestand aan
echo TOKEN=jouw_discord_token_hier > .env
echo GUILD_ID=jouw_server_id_hier >> .env

# 4. Start de bot
python Passbot.py
```

---

## Hosten via Railway

> **Let op:** Railway is niet langer gratis voor 24/7 draaien. Je betaalt op basis van gebruik (pay-as-you-go). Bekijk de actuele prijzen op [railway.app/pricing](https://railway.app/pricing). Voor een lichte Discord-bot liggen de kosten doorgaans laag, maar hou er rekening mee.

### GitHub koppelen aan Railway

1. Maak een account aan op [railway.app](https://railway.app) (log in met GitHub)
2. Klik op **New Project** → **Deploy from GitHub repo**
3. Selecteer je geforkte repository (`Passbot`)
4. Railway detecteert automatisch het Python-project

### Omgevingsvariabelen instellen

1. Ga in Railway naar je project → **Variables**
2. Voeg toe:
   - **Name:** `TOKEN` — **Value:** jouw Discord bot token
   - **Name:** `GUILD_ID` — **Value:** jouw server-ID
3. Klik op **Save**

> Commit je `.env` bestand **nooit** naar GitHub. Het staat al in `.gitignore`.

### Starten

Railway start de bot automatisch na elke push naar de `main` branch van je GitHub-repository. Klaar.

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
