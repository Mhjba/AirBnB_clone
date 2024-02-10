#!/usr/bin/python3
""" Defines the User Class """
from models.base_model import BaseModel


class User(BaseModel):
    """ the User class that inherits BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
