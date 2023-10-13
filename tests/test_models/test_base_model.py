#!/usr/bin/python3
"""
    Tests for the base class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBase(unittest.TestCase):
    """test class for the base class"""
    my_model = BaseModel()

    def test_instance_attributes(self):
        """test attriutes of the created instance of the base class"""
        self.assertTrue(hasattr(TestBase.my_model, "id"))
        self.assertTrue(hasattr(TestBase.my_model, "created_at"))
        self.assertTrue(hasattr(TestBase.my_model, "updated_at"))

    def test_id_is_string(self):
        """tests if id generated is a string"""
        self.assertIsInstance(TestBase.my_model.id, str)

    def test_instance_datetime(self):
        """tests the created at and updated time of the instance """
        self.assertIsInstance(TestBase.my_model.created_at, datetime)
        self.assertIsInstance(TestBase.my_model.updated_at, datetime)

    def test_str_method(self):
        """test the __str__ method"""
        self.maxDiff = None
        my_str = f"[BaseModel] ({TestBase.my_model.id}) {TestBase.my_model.__dict__}"
        self.assertEqual(str(TestBase.my_model), my_str)

    def test_save_method(self):
        """tests the save method"""
        prev_updated_at = TestBase.my_model.updated_at
        TestBase.my_model.save()
        new_updated_at = TestBase.my_model.updated_at
        self.assertNotEqual(prev_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """tests the to dict method"""
        obj_dict = TestBase.my_model.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict["id"], TestBase.my_model.id)
        self.assertEqual(obj_dict["created_at"],
                         TestBase.my_model.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"],
                         TestBase.my_model.updated_at.isoformat())
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_init_from_dict(self):
        """Test re-creating an instance from a dictionary representation"""
        model_dict = TestBase.my_model.to_dict()
        new_model = BaseModel(**model_dict)

        self.assertEqual(TestBase.my_model.id, new_model.id)
        self.assertEqual(TestBase.my_model.created_at, new_model.created_at)
        self.assertEqual(TestBase.my_model.updated_at, new_model.updated_at)


if __name__ == "__main__":
    unittest.main()
