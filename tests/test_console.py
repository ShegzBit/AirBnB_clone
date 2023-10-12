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
    def test_create_base_model(self):
        """tests for the create method"""
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.input', return_value="BaseModel"):
            with patch('models.storage.save') as mock_save:
                console_instance.onecmd("create")
                mock_save.assert_called_once()

    def test_create_missing_classname(self):
        """tests for output when a classname is not passed"""
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.input', return_value=""):
            with patch('builtins.print') as mock_print:
                console_instance.onecmd("create")
                mock.print.assert_called_with("** class name missing **")
    
    def test_create_nonexisting_class(self):
        """tests for the output when a classname does not exist"""
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.input', return_value="NotAModel"):
            with patch('builtins.print') as mock_print:
                console_instance.onecmd("create")
                mock_print.assert_called_with("** class doesn't exist **")
    
    def test_help_create(self):
        """tests if the create command is documented"""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("help create")
        msg = 'Creates a new instance.\n'
        self.assertEqual(msg, mock_stdout.getvalue())

    def test_show_nonexisting_instance(self):
        "tests the show method when an instance is not created yet"
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.print') as mock_print:
            console_instance.onecmd("show BaseModel My_First_Model")
            mock_print.assert_called_with("** no instance found **")
    
    def test_show_existing_instance(self):
        """tests the show method when an instance is created with
        a valid classname and id
        """
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.print') as mock_print:
            




if __name__ == "__main__":
    unittest.main()