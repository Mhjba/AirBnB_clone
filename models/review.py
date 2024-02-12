#!/usr/bin/python3
"""
Review class module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Cette classe crée des objets de révision
    """
    place_id = ""
    user_id = ""
    text = ""
