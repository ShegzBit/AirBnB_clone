#!/usr/bin/python3
"""
    test for the console
"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from models.base_model import BaseModel
import io


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

    def test_all(self):
        """tests if the """



if __name__ == "__main__":
    unittest.main()
