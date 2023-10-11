#!/usr/bin/python3
"""
    Tests for the base class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBase(unittest.TestCase):
    """test class for the base class"""
    def setUp(self):
        """set up test methods"""
        self.my_model = BaseModel()

    def test_instance_attributes(self):
        """test attriutes of the created instance of the base class"""
        self.assertTrue(hasattr(self.my_model, "id"))
        self.assertTrue(hasattr(self.my_model, "created_at"))
        self.assertTrue(hasattr(self.my_model, "updated_at"))

    def test_id_is_string(self):
        """tests if id generated is a string"""
        self.assertIsInstance(self.my_model.id, str)

    def test_instance_datetime(self):
        """tests the created at and updated time of the instance """
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

    def test_str_method(self):
        """test the __str__ method"""
        my_str = "[BaseModel] ({}) {}]"./
        format(self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), my_str)

    def test_save_method(self):
        """tests the save method"""
        prev_updated_at = self.my_model.updated_at
        self.my_model.save()
        new_updated_at = self.my_model.updated_at
        self.assertNotEqual(prev_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """tests the to dict method"""
        obj_dict = self.my_model.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict["id"], self.my_model.id)
        self.assertEqual(obj_dict["created_at"],
                         self.model.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"],
                         self.model.updated_at.isoformat())
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_init_from_dict(self):
        """Test re-creating an instance from a dictionary representation"""
        model_dict = self.my_model.to_dict()
        new_model = BaseModel(**model_dict)

        self.assertEqual(self.my_model.id, new_model.id)
        self.assertEqual(self.my_model.created_at, new_model.created_at)
        self.assertEqual(self.my_model.updated_at, new_model.updated_at)


if __name__ == "__main__":
    unittest.main()
