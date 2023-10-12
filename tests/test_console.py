#!/usr/bin/python3
"""
    test for the console
"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    """test class for the console"""
    def test_create_missing_classname(self):
        """tests for the create method"""
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.input', return_value="BaseModel"):
            with patch('models.storage.save') as mock_save:
                console_instance.onecmd("create")
                mock_save.assert_called_once()



if __name__ == "__main__":
    unittest.main()