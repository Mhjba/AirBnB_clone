#!/usr/bin/python3
"""Defines all common attributes/methods  for other classes."""
import uuid
import models
from datetime import datetime


class BaseModel:
    """Instance attributes"""
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel
        args:

            *args: list of arguments.
            **kwargs: Key/valu of arguments.

        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                        continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, t_format))

                else:
                    setattr(self, key, value)
                
            else:
                models.storage.new(self)

    def save(self):
        """Update the public instance attribute updated_at."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values."""
        t_dict = self.__dict__.copy()
        t_dict['__class__'] = self.__class__.__name__
        t_dict['created_at'] = self.created_at.isoformat()
        t_dict['updated_at'] = self.updated_at.isoformat()
        return t_dict

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

