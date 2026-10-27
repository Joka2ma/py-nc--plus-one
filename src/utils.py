# Normalise users email and address . strip white spaces and email to all lower case

import bcrypt


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