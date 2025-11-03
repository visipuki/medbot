
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
Author: [Your Name or Telegram Handle]  
Questions or feedback — please open an Issue on GitHub or contact via Telegram.
