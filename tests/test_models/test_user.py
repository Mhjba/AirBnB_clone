#!/usr/bin/python3
"""Defines unittests for models/user.py.
"""

import unittest
import os
from models import storage
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser_instantiation(unittest.TestCase):
    """User model class test case"""
    """test for user"""
    def setUp(self):
        """ standard setUp()
        """
        self.model = User()
    def setUpClass(cls):
        """Setup the unittest"""
        cls.model = User()
        cls.model.email = "me@example.com"
        cls.model.password = "123i123"
        cls.model.first_name = "John"
        cls.umodel.last_name = "Swag"

    def test_has_attributes(self):
        """ if public attributes are exist and if equal to empty string
        """
        self.assertTrue('id' in self.model.__dict__)
        self.assertTrue('created_at' in self.model.__dict__)
        self.assertTrue('updated_at' in self.model.__dict__)
        self.assertTrue('email' in self.model.__dict__)
        self.assertTrue('password' in self.model.__dict__)
        self.assertTrue('first_name' in self.model.__dict__)
        self.assertTrue('last_name' in self.model.__dict__)

    def test_attributes_are_string(self):
        """ input for each attr
        """
        self.model.email = "airbnb@holbertonshool.com"
        self.model.password = "root"
        self.model.first_name = "Betty"
        self.model.last_name = "Holberton"
        self.assertIs(type(self.model.email), str)
        self.assertIs(type(self.model.password), str)
        self.assertIs(type(self.model.first_name), str)
        self.assertIs(type(self.model.last_name), str)

if __name__ == "__main__":
    unittest.main()
