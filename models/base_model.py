#!/usr/bin/python3
"""
Ce module contient la classe Basemodel
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Définit tous les attributs communs aux autres classes
    """

    def __init__(self, *args, **kwargs):
        """Instance constructor"""
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
        """Returns string rep of instance"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Met à jour l'attribut update_at avec la date/heure actuelle"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        temp = self.__dict__.copy()
        temp['created_at'] = self.created_at.isoformat()
        temp['updated_at'] = self.updated_at.isoformat()
        temp['__class__'] = type(self).__name__
        return temp
