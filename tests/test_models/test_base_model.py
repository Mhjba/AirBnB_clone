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
        except:
            pass

    def test_uuid(self):
        """ Test for uuid
        """
        self.assertNotEqual(self.model.id, self.modl.id)
        self.assertTrue(hasattr(self.model, "id"))
        self.assertEqual(type(self.model.id), str)
        self.assertEqual(type(self.modl.id), str)

    def test_ins(self):
        """ Test for instance
        """
        self.assertTrue(isinstance(self.model, BaseModel))
        self.assertTrue(isinstance(self.modl, BaseModel))

    def test_save(self):
        """ Test for save
        """
        cls= self.model.updated_at
        self.model.save()
        self.assertFalse(cls == self.model.updated_at)

    def test_update(self):
        """ Test for update
        """
        self.model.name = "Holberton"
        self.assertTrue(hasattr(self.model, "name"))

    def test_kw(self):
        """ Test to init for kwargs
        """
        self.model.name = "Holberton"
        model_json = self.model.to_dict()
        new_model = BaseModel(**model_json)
        self.assertDictEqual(model_json, new_model.to_dict())
        self.assertIn("name", new_model.to_dict())
        self.assertIsNot(self.model, new_model)

    def test_sto(self):
        """ Test to staorage
        """
        obj_dict = models.storage.all()
        self.assertTrue(obj_dict)

    def test_docstr(self):
        """ test doc in the file
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
    
    def test__str__(self):
        """[Cheking correct output when printing]"""
        cls = self.model.id
        self.assertTrue(f'[BaseModel] ({cls})' in str(self.model))

if __name__ == '__main__':
    unittest.main()
