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

    def all_classes(self):
        """Returns a dictionary of valid classes and their references"""
        all_classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return all_classes

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

    def test_new(self, classname):
        """tests the new method"""
        obj_class = TestFileStorage.all_classes()[classname]
        obj = obj_class()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertTrue(key in FileStorage.__objects)
        self.assertEqual(FileStorage.__objects[key], obj)


if __name__ == "__main__":
    unittest.main()
