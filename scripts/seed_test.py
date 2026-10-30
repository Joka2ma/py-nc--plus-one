"""Seed the test database from the sample files in tests/data/.

Usage (from the project root):
    python -m scripts.seed_test

Creates no database: run `createdb nc_plus_one_test` first. Drops and
recreates all tables in nc_plus_one_test. The dev database is never touched.
"""

import json
import os
from pathlib import Path
from typing import cast

# Must be set before config.connection is imported.
os.environ["PGDATABASE"] = "nc_plus_one_test"

from config.connection import get_db_connection
from src.seed import SeedData, seed

DATA_DIR = Path("tests/data")


def main() -> None:
    """Rebuild the test database tables and load the sample data."""
    data = {
        name: json.loads((DATA_DIR / f"{name}.json").read_text())
        for name in ("users", "venues", "events", "rsvps")
    }
    conn = get_db_connection()
    try:
        seed(conn, cast(SeedData, data))
        print("Test database seeded from tests/data/")
    finally:
        conn.close()


if __name__ == "__main__":
    main()