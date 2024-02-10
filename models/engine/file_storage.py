#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


class FileStorage():
    """
    Serializes instances to a JSON file and deserializes
    JSON file to instances attributes:

    __file_path: Path to JSON file
    __objects: Dictionary storing all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(cls_name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(FileStorage.__file_path, 'w') as file:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                obj_dict[key] = value.to_dict()
            obj_name = json.dumps(obj_dict)
            file.write(obj_name)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls = key.split('.')[0]
                    obj_name = eval(cls)(**value)
                    self.new(obj_name)
        except FileNotFoundError:
            pass

