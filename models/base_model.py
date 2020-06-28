#!/usr/bin/python3
"""BaseModel python file"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class"""

    def __init__(self):
        """public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """prints [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
           with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
           of __dict__ of the instance"""
        d = {}
        d["__class__"] = self.__class__.__name__
        f = '%Y-%m-%dT%H:%M:%S.%f'
        for key, value in self.__dict__.items():
            if key == "created_at":
                self.created_at = self.created_at.strftime(f)
                d["created_at"] = self.created_at
            elif key == "updated_at":
                self.updated_at = self.updated_at.strftime(f)
                d["updated_at"] = self.updated_at
            else:
                d[key] = value
            return d
