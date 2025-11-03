# MedBot — Telegram Medicine Reminder Bot

MedBot is a Telegram chatbot designed to help users (especially teens) remember to take their medications on schedule. The bot allows flexible configuration of medication lists and reminder times, tracks user actions, and provides logging for parental control or shared channels.

## Features

- Scheduled reminders for taking medication, customizable per day.
- Each notification can include a list of medicines, precise dosing, and comments (e.g. before/after food).
- Ability to postpone notifications for a set number of minutes or hours.
- Option to confirm medication was taken; otherwise, reminders can be repeated.
- Activity logs sent to a second Telegram channel for parent notifications.
- Customizable notification messages.
- Simple configuration via Telegram commands.
- Notifications and medicines are managed via a user-friendly Telegram interface.
- All sensitive data (bot tokens etc.) managed via environment variables, not stored in code or repo.
- Stores data in SQLite, with proper migrations and automated DB setup.
- Ready for Docker Compose deployment.

## Quickstart

1. **Clone the repository:**

```bash
git clone https://github.com/visipuki/medbot.git
cd medbot
```

2. **Prepare the .env file:**  
Copy `.env.example` to `.env` and set your Telegram bot token and config parameters.

3. **Run database migrations:**  
Migrations are applied automatically when you run the container, or manually with:

```bash
python database.py migrate
```

4. **Launch with Docker Compose:**

```bash
docker-compose up --build
```

5. **Use Telegram:**  
- Add the bot to your Telegram.
- Send `/start` to begin, then follow prompts to set up reminders.

## Project Structure

```text
medbot/
├── bot.py # Main bot entry point
├── database.py # Handles SQLite DB operations & runs migrations
├── handlers.py # Bot command & message handling
├── models.py # Data models and helpers
├── migrations/ # Database schema migrations (.sql files)
├── requirements.txt # Python dependencies
├── .env.example # Example environment configuration
└── README.md # Project documentation
```

## Telegram Commands

- `/start` — begins work with the bot
- `/add_notification` — create a new reminder (for a specific time and medicine list)
- `/list_notifications` — show all upcoming notifications
- `/taken` — confirm a medicine has been taken
- `/delay` — postpone the next notification
- `/help` — show help message with command list

## Configuration

All sensitive settings (such as the Telegram bot token) are provided through environment variables.  
Do not commit `.env` with secrets to the repository — keep it listed in `.gitignore`.

Example `.env`:

```text
TELEGRAM_BOT_TOKEN=your_secret_bot_token
TZ=Europe/Moscow
```

## Database & Migrations

- The SQLite database schema uses migrations stored in the `migrations/` folder.
- Migrations are applied automatically when launching the project via Docker.
- You can add or alter tables by adding a new `.sql` file to `migrations/` and running migration.

## Logging and Notifications

- Bot activity and child’s medication-taking events are logged in the database.
- You can configure the bot to send this log to a separate Telegram channel for parental review.

## Contributing & Extending

- See the TODO section in README or open issues for new features and bug fixes.
- Contributions are welcome — please fork and submit a pull request with clear documentation.

## License & Contact

MIT License.  
Author: [Visipuki]  
Questions or feedback — please open an Issue on GitHub or contact via Telegram.
