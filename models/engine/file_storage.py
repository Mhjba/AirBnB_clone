#!/usr/bin/python3
"""defines the class FileStorage."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Act as a storage engine abstraction.

    Qualities:
        __file_path (str): The filename to which objects should be saved.
        A dictionary of instantiated objects is called __objects (dict).

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Give the dictionary back to __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Use the key <obj_class_name>.id to set obj in __objects."""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """__objects should be serialized to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """If the JSON file __file_path exists, deserialize it to __objects."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
