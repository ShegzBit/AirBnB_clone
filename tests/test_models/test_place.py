#!/usr/bin/python3
"""
    Test class the Place class
"""
from models.place import Place
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from unittest.mock import patch
import io


class TestPlace(unittest.TestCase):
    """Test class the Place class"""
    my_place = Place()

    def test_instance_attributes(self):
        """tests if an instance has all attributes
        that makes up a place
        """
        self.assertTrue(hasattr(TestPlace.my_place, "name"))
        self.assertTrue(hasattr(TestPlace.my_place, "state_id"))

    def test_place_print(self):
        """tests the format the place is printed in"""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(TestPlace.my_place)
        expected_output = (
            "[Place] ({}) ".format(TestPlace.my_place.id) +
            "{}".format(TestPlace.my_place.__dict__)
        )


if __name__ == "__main__":
    unittest.main()