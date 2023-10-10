#!/usr/bin/env python3
"""
This module contains a file storage system for Base Model and
it subclasses
"""
from models.base_model import BaseModel
import json


class FileStorage:
    """
    A file storage system to persist objects created during execution of airbnb console
    """
    __file_path = "file.json"
    __object = {}

    def all(self):
        """
        Returns a dictionary of all objects that has been created
        """
        return type(self).__object
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "BaseModel." + str(obj.id)
        type(self).__object.update({key: obj.to_dict})

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        my_object = type(self).__object
        filename = my_object.__file_path
        # write __object to json file
        with open(filename, "w") as f:
            json.dump(my_object, f, indent=2)
        
    def reload(self):
        """
        
        """