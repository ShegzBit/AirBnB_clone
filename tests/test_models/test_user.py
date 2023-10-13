#!/usr/bin/python3
"""
    Tests for the User class
"""
from models.user import User
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage
from models import storage

class TestUser(unittest.TestCase):
    """test class for the User class"""

    my_user = User()
    my_user.first_name = "Hamida"
    my_user.last_name = "The Great"
    my_user.email = "sheisawesome@gmail.com"
    my_user.password = "root"

    def test_instance_attributes(self):
        """tests if an instance has all attributes
        that makes up a user
        """
        self.assertTrue(hasattr(TestUser.my_user, "email"))
        self.assertTrue(hasattr(TestUser.my_user, "password"))
        self.assertTrue(hasattr(TestUser.my_user, "first_name"))
        self.assertTrue(hasattr(TestUser.my_user, "last_name"))

    def test_user_print(self):
        """tests the format the user is printed in"""   


if __name__ == "__main__":
    unittest.main()
