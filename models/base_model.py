#!/usr/bin/python3
"""BaseModel python file"""
from datetime import datetime
from models import storage
import uuid


time_format = '%Y-%m-%dT%H:%M:%S.%f'

class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """public instance attributes"""
        """self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        value, time_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        value, time_format)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """prints [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
           with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
           of __dict__ of the instance"""
        d = {}
        d["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == "created_at":
                d[key] = self.created_at.strftime(time_format)
            elif key == "updated_at":
                d[key] = self.updated_at.strftime(time_format)
            else:
                d[key] = value
        return d
