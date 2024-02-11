#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import datetime

class TestAmenity(unittest.TestCase):
    """Amenity model class test case"""

    def setUp(self):
        """Setup the unittest"""
        self.model = Amenity()

    def tearDown(self):
        """Clean up the dirt"""
        del self.model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_public_att(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.model, 'name'))
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_string(self):
        """
        assertEqual input for each attr
        """
        self.assertIs(type(self.model.name), str)

if __name__ == "__main__":
    unittest.main()
