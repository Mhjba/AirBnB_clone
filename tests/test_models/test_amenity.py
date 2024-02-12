#!/usr/bin/python3
""" Contains unit tests for class BaseModel """

import unittest
import sys
import os
from datetime import datetime
from models.base_model import BaseModel
import models


class TestBaseModel(unittest.TestCase):
    """test for class BaseModel and its methods
    """
    def setUp(self):
        """ Set up method
        """
        self.model = BaseModel()
        self.modl = BaseModel()

    def tearDown(self):
        """
        Resets tests
        """
        try:
            os.remove("file.json")
        except FileNotFoundErro:
            pass

    def test_kw(self):
        """ Test to init for kwargs
        """
        self.model.name = "Holberton"
        model_json = self.model.to_dict()
        new_model = BaseModel(**model_json)
        self.assertDictEqual(model_json, new_model.to_dict())
        self.assertIn("name", new_model.to_dict())
        self.assertIsNot(self.model, new_model)

    def test__str__(self):
        """[Cheking correct output when printing]"""
        cls = self.model.id
        self.assertTrue(f'[BaseModel] ({cls})' in str(self.model))

    def test_save(self):
        """Checks if updated_at is changed with save method"""
        self.model.save()
        self.assertNotEqual(self.model.updated_at,
                            self.model.created_at)

    def test_save_with_file(self):
        """ Checks if the generated key is saved in the json file"""
        obj = BaseModel()
        obj.save()
        key_id = f"BaseModel.{obj.id}"
        with open("file.json", mode="r", encoding="utf-8") as file:
            self.assertIn(key_id, file.read())

    def test_to_dict(self):
        """Checks to_dict method"""
        base_test4 = BaseModel()
        dict_base4 = base_test4.to_dict()
        self.assertIsInstance(dict_base4, dict)
        self.assertIsInstance(dict_base4['created_at'], str)
        self.assertIsInstance(dict_base4['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
