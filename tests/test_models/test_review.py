#!/usr/bin/python3
"""
    Test class the Review class
"""
from models.review import Review
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from unittest.mock import patch
import io


class TestReview(unittest.TestCase):
    """Test class the Review class"""
    my_review = Review()

    def test_instance_attributes(self):
        """tests if an instance has all attributes
        that makes up a review
        """
        attributes_to_check = [
            "place_id", "user_id", "text",
        ]
        for attribute in attributes_to_check:
            self.assertTrue(hasattr(TestReview.my_review, attribute))

    def test_review_print(self):
        """tests the format the review is printed in"""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(TestReview.my_review)
        expected_output = (
            "[Review] ({}) ".format(TestReview.my_review.id) +
            "{}".format(TestReview.my_review.__dict__)
        )

    def test_default_attr_values(self):
        """tests the default set attribute values"""
        attributes_to_check = [
            "place_id", "user_id", "text",
        ]
        for attribute in attributes_to_check:
            default_val = ""
            self.assertEqual(getattr(TestReview.my_review, attribute),
                             default_val)


if __name__ == "__main__":
    unittest.main()
