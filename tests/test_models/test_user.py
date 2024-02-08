#!/usr/bin/python3
"""Unittest for User"""

from contextlib import redirect_stdout
import unittest
from models.user import User
from datetime import datetime
import io
import os
import sys


class baseTest(unittest.TestCase):
    """Class that tests the User class"""

    def test_init(self):
        """Test initialisation"""
        model = User()
        model.name = "Test"
        self.assertEqual(model.name, 'Test')

    def test_init2(self):
        """Test initialisation"""
        model = User()
        model.name = "Test"
        model.my_number = 29
        self.assertEqual(model.name, "Test")
        self.assertEqual(model.my_number, 29)

    def test_initkwargs(self):
        """Test initialization with kwargs"""
        model = User(name='Test', my_number=30)
        self.assertEqual(model.name, 'Test')
        self.assertEqual(model.my_number, 30)

    def test_initid(self):
        """Test allocation of uuid"""
        model = User()
        self.assertEqual(type(model.id), str)
        self.assertEqual(len(model.id), 36)

    def test_initdate(self):
        """Test datetime"""
        model = User()
        x = str(datetime.now())[:-10]
        y = str(model.created_at)[:-10]
        z = str(model.updated_at)[:-10]
        self.assertEqual(x, y)

    def test_str(self):
        """Test __str__"""
        model = User()
        model.name = "Test"
        model.my_number = 29
        output = ""
        with io.StringIO() as buf, redirect_stdout(buf):
            print(model)
            output = buf.getvalue()
        z = '\'my_number\': 29'
        x = z in output
        self.assertEqual(x, True)

    def test_save(self):
        """Test updating attributes after/during save"""
        model = User()
        x = model.updated_at
        model.name = "Test"
        model.save()
        self.assertNotEqual(x, model.updated_at)
        self.assertEqual(str(x)[:-10], str(model.updated_at)[:-10])

    def test_todict(self):
        """Test to_dict object function"""
        model = User()
        x = model.to_dict()
        self.assertEqual('id' in x.keys(), True)
        self.assertEqual('created_at' in x.keys(), True)
        self.assertEqual(type(x.get('created_at')), str)

    def test_todict2(self):
        """Test to_dict with new attributes"""
        model = User()
        model.name = "Test"
        x = model.to_dict()
        self.assertEqual('name' in x.keys(), True)
        self.assertEqual('number' in x.keys(), False)
        model.number = 29
        x = model.to_dict()
        self.assertEqual('number' in x.keys(), True)

    def test_modelfromdict(self):
        """Test creating User object from dict"""
        model = User()
        model.name = "Test"
        x = model.to_dict()
        self.assertEqual('number' in x.keys(), False)
        self.assertEqual('name' in x.keys(), True)
        model2 = User(**x)
        self.assertEqual(model2.name, 'Test')
        self.assertEqual(model2.created_at, model.created_at)


if __name__ == '__main__':
    unittest.main()
