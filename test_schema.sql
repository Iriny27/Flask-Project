CREATE TABLE IF NOT EXISTS registrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    birth_date TEXT NOT NULL,
    gender TEXT NOT NULL,
    address_line1 TEXT NOT NULL,
    address_line2 TEXT NOT NULL,
    country TEXT NOT NULL,
    city TEXT NOT NULL,
    region TEXT NOT NULL,
    postal_code TEXT NOT NULL
);
