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
        d = {}
        for key in self.__objects:
            d[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(d, f)

    def reload(self):
        """deserializes the JSON file to __objects
           only if the file exists"""
        try:
            with open(self.__file_path, 'r') as f:
                d = json.load(f)
            for key in d.keys():
                self.__objects[key] = d[]
        except:
            pass
