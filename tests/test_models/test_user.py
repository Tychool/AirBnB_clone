#!/usr/bin/python3
""" Tests class State """
import unittest
from models.state import State
from models.base_model import BaseModel
import os
import pep8


class TestState(unittest.TestCase):
    """ Test cases for the State class """

    @classmethod
    def setUpClass(cls):
        """ Set up an instance of State """
        cls.user_instance = User()
        cls.user_instance.first_name = "Holberton"
        cls.user_instance.last_name = "School"
        cls.user_instance.email = "user@example.com"
        cls.user_instance.password = "default123"

    @classmethod
    def tearDownClass(cls):
        """ Tear down the test environment """
        del cls.user_instance
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """ Check if the script complies with PEP8 """
        pep8_style_checker = pep8.StyleGuide(quiet=True)
        pep8_errors = pep8_style_checker.check_files(['models/user.py'])
        self.assertEqual(pep8_errors.total_errors, 0, "Fails PEP8")

    def test_functions(self):
        """ Check for docstrings inside State class """
        self.assertIsNotNone(State.__doc__)

    def test_subclass_of_base_model(self):
        """ Check if instance is a subclass of BaseModel """
        self.setUpClass()
        sub_class = self.user_instance.__class__
        self.assertTrue(issubclass(sub_class, BaseModel), True)

    def test_save_method(self):
        """ Test the functionality of the save method """
        self.setUpClass()
        self.user_instance.save()
        created = self.user_instance.created_at
        updated = self.user_instance.updated_at
        self.assertNotEqual(created, updated)


if __name__ == '__main__':
    unittest.main()
