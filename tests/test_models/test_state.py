#!/usr/bin/python3
"""
    Tests for the State class
"""
from models.state import State
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from unittest.mock import patch
import io


class TestState(unittest.TestCase):
    """Test class the State class"""
    my_state = State()

    def test_instance_attributes(self):
        """tests if an instance has all attributes
        that makes up a state
        """
        self.assertTrue(hasattr(TestState.my_state, "name"))

    def test_default_attr_values(self):
        """tests the default set attribute values"""
        self.assertEqual(TestState.my_state.name, "")

    def test_state_print(self):
        """tests the format the state is printed in"""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(TestState.my_state)
        expected_output = (
            "[State] ({}) ".format(TestState.my_state.id) +
            "{}".format(TestState.my_state.__dict__)
        )


if __name__ == "__main__":
    unittest.main()
