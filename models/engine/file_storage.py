#!/usr/bin/env python3
"""
This module contains a file storage system for Base Model and
it subclasses
"""
import json
from os import path


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
        return FileStorage.__object
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.to_dict()["__class__"] + str(obj.id)
        FileStorage.__object.update({key: obj.to_dict()})

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        my_object = FileStorage.__object
        filename = FileStorage.__file_path
        # write __object to json file
        with open(filename, "w") as f:
            json.dump(my_object, f, indent=2)

    def reload(self):
        """
        deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """

        filename = FileStorage.__file_path
        obj_dict = FileStorage.__object
        # check if file_path exists
        if not path.exists(filename):
            return
        # opens the file and parses json string into a dictionary
        with open(filename, "r", encoding="utf-8") as f:
            FileStorage.__object = json.load(f)