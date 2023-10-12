#!/usr/bin/python3
"""
    test for the console
"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from models.base_model import BaseModel
import io
from models import storage
from models.engine.file_storage import FileStorage
import sys
import json


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
                mock_print.assert_called_with("** class name missing **")

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
            console_instance.onecmd("show BaseModel 121212")
            mock_print.assert_called_with("** no instance found **")

    def test_show_existing_instance(self):
        """tests the show method when an instance is created with
        a valid classname and id
        """
        # TODO:I am unsure of how this will behave
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.print') as mock_print:
            console_instance.onecmd("create BaseModel")
            output = mock_print.call_args_list[0][0][0]

            mock_print.reset_mock()
            console_instance.onecmd(f'show BaseModel {output}')
            self.assertTrue(output in mock_print.call_args_list[0][0][0])

    def test_show_missing_class(self):
        """tests the show method when no class is passed"""
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch("builtin.print") as mock_print:
            console_instance.onecmd("show")
            mock_print.assert_called_with("** class name missing **")

    def test_show_missing_id(self):
        """tests the show method when no id is passed"""
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch("builtin.print") as mock_print:
            console_instance.onecmd("show BaseModel")
            mock_print.assert_called_with("** instance id missing **")

    def test_show_nonexisting_class(self):
        "tests the show method when a classname does not exist"
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.print') as mock_print:
            console_instance.onecmd("show MyModel")
            mock_print.assert_called_with("** class doesn't exist **")

    def test_help_show(self):
        """tests if the show command is documented"""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("help create")
        msg = 'Prints the string representation of an \
        instance based on the class name and id\n'
        self.assertEqual(msg, mock_stdout.getvalue())

    def test_destroy_missing_class(self):
        """tests the destroy method for when no classname is passed"""
        console_instance = HBNBCommand()
        console_prompt = '(hbnb)'
        with patch('builtins.print') as mock_print:
            console_instance.onecmd("destroy")
            mock_print.assert_called_with("** class name missing **")

    def test_destroy_nonexisting_class(self):
        """tests the output of the destroy method for
        when a class does not exist
        """
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.print') as mock_print:
            console_instance.onecmd("destroy MyModel")
            mock_print.assert_called_with("** class doesn't exist **")

    def test_destroy_missing_id(self):
        """tests the output of the destroy method
        when an id is not passed
        """
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch("builtin.print") as mock_print:
            console_instance.onecmd("destroy BaseModel")
            mock_print.assert_called_with("** instance id missing **")

    def test_destroy_nonexisting_instance(self):
        "tests the destroy method when an instance is not created yet"
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.print') as mock_print:
            console_instance.onecmd("destroy BaseModel 121212")
            mock_print.assert_called_with("** no instance found **")

    def test_destroy_existing_instance(self):
        """tests the output for the destroy method for an existing
        instance
        """
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.print') as mock_print:
            console_instance.onecmd("create BaseModel")
            output = mock_print.call_args_list[0][0][0]

        mock_print.reset_mock()
        with patch('builtins.input', return_value=f"yes\n"):
            console_instance.onecmd(f'destroy BaseModel {output}')

        with patch('builtins.print') as mock_print:
            console_instance.onecmd(f"show BaseModel {output}")
            mock_print.assert_called_with("** no instance found **")

    def test_help_destroy(self):
        """tests if the destroy command is documented"""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("help create")
        msg = 'Deletes an instance based on the class name and id\n'
        self.assertEqual(msg, mock_stdout.getvalue())

    def test_all_nonexisting_class(self):
        """tests the output of the all method when a class that
        does not exist is passed
        """
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.print') as mock_print:
            console_instance.onecmd("all MyModel")
            mock_print.assert_called_with("** class doesn't exist **")

    def test_update_missing_class(self):
        """tests the output of the update method when
        no class is passed
        """
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.print') as mock_print:
            console_instance.onecmd("update")
            mock_print.assert_called_with("** class name missing **")

    def test_update_nonexisting_class(self):
        """tests the output of the update method when
        a class that does not exist is passed
        """
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.print') as mock_print:
            console_instance.onecmd("update MyModel 1234-1234-1234 \
                                    email 'airbnb@mail.com'")
            mock_print.assert_called_with("** class doesn't exist **")

    def test_update_missing_id(self):
        """tests the output of the update method
        when an id is not passed
        """
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.print') as mock_print:
            self.cmd_instance.onecmd("update BaseModel")
            mock_print.assert_called_with("** instance id missing **")

    def test_update_nonexising_instance(self):
        """tests the output of the update command when
        an instance the does not exist is passed
        """
        with patch('builtins.print') as mock_print:
            self.cmd_instance.onecmd("update BaseModel 121212 \
                                     email 'airbnb@mail.com'")
            mock_print.assert_called_with("** no instance found **")

    def test_update_missing_attribute_name(self):
        """tests the output of the update command when
        an atrribute name is missing
        """
        with patch('builtins.print') as mock_print:
            self.cmd_instance.onecmd("update BaseModel 1234-1234-1234")
            mock_print.assert_called_with("** attribute name missing **")

    def test_update_missing_attribute_value(self):
        """tests the output of the update command when
        an atrribute value is missing
        """
        with patch('builtins.print') as mock_print:
            self.cmd_instance.onecmd("update BaseModel 1234-1234-1234 email")
            mock_print.assert_called_with("** value missing **")

    def test_update_non_simple_arguments(self):
        """tests the output of the update command when
        non-simple args are passed
        """
        with patch('builtins.print') as mock_print:
            self.cmd_instance.onecmd("update BaseModel 1234-1234-1234 \
                                     my_list [1, 2, 3]")
            mock_print.assert_called_with("Only “simple” arguments can be \
                                          updated: string, integer and float.")


if __name__ == "__main__":
    unittest.main()
