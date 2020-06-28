#!/usr/bin/python3
"""BaseModel python file"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """public instance attributes"""
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    f = '2017-06-14T22:31:03.285259'
                    self.created_at = self.updated_at = datetime.strptime(
                        f, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    self.__dict__[key] = value
        else:
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
