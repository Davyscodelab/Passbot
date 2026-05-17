# Passbot

![Banner](Banner.png)

Een Discord-bot gebouwd als leerproject — demonstreert slash commands, automatisch rolbeheer en ledenverwerking via discord.py. Getest op een privé-testserver.

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
3. Ga naar **Bot** → klik op **Reset Token** → kopieer het token (je hebt dit nodig in stap 4)
4. Zet onder **Privileged Gateway Intents** de volgende aan:
   - `SERVER MEMBERS INTENT`
   - `MESSAGE CONTENT INTENT`

### Stap 2 — Voeg de bot toe aan je server

De bot moet uitgenodigd worden via een OAuth2-link. Die link vraagt je bij het openen welke server je bedoelt — de server-ID heb je hier dus nog niet nodig.

1. Ga in de Developer Portal naar **OAuth2 → URL Generator**
2. Selecteer bij Scopes: `bot`, `applications.commands`
3. Selecteer bij Bot permissions: `Send Messages`, `Manage Roles`, `Read Message History`
4. Kopieer de gegenereerde URL en open die in je browser
5. Kies de server waarop je de bot wil toevoegen en bevestig

### Stap 3 — Noteer je server-ID

De bot heeft de server-ID nodig om zijn slash commands te synchroniseren.

Rechtermuisklik op je server in Discord → **Copy Server ID**. (Zet ontwikkelaarsmodus aan via Instellingen → Geavanceerd als de optie ontbreekt.)

### Stap 4 — Bot draaien

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

## Notities
Ontwikkeld met in VSCode met behulp van Claude Code. Met dank aan de community voor de input en de testen.
