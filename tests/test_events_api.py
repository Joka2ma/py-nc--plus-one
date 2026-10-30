"""Integration tests for GET /api/events."""

from typing import Any

from fastapi.testclient import TestClient


def test_returns_200(client: TestClient) -> None:
    assert client.get("/api/events").status_code == 200


def test_body_is_object_with_events_key(client: TestClient) -> None:
    body = client.get("/api/events").json()
    assert isinstance(body, dict)
    assert isinstance(body["events"], list)


def test_returns_all_seeded_events(
    client: TestClient, seed_data: dict[str, Any]
) -> None:
    events = client.get("/api/events").json()["events"]
    assert len(events) == len(seed_data["events"])


def test_event_shape(client: TestClient) -> None:
    event = client.get("/api/events").json()["events"][0]
    assert set(event) == {"id", "title", "starts_at", "ends_at", "location"}


def test_ordered_by_start_time_then_id(client: TestClient) -> None:
    events = client.get("/api/events").json()["events"]
    keys = [(e["starts_at"], e["id"]) for e in events]
    assert keys == sorted(keys)


def test_location_comes_from_venue(client: TestClient) -> None:
    events = client.get("/api/events").json()["events"]
    assert all(e["location"] for e in events)