#!/usr/bin/python3

"""
Provides the FileStorage class for serialization and deserialization of instances.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances"""

"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel


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

        """Returns the dictionary of all objects."""
        return self.__objects

    def new(self, obj):
        """Sets the object in the dictionary of objects."""
        if obj:
            key = f'{type(obj).__name__}.{obj.id}'
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        temp = self.__objects
        obj_dict = {obj: temp[obj].to_dict() for obj in temp.keys()}
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            f.write(json.dumps(obj_dict))

    def reload(self):
        """ Deserializes the JSON file to the dictionary of objects."""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                data = json.loads(f.read())
                for key, value in data.items():
                    model_name, model_id = key.split('.')
                    try:
                        self.new(eval(model_name)(**value))
                    except Exception as e:
                        print(e)

        except Exception:
            self.__objects = {}

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

