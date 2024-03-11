#!/usr/bin/python3
""" Tests class Amenity """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import os
import pep8


class TestAmenity(unittest.TestCase):
    """ Test cases for the Amenity class """

    @classmethod
    def setUpClass(cls):
        """ Set up an instance of Amenity """
        cls.amenity_instance = Amenity()
        cls.amenity_instance.name = "gym"

    @classmethod
    def tearDownClass(cls):
        """ Tear down the test environment """
        del cls.amenity_instance
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """ Check if the script complies with PEP8 """
        pep8_style_checker = pep8.StyleGuide(quiet=True)
        pep8_errors = pep8_style_checker.check_files(['models/amenity.py'])
        self.assertEqual(pep8_errors.total_errors, 0, "Fails PEP8")

    def test_docstrings(self):
        """ Check if methods inside Amenity class have docstrings """
        self.assertIsNotNone(Amenity.__doc__)

    def test_subclass_of_base_model(self):
        """ Check if instance is a subclass of BaseModel """
        self.setUpClass()
        sub_class = self.amenity_instance.__class__
        self.assertTrue(issubclass(sub_class, BaseModel), True)

    def test_save_method(self):
        """ Test the functionality of the save method """
        self.setUpClass()
        self.amenity_instance.save()
        created = self.amenity_instance.created_at
        updated = self.amenity_instance.updated_at
        self.assertNotEqual(created, updated)


if __name__ == '__main__':
    unittest.main()
