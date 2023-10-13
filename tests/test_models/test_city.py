#!/usr/bin/python3
"""
    Test class the City class
"""
from models.city import City
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from unittest.mock import patch
import io


class TestCity(unittest.TestCase):
    """Test class the City class"""
    my_city = City()

    def test_instance_attributes(self):
        """tests if an instance has all attributes
        that makes up a city
        """
        self.assertTrue(hasattr(TestCity.my_city, "name"))
        self.assertTrue(hasattr(TestCity.my_city, "state_id"))

    def test_default_attr_values(self):
        """tests the default set attribute values"""
        self.assertEqual(TestCity.my_city.name, "")
        self.assertEqual(TestCity.my_city.state_id, "")

    def test_city_print(self):
        """tests the format the city is printed in"""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(TestCity.my_city)
        expected_output = (
            "[City] ({}) ".format(TestCity.my_city.id) +
            "{}".format(TestCity.my_city.__dict__)
        )


if __name__ == "__main__":
    unittest.main()
