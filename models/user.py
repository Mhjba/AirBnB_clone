#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):"""class define User model inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
