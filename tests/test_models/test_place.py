#!/usr/bin/python3
#!/usr/bin/env python3
"""Test model for Place class"""

import unittest
import os
from models.place import Place
from datetime import datetime
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Place model class test case"""

    def setUp(self):
        """ standard setUp() """
        self.model = Place()
        self.model.save()

    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_public_attr(self):
        """ if public attribute exists and if equal to
        empty string, int, or float
        """
        self.assertTrue('id' in self.model.__dict__)
        self.assertTrue('created_at' in self.model.__dict__)
        self.assertTrue('updated_at' in self.model.__dict__)
        self.assertTrue('city_id' in self.model.__dict__)
        self.assertTrue('user_id' in self.model.__dict__)
        self.assertTrue('name' in self.model.__dict__)
        self.assertTrue('max_guest' in self.model.__dict__)
        self.assertTrue('price_by_night' in self.model.__dict__)
        self.assertTrue('latitude' in self.model.__dict__)
        self.assertTrue('longitude' in self.model.__dict__)
        self.assertTrue('amenity_ids' in self.model.__dict__)
        self.assertTrue('description' in self.model.__dict__)
        self.assertTrue('number_rooms' in self.model.__dict__)
        self.assertTrue('number_bathrooms' in self.model.__dict__)

    def test_string_attr(self):
        """ input for each attr
        """
        self.assertIs(type(self.model.city_id), str)
        self.assertIs(type(self.model.user_id), str)
        self.assertIs(type(self.model.name), str)
        self.assertIs(type(self.model.description), str)
        self.assertIs(type(self.model.number_rooms), int)
        self.assertIs(type(self.model.max_guest), int)
        self.assertIs(type(self.model.price_by_night), int)
        self.assertIs(type(self.model.latitude), float)
        self.assertIs(type(self.model.longitude), float)
        self.assertIs(type(self.model.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
