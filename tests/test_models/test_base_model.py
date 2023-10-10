#!/usr/bin/python3
"""
    Tests for the base class
"""
import unittest
from models.base_model import BaseModel

class TestBase(unittest.TestCase):
    """test class for the base class"""
    def setUp(self):
        """set up test methods"""
        pass

    def test_init(self):
        """test the initialization of the base model"""
        my_model = BaseModel
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)
        self.assertEqual(my_model.created_at, my_model.updated_at)

if __name__ == "__main__":
    unittest.main()
    