#!/usr/bin/python3
"""
    Tests for the User class
"""
from models.user import User
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from unittest.mock import patch
import io


class TestUser(unittest.TestCase):
    """test class for the User class"""

    my_user = User()

    def test_instance_attributes(self):
        """tests if an instance has all attributes
        that makes up a user
        """
        attributes_to_check = [
            "email", "password", "first_name", "last_name"
        ]
        for attribute in attributes_to_check:
            self.assertTrue(hasattr(TestUser.my_user, attribute))

    def test_default_attr_values(self):
        """tests the default set attribute values"""
        attributes_to_check = [
            "email", "password", "first_name", "last_name"
        ]
        for attribute in attributes_to_check:
            default_val = ""
            self.assertEqual(getattr(TestUser.my_user, attribute), default_val)

    def test_user_print(self):
        """tests the format the user is printed in"""
        TestUser.my_user.first_name = "Hamida"
        TestUser.my_user.last_name = "The Great"
        TestUser.my_user.email = "sheisawesome@gmail.com"
        TestUser.my_user.password = "root"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(TestUser.my_user)
        expected_output = (
            "[User] ({}) ".format(TestUser.my_user.id) +
            "{}".format(TestUser.my_user.__dict__)
        )


if __name__ == "__main__":
    unittest.main()
