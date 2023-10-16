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
from models import FileStorage
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
                id = io.StringIO()
                sys.stdout = id
                console_instance.onecmd("create BaseModel")
                mock_save.assert_called_once()
                sys.stdout = sys.__stdout__

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
                console_instance.onecmd("create Mydj")
                mock_print.assert_called_with("** class doesn't exist **")

    def test_help_create(self):
        """tests if the create command is documented"""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("help create")
        msg = 'creates a new object and saves it to the file\n'
        self.assertEqual(msg, mock_stdout.getvalue())

    def test_show_nonexisting_instance(self):
        """tests the show method when an instance is not created yet"""
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.print') as mock_print:
            console_instance.onecmd("show BaseModel 121212")
            mock_print.assert_called_with("** no instance found **")

    def test_show_existing_instance(self):
        """tests the show method when an instance is created with
        a valid classname and id
        """
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch('builtins.print') as mock_print:
            # console_instance.onecmd("create BaseModel")
            # output = mock_print.call_args_list[0][0][0]
            id = str((BaseModel()).id)

            mock_print.reset_mock()
            console_instance.onecmd(f'show BaseModel {id}')
            self.assertTrue(id == mock_print.call_args_list[0][0][0].id)

    def test_show_missing_class(self):
        """tests the show method when no class is passed"""
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch("builtins.print") as mock_print:
            console_instance.onecmd("show")
            mock_print.assert_called_with("** class name missing **")

    def test_show_missing_id(self):
        """tests the show method when no id is passed"""
        console_instance = HBNBCommand()
        console_prompt = "(hbnb)"
        with patch("builtins.print") as mock_print:
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
            HBNBCommand().onecmd("help show")
        msg = 'Print the object of the class and id passed\n'
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
        with patch("builtins.print") as mock_print:
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
            HBNBCommand().onecmd("help destroy")
        msg = 'Destroy the object of the class and id passed\n'
        self.assertEqual(msg, mock_stdout.getvalue())

    def test_all_nonexisting_class(self):
        """tests the output of the all method when a class that
        does not exist is passed
        """
        console_instance = HBNBCommand()
        console_prompt = "(hbnb) "
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
            console_instance.onecmd("update BaseModel")
            mock_print.assert_called_with("** instance id missing **")

    def test_update_nonexising_instance(self):
        """tests the output of the update command when
        an instance the does not exist is passed
        """
        console_instance = HBNBCommand()
        with patch('builtins.print') as mock_print:
            console_instance.onecmd("update BaseModel 121212 \
                                     email 'airbnb@mail.com'")
            mock_print.assert_called_with("** no instance found **")

    def test_update_missing_attribute_name(self):
        """tests the output of the update command when
        an atrribute name is missing
        """
        console_instance = HBNBCommand()
        with patch('builtins.print') as mock_print:
            id = str((BaseModel()).id)
            console_instance.onecmd(f"update BaseModel {id}")
            mock_print.assert_called_with("** attribute name missing **")

    def test_update_missing_attribute_value(self):
        """tests the output of the update command when
        an atrribute value is missing
        """
        console_instance = HBNBCommand()
        with patch('builtins.print') as mock_print:
            id = str((BaseModel()).id)
            console_instance.onecmd(f"update BaseModel {id} email")
            mock_print.assert_called_with("** value missing **")

    def test_quit(self):
        """tests the quit method"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            with self.assertRaises(SystemExit) as context:
                HBNBCommand().onecmd("quit")

        self.assertEqual(context.exception.code, 0)
        output = f.getvalue()
        self.assertEqual(output, "")

    def test_help_quit(self):
        """tests if the quit command is documented"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        msg = 'Quit command to exit the program\n'
        self.assertEqual(msg, f.getvalue())

    def test_EOF(self):
        """tests for the EOF method"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            with self.assertRaises(SystemExit) as context:
                HBNBCommand().onecmd("EOF")
        self.assertEqual(context.exception.code, 0)
        output = f.getvalue()
        self.assertEqual(output, "\n")

    def test_help_EOF(self):
        """tests if the EOF command is documented"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        msg = "cleanly exits command line interface on " + \
            "EOF signal (on `ctrl + D`)\n\n"
        self.assertEqual(msg, f.getvalue())

    def test_help(self):
        """tests the help command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help")
        msg = """
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

"""
        self.assertEqual(msg, f.getvalue())

    def test_emptyline(self):
        """tests the empty line"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("\n")
        msg = ""
        self.assertEqual(msg, f.getvalue())
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("                  \n")
        msg = ""
        self.assertEqual(msg, f.getvalue())


if __name__ == "__main__":
    unittest.main()
