# Normalise users email and address . strip white spaces and email to all lower case

import bcrypt
from datetime import datetime 


def normalise_email(email:str)-> str:
    """_summary_
    

    Args:
        email (str): _description_

    Returns:
        str: _description_,
        the email trimmed for whitespaces and  coverted to all lowercase
    """
    return email.strip().lower()

def hash_password(password:str) -> str:
    """_summary_

    Args:
        password (str): _description_

    Returns:
        str: _description_
    """
    return bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()


def validate_event_times (starts_at:str,ends_at:str) -> None:
    """Checks that an event does not end before it starts on the
    the same day. 
    
    This  will validate the event before it entered into the database
    """
    
    start = datetime.fromisoformat(starts_at)
    end = datetime.fromisoformat(ends_at)
    
    if start.date() == end.date() and end < start:
        raise ValueError(
            f"ends at ({ends_at}) must not before start_at ({starts_at})"
        )