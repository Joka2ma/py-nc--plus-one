# src/seed.py

from src.utils import normalise_email,hash_password,validate_event_times
from psycopg2.extensions import connection
from typing import TypedDict

class UserRow(TypedDict):
    email: str
    password: str  # plain text in the JSON; hashed on insert
    name: str


class VenueRow(TypedDict):
    name: str
    address: str
    capacity: int


class EventRow(TypedDict):
    title: str
    description: str
    starts_at: str  # ISO 8601 timestamp
    ends_at: str    # ISO 8601 timestamp
    organiser_id: int
    venue_id: int


class RsvpRow(TypedDict):
    attendee_id: int
    event_id: int

class SeedData(TypedDict):
    users: list[UserRow]
    venues: list[VenueRow]
    events: list[EventRow]
    rsvps: list[RsvpRow]


def run_sql_file(conn:connection, filepath:str) -> None:
    with open(filepath, 'r') as file:
        sql_script = file.read()
    with conn.cursor() as cursor:
        cursor.execute(sql_script)
    conn.commit()
    print(f"Executed script: {filepath}")

def drop_tables(conn:connection) -> None:
    run_sql_file(conn,"db/drop_tables.sql")
    
def create_tables(conn:connection) -> None:
    run_sql_file(conn,"db/create_tables.sql")

def seed_users_table(conn:connection, users_data:list[UserRow]):
    with conn.cursor() as cursor:
        for u in users_data:
            cursor.execute(
                "INSERT INTO Users(email, password, name) VALUES (%s, %s, %s);",
                (normalise_email(u["email"]), hash_password(u["password"]), u["name"]),
            )
    conn.commit()


def seed_venues_table(conn:connection, venues_data:list[VenueRow]):
    with conn.cursor() as cursor:
        for v in venues_data:
            cursor.execute(
                "INSERT INTO Venues(name, address, capacity) VALUES (%s, %s, %s);",
                (v["name"], v["address"], v["capacity"]),
            )
    conn.commit()


def seed_events_table(conn:connection, events_data:list[EventRow]):
    with conn.cursor() as cursor:
        for e in events_data:
            validate_event_times(e["starts_at"],e["ends_at"])
            cursor.execute(
                "INSERT INTO Events(title, description, starts_at, ends_at, organiser_id, venue_id) "
                "VALUES (%s, %s, %s, %s, %s, %s);",
                (e["title"], e["description"], e["starts_at"], e["ends_at"],
                 e["organiser_id"], e["venue_id"]),
            )
    conn.commit()


def seed_rsvp_table(conn:connection, rsvp_data:list[RsvpRow]):
    with conn.cursor() as cursor:
        for a in rsvp_data:
            cursor.execute(
                "INSERT INTO Rsvps(attendee_id, event_id) VALUES (%s, %s);",
                (a["attendee_id"], a["event_id"]),
            )
    conn.commit()
    
    
    
def seed(conn:connection,data:SeedData) -> None:
    drop_tables(conn)
    create_tables(conn)
    seed_users_table(conn,data["users"])
    seed_venues_table(conn,data["venues"])
    seed_events_table(conn,data["events"])
    seed_rsvp_table(conn,data["rsvps"])