#!/usr/bin/python3
"""Test model for Review class
"""
import unittest
import os
from datetime import datetime
from models import storage
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Review model class test case"""

    """ test for review
    """
    def setUp(self):
        """ standard setUp()
        """
        self.model = Review()

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
        self.assertTrue('user_id' in self.model.__dict__)
        self.assertTrue('place_id' in self.model.__dict__)
        self.assertTrue('text' in self.model.__dict__)

    def test_attributes_are_string(self):
        self.assertIs(type(self.model.user_id), str)
        self.assertIs(type(self.model.place_id), str)
        self.assertIs(type(self.model.text), str)


if __name__ == "__main__":
    unittest.main()
