#!/usr/bin/python3
"""file storage engine"""
import json
import os.path


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with
           key <obj class name>.id"""
        self.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects
           only if the file exists"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
                    self.new(value)
        except:
            pass
