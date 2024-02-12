#!/usr/bin/python3
<<<<<<< HEAD
"""
This module contains FileStorage class
"""
=======
"""Defines the FileStorage class."""

>>>>>>> 5e6007f76892768484a8de792af1bf94be82d2e3
import json
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


<<<<<<< HEAD
class FileStorage:
<<<<<<< HEAD
    """sérialise les instances à un fichier JSON et
    désérialise le fichier json aux instances"""
=======
class FileStorage():
    """
    Serializes instances to a JSON file and deserializes
    JSON file to instances attributes:

    __file_path: Path to JSON file
    __objects: Dictionary storing all objects
    """
>>>>>>> 5e6007f76892768484a8de792af1bf94be82d2e3
=======
    """serializes instances to a JSON file and
    deserializes JSON file to instances"""
>>>>>>> parent of 0c45b91... update this file
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
<<<<<<< HEAD
<<<<<<< HEAD
        """désérialise le fichier JSON en __object"""
=======
        """Deserialize the JSON file __file_path to __objects, if it exists."""
>>>>>>> 5e6007f76892768484a8de792af1bf94be82d2e3
=======
        """deserializes the JSON file to __objects"""
>>>>>>> parent of 0c45b91... update this file
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls = key.split('.')[0]
                    obj_name = eval(cls)(**value)
                    self.new(obj_name)
        except FileNotFoundError:
            pass
