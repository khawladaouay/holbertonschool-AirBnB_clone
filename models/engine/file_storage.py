#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.base_model import BaseModel


classes = {"BaseModel": BaseModel}


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id."""
        obj = self.__objects["{}.{}".format(type(obj).__name__, obj.id)]

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects, if it exists"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                objdict = json.load(f)
            for key in objdict:
                self.__objects[key] = classes[objdict[key]["__class__"]](**objdict[key])
        except FileNotFoundError:
            pass
