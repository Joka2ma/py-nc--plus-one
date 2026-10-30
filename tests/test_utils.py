import pytest

from src.utils import normalise_email,hash_password,validate_event_times

def test_lowercase_email():
    assert normalise_email("DavId@example.com") == "david@example.com"
    
    
def test_remove_whitespaces():
    assert normalise_email(" david@example.com ") == "david@example.com"
    
def test_password_is_hashed():
   new_password = hash_password("password123")
   
   assert new_password != "passsword123"
    
    



def test_raises_if_end_before_start_on_same_day() -> None:
    with pytest.raises(ValueError):
        validate_event_times("2026-07-04T20:00:00+01:00", "2026-07-04T17:00:00+01:00")


def test_accepts_end_after_start_on_same_day() -> None:
    validate_event_times("2026-07-04T17:00:00+01:00", "2026-07-04T20:00:00+01:00")


def test_accepts_end_equal_to_start() -> None:
    validate_event_times("2026-07-04T17:00:00+01:00", "2026-07-04T17:00:00+01:00")


def test_accepts_end_on_a_later_day() -> None:
    validate_event_times("2026-07-04T22:00:00+01:00", "2026-07-05T02:00:00+01:00")


def test_raises_on_invalid_date_string() -> None:
    with pytest.raises(ValueError):
        validate_event_times("not a date", "2026-07-04T17:00:00+01:00")