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
        b_model = BaseModel
        self.assertIsInstance(b_model, BaseModel)
        self.assertIsNotNone(b_model.id)
        self.assertIsNotNone(b_model.created_at)
        self.assertIsNotNone(b_model.updated_at)
        self.assertEqual(b_model.created_at, b_model.updated_at)

if __name__ == "__main__":
    unittest.main()
    