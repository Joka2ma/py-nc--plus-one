"""Shared fixtures: a seeded test database and an API client."""

import json
import os
from collections.abc import Iterator
from typing import Any, cast

# Must be set before config.connection is imported.
os.environ["PGDATABASE"] = "nc_plus_one_test"

import pytest
from fastapi.testclient import TestClient

from app import app
from config.connection import get_db_connection
from src.seed import SeedData, seed


def _load(name: str) -> Any:
    with open(f"db/data/{name}.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def seed_data() -> dict[str, Any]:
    return {n: _load(n) for n in ("users", "venues", "events", "rsvps")}


@pytest.fixture(scope="session", autouse=True)
def seeded_db(seed_data: dict[str, Any]) -> Iterator[None]:
    conn = get_db_connection()
    try:
        seed(conn, cast(SeedData, seed_data))
        yield
    finally:
        conn.close()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)