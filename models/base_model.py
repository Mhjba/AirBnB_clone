#!/usr/bin/python3
"""
describes all the traits that other classes have in common.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    outlines every shared characteristic for other classes.
    """

    def __init__(self, *args, **kwargs):
        """constructor of instances"""
        if (kwargs):
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """gives back the instance's string representation."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """applies the current date and time to the updated_at attribute."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """yields a dictionary with all of the __dict__'s keys and values."""
        temp = self.__dict__.copy()
        temp['created_at'] = self.created_at.isoformat()
        temp['updated_at'] = self.updated_at.isoformat()
        temp['__class__'] = type(self).__name__
        return temp
