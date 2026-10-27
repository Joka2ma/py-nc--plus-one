# config/connection.py
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv(".env.development")


def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv("PGDATABASE", "nc_plus_one"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD"),
        host=os.getenv("PGHOST", "localhost"),
        port=os.getenv("PGPORT", "5432"),
    )

