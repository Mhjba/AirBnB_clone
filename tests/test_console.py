#!/usr/bin/python3
"""A unit test module for the console (command interpreter).
"""

import unittest
import json
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models import storage
from datetime import datetime
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """Represents the test class for the testconsole class.
    """

    def test_class(self):
        """Test for class BaseModel"""

        city = City()
        place = Place()
        review = Review()
        state = State()
        amenity = Amenity()
        self.assertEqual(city.__class__.__name__, "City")
        self.assertEqual(place.__class__.__name__, "Place")
        self.assertEqual(review.__class__.__name__, "Review")
        self.assertEqual(state.__class__.__name__, "State")
        self.assertEqual(amenity.__class__.__name__, "Amenity")

    def test_att(self):
        """
        attributes correcly from BaseModel
        """
        city = City()
        place = Place()
        review = Review()
        state = State()
        amenity = Amenity()
        self.assertTrue(issubclass(city.__class__, BaseModel))
        self.assertTrue(issubclass(place.__class__, BaseModel))
        self.assertTrue(issubclass(review.__class__, BaseModel))
        self.assertTrue(issubclass(state.__class__, BaseModel))
        self.assertTrue(issubclass(amenity.__class__, BaseModel))


if __name__ == '__main__':
    unittest.main()
