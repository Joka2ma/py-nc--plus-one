# main.py
import json
from config.connection import get_db_connection
from src.seed import (
    run_sql_file,
    seed_users_table,
    seed_venues_table,
    seed_events_table,
    seed_rsvp_table,
)


def load_data(filepath):
    with open(filepath) as file:
        return json.load(file)


if __name__ == "__main__":
    conn = get_db_connection()
    try:
        print("Rebuilding database structures...")
        run_sql_file(conn, "db/setup.sql")

        print("Seeding tables...")
        seed_users_table(conn, load_data("db/data/users.json"))
        seed_venues_table(conn, load_data("db/data/venues.json"))
        seed_events_table(conn, load_data("db/data/events.json"))
        seed_rsvp_table(conn, load_data("db/data/rsvps.json"))

        print("Database successfully seeded!")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()