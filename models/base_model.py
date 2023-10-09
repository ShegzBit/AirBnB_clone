#!/usr/bin/env python3
"""
A module for Base model for all classes in AirBnB console
"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    Base class for all other classes in AirBnB project to inherit from
    it contain all neccessary method for smooth operation of each class
    """

    def __init__(self):
        """
        Class constructor for base module
        Init the public instance attribute `id`
        """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        String representation of BaseModel class
        """
        class_name = __class__.__name__
        id = self.id
        my_dict = self.__dict__

        return f'[{class_name}] ({id}) {my_dict}'
    def save(self):
        """
        Update the public instance `updated_at` with
        current datetime
        """
        self.updated_at = datetime.now()
    
if __name__ == "__main__":
    b1 = BaseModel()
    print(b1)
