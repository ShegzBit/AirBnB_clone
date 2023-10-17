#!/usr/bin/python3
"""
    test for the file storage
"""
import unittest
from unittest.mock import patch, mock_open
from models import storage
from models.base_model import BaseModel
from unittest.mock import patch, mock_open
from models.engine.file_storage import FileStorage
import io
from models.base_model import BaseModel
from models.user import User
from models.place import Place
import json


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

        my_storage = FileStorage()
        from_file = my_storage._FileStorage__objects
        self.assertEqual(my_storage.all(), from_file)

        my_storage.new(BaseModel())
        my_storage.new(BaseModel())
        self.assertEqual(my_storage.all(), from_file)

        my_storage.new(User())
        self.assertEqual(my_storage.all(), from_file)

    def test_save(self):
        """test updated save method"""
        str_json = io.StringIO()
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        self.my_model.save()
        local_storage = FileStorage()

        objs = ([BaseModel(), BaseModel(), BaseModel(), BaseModel(),
                User(), User(), Place()])
        for obj in objs:
            local_storage.new(obj)
        data = mock_open()
        with patch('builtins.open', data, create=True):
            local_storage.save()
            data.assert_called_with('file.json', 'w', encoding='utf-8')

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
        local_storage = FileStorage()

        objs = ([BaseModel(), BaseModel(), BaseModel(), BaseModel(),
                User(), User(), Place()])
        for obj in objs:
            local_storage.new(obj)
        local_storage.save()
        storage.reload()
        self.assertNotEqual(storage.all(), {})

    def test_new_method(self):
        """
        Tests new method
        """
        my_base = BaseModel()
        my_storage = FileStorage()

        my_storage.new(my_base)
        my_base_key = 'BaseModel.' + str(my_base.id)
        self.assertTrue(my_base_key in my_storage.all())
        self.assertEqual(my_base, my_storage.all()[my_base_key])

    def test_has_class_attributes(self):
        """
        Checks if File Storage has default class attributes and method
        """
        all = FileStorage().all
        new = FileStorage().new
        save = FileStorage().save
        reload = FileStorage().reload

        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage,
                        '_FileStorage__objects'))
        self.assertTrue(hasattr(FileStorage, 'all') and
                        type(all) is type(self.assertTrue))
        self.assertTrue(hasattr(FileStorage, 'new') and
                        type(new) is type(self.assertTrue))
        self.assertTrue(hasattr(FileStorage, 'save') and
                        type(save) is type(self.assertTrue))
        self.assertTrue(hasattr(FileStorage, 'reload') and
                        type(reload) is type(self.assertTrue))
        self.assertTrue(type('_FileStorage__file_path') is str)
        self.assertTrue(type('_FileStorage__objects') is str)


if __name__ == "__main__":
    unittest.main()
