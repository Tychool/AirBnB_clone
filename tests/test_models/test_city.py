#!/usr/bin/python3
""" Tests class City """
import models
from models.city import City
from models.base_model import BaseModel
import os
import pep8
import unittest


class TestCity(unittest.TestCase):
    """ Test cases for the City class """

    @classmethod
    def setUpClass(cls):
        """ Set up an instance of City and its attributes """
        cls.city_instance = City()
        cls.city_instance.name = "Kano"
        cls.city_instance.state_id = "KanoNG"

    @classmethod
    def tearDownClass(cls):
        """ Tear down the test environment """
        del cls.city_instance
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_functions(self):
        """ Check for docstrings inside City class """
        self.assertIsNotNone(City.__doc__)

    def test_pep8(self):
        """ Check if the script complies with PEP8 """
        pep8_style_checker = pep8.StyleGuide(quiet=True)
        pep8_errors = pep8_style_checker.check_files(['models/city.py'])
        self.assertEqual(pep8_errors.total_errors, 0, "Fails PEP8")

   def test_subclass_of_base_model(self):
        """ Check if instance is a subclass of BaseModel """
        self.setUpClass()
        sub_class = self.city_instance.__class__
        self.assertTrue(issubclass(sub_class, BaseModel), True)

    def test_save_method(self):
        """ Test the functionality of the save method """
        self.setUpClass()
        self.city_instance.save()
        created = self.city_instance.created_at
        updated = self.city_instance.updated_at
        self.assertNotEqual(created, updated)


if __name__ == '__main__':
    unittest.main()
