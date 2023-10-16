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

    def test_new(self):
        """tests the new method to check if it saves an obj to
        __objects dictionary with the format <classname>.id"""
        self.assertIn("{}.{}".format("BaseModel", TestFileStorage.my_model.id),
                      storage._FileStorage__objects)

    def test_reload(self):
        """tests the reload method"""
        storage._FileStorage__file_path = "hamida.json"
        storage.reload()

    def test_attributes(self):
        """tests attributes present in file storage"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))


    def test_new_method(self):
        """
        Tests new method
        """
        my_base = BaseModel()
        my_storage = FileStorage()

        my_storage.new(my_base)
        my_base_key = 'BaseModel.' + str(my_base.id)
        self.assertTrue(my_base_key in my_storage.all())
        self.assertEqual(my_base, my_storage.all[my_base_key])

if __name__ == "__main__":
    unittest.main()
