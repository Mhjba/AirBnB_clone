#!/usr/bin/python3
"""The Place class is defined."""
from models.base_model import BaseModel


class Place(BaseModel):
    """symbolize a location.

    Qualities:
        city_id (str): This is the ID of the city.
        user_id (str): The id of the user.
        name (str): The location's name.
        description (str): The location's description.
        number_rooms (int): The location's total number of rooms.
        number_bathrooms (int): The location's bathroom count.
        max_guest (int): The location's maximum number of visitors.
        price_by_night (int): The location's price at night.
        latitude (float): The location's latitude.
        longitude (float): The location's longitude.
        amenity_ids (list): The Amenity ids are listed here.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
