#!/usr/bin/python3
import unittest
import json
import os
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class TestFileStorage(unittest.TestCase):
    """Unit tests for FileStorage class"""

    def setUpClass():
        """ check empty """
        try:
            os.rename("file.json")
        except Exception:
            pass

    def tearDownClass():
        """ check remove class """
        try:
            os.remove("file.json")
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def setUp(self):
        """Common setup for each test case"""
        self.file_path = FileStorage._FileStorage__file_path
        self.objects = FileStorage._FileStorage__objects

    def test_reload_with_arg(self):
        """Test the reload() method with an argument"""
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_init(self):
        """Test the initialization of FileStorage"""
        self.assertIsInstance(FileStorage(), FileStorage)
        self.assertIsInstance(storage, FileStorage)
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_attributes(self):
        """Test the private attributes of FileStorage"""
        self.assertIsInstance(self.file_path, str)
        self.assertIsInstance(self.objects, dict)

    def test_all(self):
        """Test the all of FileStorage"""
        self.assertIsInstance(storage.all(), dict)
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self):
        """Test the new of FileStorage"""
        obj = BaseModel()
        storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", self.objects)
        self.assertIn(obj, self.objects.values())
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    def test_save(self):
        """Test the save of FileStorage"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()

    def test_reload(self):
        """Test the reload of FileStorage"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()
        self.assertIn(f"BaseModel.{obj.id}", self.objects)

if __name__ == "__main__":
    unittest.main()
