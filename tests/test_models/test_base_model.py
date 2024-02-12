#!/usr/bin/python3
""" Contains unit tests for class BaseModel """

import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for class BaseModel"""

    def setUp(self):
        """Set up method"""

        self.model = BaseModel()

    def tearDown(self):
        """
        Resets tests
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init_kw(self):
        """Test to initialize with kwargs
        """
        self.model.name = "Holberton"
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertDictEqual(model_dict, new_model.to_dict())
        self.assertIn("name", new_model.to_dict())
        self.assertIsNot(self.model, new_model)

    def test_str(self):
        """Checking correct output when printing"""

        cls_id = self.model.id
        self.assertIn(f'[BaseModel] ({cls_id})', str(self.model))

    def test_save(self):
        """Checks if updated_at is changed with the save method"""

        self.model.save()
        self.assertNotEqual(self.model.updated_at, self.model.created_at)

    def test_save_method(self):
        """Checks if the generated key is saved in the json file"""

        obj = BaseModel()
        obj.save()
        key_id = f"BaseModel.{obj.id}"
        with open("file.json", mode="r", encoding="utf-8") as file:
            self.assertIn(key_id, file.read())

    def test_to_dict(self):
        """Checks to_dict method returns a dictionary"""

        cls = BaseModel()
        dict_to = cls.to_dict()
        self.assertIsInstance(dict_to, dict)
        self.assertIsInstance(dict_to['created_at'], str)
        self.assertIsInstance(dict_to['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
