"""Event routes."""

from typing import Any, cast

from fastapi import APIRouter
from psycopg2.extras import RealDictCursor

from config.connection import get_db_connection
from models.event import EventsResponse

router = APIRouter(prefix="/events", tags=["events"])


@router.get("", response_model=EventsResponse)
def get_events() -> dict[str, list[dict[str, Any]]]:
    """Return all events with their venue location, soonest first."""
    conn = get_db_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT e.event_id AS id,
                       e.title,
                       e.starts_at,
                       e.ends_at,
                       NULLIF(concat_ws(', ', v.name, v.address), '') AS location
                FROM events e
                LEFT JOIN venues v ON v.venue_id = e.venue_id
                ORDER BY e.starts_at ASC, e.event_id ASC;
                """
            )
            rows = cast(list[dict[str, Any]], cursor.fetchall())
            return {"events": rows}
    finally:
        conn.close()
        
    

