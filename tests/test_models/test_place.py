#!/usr/bin/python3
""" Tests class Place """
import unittest
from models.place import Place
from models.base_model import BaseModel
import os
import pep8


class TestPlace(unittest.TestCase):
    """ Test cases for the Place class """

    @classmethod
    def setUpClass(cls):
        """ Set up an instance of Place """
        cls.place_instance = Place()
        cls.place_instance.city_id = "KanoNG"
        cls.place_instance.user_id = "Sola"
        cls.place_instance.name = "Jaba"
        cls.place_instance.description = "Peace and quiet"
        cls.place_instance.number_rooms = 3
        cls.place_instance.number_bathrooms = 2
        cls.place_instance.max_guest = 8
        cls.place_instance.price_by_night = 10
        cls.place_instance.latitude = 0.0
        cls.place_instance.longitude = 0.0
        cls.place_instance.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        """ Tear down the test environment """
        del cls.place_instance
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """ Check if the script complies with PEP8 """
        pep8_style_checker = pep8.StyleGuide(quiet=True)
        pep8_errors = pep8_style_checker.check_files(['models/place.py'])
        self.assertEqual(pep8_errors.total_errors, 0, "Fails PEP8")

    def test_functions(self):
        """ Check for docstrings inside Place class """
        self.assertIsNotNone(Place.__doc__)

    def test_subclass_of_base_model(self):
        """ Check if instance is a subclass of BaseModel """
        self.setUpClass()
        self.assertTrue(issubclass(self.place_instance.__class__, BaseModel), True)

    def test_save_method(self):
        """ Test the functionality of the save method """
        self.setUpClass()
        self.place_instance.save()
        self.assertNotEqual(self.place_instance.created_at, self.place_instance.updated_at)


if __name__ == '__main__':
    unittest.main()
