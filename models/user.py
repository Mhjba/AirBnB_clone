#!/usr/bin/python3
"""defines the class User."""
from models.base_model import BaseModel


class User(BaseModel):
    """Act as a User's Representative.

    Qualities:
        email (str): The user's email address.
        password (str): The user's password.
        First name (str): The user's first name.
        last_name (str): The user's last name.

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
