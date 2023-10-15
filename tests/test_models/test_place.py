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
        attributes_to_check = [
            "name", "city_id", "user_id", "description",
            "number_rooms", "number_bathrooms", "max_guest",
            "price_by_night", "latitude", "longitude", "amenity_ids"
        ]
        for attribute in attributes_to_check:
            self.assertTrue(hasattr(TestPlace.my_place, attribute))

    def test_place_print(self):
        """tests the format the place is printed in"""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(TestPlace.my_place)
        expected_output = (
            "[Place] ({}) ".format(TestPlace.my_place.id) +
            "{}".format(TestPlace.my_place.__dict__)
        )

    def test_default_attr_values(self):
        """tests the default set attribute values"""
        attributes_to_check = [
            "name", "city_id", "user_id", "description",
            "number_rooms", "number_bathrooms", "max_guest",
            "price_by_night", "latitude", "longitude", "amenity_ids"
        ]
        for attribute in attributes_to_check:
            if not isinstance(getattr(TestPlace.my_place, attribute), list):
                default_val = "" \
                    if isinstance(getattr(TestPlace.my_place, attribute), str)\
                    else 0
            else:
                default_val = []

            self.assertEqual(getattr(TestPlace.my_place, attribute),
                             default_val)


if __name__ == "__main__":
    unittest.main()
