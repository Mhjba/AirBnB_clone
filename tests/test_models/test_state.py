#!/usr/bin/python3
"""Defines unittests for models state.
"""
import os
import unittest
from datetime import datetime
from models.state import State
from models import storage
from models.base_model import BaseModel


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""
    """ test for state
    """

    def setUp(self):
        """ standard setUp()
        """
        self.model = State()

    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_name_is_public_class_attribute(self):
        st = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(st))
        self.assertNotIn("name", st.__dict__)


if __name__ == "__main__":
    unittest.main()
