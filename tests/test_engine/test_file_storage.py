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


class TestFileStorage(unittest.TestCase):
    """test class for file storage"""
    def setUp(self):
        """set up test methods"""
        self.my_model = BaseModel()
    
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


if __name__ == "__main__":
    unittest.main()