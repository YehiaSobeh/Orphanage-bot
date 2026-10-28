# Orphanage Bot

A bilingual (Russian and English) Telegram bot that connects orphanage alumni and children in Tatarstan with volunteers: tutors, psychologists, lawyers, or help with anything else. A person registers, describes the problem, and an admin team matches them with a volunteer. The volunteer rules and manual were written with Innopolis University professors.

Built in 2024 by a volunteer student team at Innopolis University. I worked on the backend: the conversation flow, the database, and the request routing.

## Why it matters

Orphanage graduates often lose access to adults they can ask for help the day they leave. The bot gives them one place to ask, in their own language, and gives volunteers a queue instead of scattered messages.

![Bot flow](docs/demo.png)
*[ADD SCREENSHOT: docs/demo.png, registration and request flow in the Telegram client]*

## What it does

- **Registration:** name, age, region, orphanage, alumni status. A person can re-register; the record is updated, not duplicated.
- **Requesting help:** pick a category (tutor, psychologist, lawyer, other), describe the problem, confirm. The request is forwarded to the admin.
- **Error reporting:** any user can send a problem report that reaches the admin.
- **Language switch:** English or Russian at any point.
- Every step can be cancelled and restarted.

## Architecture

```
Telegram user ──▶ bot.py (python-telegram-bot, async ConversationHandler)
                      │
                      ├── backend/app.py (Flask + SQLAlchemy): events table, admin endpoints
                      └── SQLite (backend/instance/events.db)
```

## Tech stack

Python 3.9, python-telegram-bot (asyncio), Flask, Flask-SQLAlchemy, SQLite, Docker.

## How to run

```bash
git clone https://github.com/YehiaSobeh/Orphanage-bot.git
cd Orphanage-bot/backend
pip install -r requirements.txt
export TELEGRAM_BOT_TOKEN=...      # read by backend/app.py and bot.py
flask run --host 0.0.0.0           # backend
python3 ../bot.py                  # bot
```

Or with Docker:

```bash
cd backend && docker build -t orphanage-bot . && docker run --env TELEGRAM_BOT_TOKEN=... orphanage-bot
```

## What I learned

- Conversation state machines get complicated fast. Modelling the flow as explicit states (NAME, AGE, REGION, ORPHANAGE, ALUMNI, PROBLEM) with a cancel path from every state kept it debuggable.
- Idempotent registration (update, never duplicate) matters more than it looks when users retry.
- Building for real users with non-technical stakeholders means the manual and the rules are part of the product.
