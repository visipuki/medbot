CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_id INTEGER NOT NULL UNIQUE,
    name TEXT,
    role TEXT
);

CREATE TABLE medicines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT,
    dose TEXT,
    description TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);

CREATE TABLE schedules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    medicine_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    weekday INTEGER NOT NULL,  -- 0=Monday
    time TEXT NOT NULL,        -- HH:MM
    enabled BOOLEAN NOT NULL DEFAULT 1,
    FOREIGN KEY(medicine_id) REFERENCES medicines(id),
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);

CREATE TABLE reminders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    schedule_id INTEGER NOT NULL,
    status TEXT NOT NULL,
    planned_at TEXT NOT NULL,
    actual_at TEXT,
    postponed_minutes INTEGER DEFAULT 0,
    default_postpone INTEGER DEFAULT 0,
    FOREIGN KEY(schedule_id) REFERENCES schedules(id)
);

CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    event TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);

