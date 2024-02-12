#!/usr/bin/python3
"""Unittest module for the City Class.
"""
import unittest
from datetime import datetime
from models.city import City
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """City model class test case"""

    def setUpClass(cls):
        """Setup the unittest"""
    def setUp(self):
        """ standard setUp()
        """
        self.model = City()

    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_has_attributes(self):
        self.assertTrue('id' in self.model.__dict__)
        self.assertTrue('created_at' in self.model.__dict__)
        self.assertTrue('updated_at' in self.model.__dict__)
        self.assertTrue('state_id' in self.model.__dict__)
        self.assertTrue('name' in self.model.__dict__)

    def test_attributes_are_string(self):
        self.assertIs(type(self.model.state_id), str)
        self.assertIs(type(self.model.name), str)


if __name__ == "__main__":
    unittest.main()
