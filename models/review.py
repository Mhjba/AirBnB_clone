#!/usr/bin/python3
"""
This class creates review objects.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review objects are created by this class.
    """
    place_id = ""
    user_id = ""
    text = ""
