#!/usr/bin/python3
"""the City class is defined."""
from models.base_model import BaseModel


class City(BaseModel):
    """Act as a city's representative.

    Qualities:
        name (str): The city's name; state_id (str): The state id.

    """

    state_id = ""
    name = ""
