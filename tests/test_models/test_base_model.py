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
        self.assertIsInstance(model, BaseModel)
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(mode.updated_at)
        self.assertEqual(model.created_at, model.updated_at)
    