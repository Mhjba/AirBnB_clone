#!/usr/bin/python3
"""
City module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Cette classe crée des objets de la ville
    """
    state_id = ""
    name = ""
