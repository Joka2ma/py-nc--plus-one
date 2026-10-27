# src/seed.py

def run_sql_file(conn, filepath):
    with open(filepath, 'r') as file:
        sql_script = file.read()
    with conn.cursor() as cursor:
        cursor.execute(sql_script)
    conn.commit()
    print(f"Executed script: {filepath}")


def seed_users_table(conn, users_data):
    with conn.cursor() as cursor:
        for u in users_data:
            cursor.execute(
                "INSERT INTO Users(email, password, name) VALUES (%s, %s, %s);",
                (u["email"], u["password"], u["name"]),
            )
    conn.commit()


def seed_venues_table(conn, venues_data):
    with conn.cursor() as cursor:
        for v in venues_data:
            cursor.execute(
                "INSERT INTO Venues(name, address, capacity) VALUES (%s, %s, %s);",
                (v["name"], v["address"], v["capacity"]),
            )
    conn.commit()


def seed_events_table(conn, events_data):
    with conn.cursor() as cursor:
        for e in events_data:
            cursor.execute(
                "INSERT INTO Events(title, description, starts_at, ends_at, organiser_id, venue_id) "
                "VALUES (%s, %s, %s, %s, %s, %s);",
                (e["title"], e["description"], e["starts_at"], e["ends_at"],
                 e["organiser_id"], e["venue_id"]),
            )
    conn.commit()


def seed_rsvp_table(conn, rsvp_data):
    with conn.cursor() as cursor:
        for a in rsvp_data:
            cursor.execute(
                "INSERT INTO Rsvps(attendee_id, event_id) VALUES (%s, %s);",
                (a["attendee_id"], a["event_id"]),
            )
    conn.commit()