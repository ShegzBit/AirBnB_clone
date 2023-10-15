#!/usr/bin/python3
"""
    Tests for the Amenity class
"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from unittest.mock import patch
import io


class TestAmenity(unittest.TestCase):
    """Test class the Amenity class"""
    my_amenity = Amenity()

    def test_instance_attributes(self):
        """tests if an instance has all attributes
        that makes up a amenity
        """
        self.assertTrue(hasattr(TestAmenity.my_amenity, "name"))

    def test_default_attr_values(self):
        """tests the default set attribute values"""
        self.assertEqual(TestAmenity.my_amenity.name, "")

    def test_amenity_print(self):
        """tests the format the amenity is printed in"""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(TestAmenity.my_amenity)
        expected_output = (
            "[Amenity] ({}) ".format(TestAmenity.my_amenity.id) +
            "{}".format(TestAmenity.my_amenity.__dict__)
        )


if __name__ == "__main__":
    unittest.main()
