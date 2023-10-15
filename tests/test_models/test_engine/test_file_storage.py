#!/usr/bin/python3
"""
    test for the file storage
"""
import unittest
from models import storage
from models.base_model import BaseModel
from unittest.mock import patch
from models.engine.file_storage import FileStorage
import io
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """test class for file storage"""
    my_model = BaseModel()

    def test_all(self):
        """test the all method"""
        all_objs = storage.all()
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
        expected_output = ()

    def test_save(self):
        """test updated save method"""
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        self.my_model.save()
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(self.my_model)
        expected_output = (
            "[BaseModel] ({}) ".format(self.my_model.id) +
            "{}".format(self.my_model.__dict__)
        )

    def test_storage_instance(self):
        """tests if storage is an instance of FileStorage"""
        self.assertEqual(type(storage).__name__, "FileStorage")


if __name__ == "__main__":
    unittest.main()
