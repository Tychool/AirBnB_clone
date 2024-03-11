#!/usr/bin/python3
"""This script contains unit test module for file_storage.py
"""

import json
import os
import pep8
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
"""
Unittesting for file_storage
"""


class TestFileStorage(unittest.TestCase):
    """
    Testing methods within FileStorage class
    """
    @classmethod
    def setUpClass(cls):
        """ Creates instance of a class to test """
        cls.test_user_instance = User()
        cls.test_user_instance.first_name = "Betty"
        cls.test_user_instance.last_name = "Holberton"
        cls.test_user_instance.email = "betty@holbertonschool.com"
        cls.test_user_instance.password = "password123"

    @classmethod
    def tearDownClass(cls):
        """ Deletes instance of the class """
        del cls.test_user_instance
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """ Tests this script for PEP8 styling """
        style_checker = pep8.StyleGuide(quiet=True)
        errors8 = style_checker.check_files(['models/engine/file_storage.py'])
        self.assertEqual(pep8_errors.total_errors, 0, "Fails PEP8")

    def test_all_method(self):
        """ Tests all() method """
        file_storage_instance = FileStorage()
        instance_dict = file_storage_instance.all()
        self.assertIsNotNone(instance_dict)
        self.assertEqual(type(instance_dict), dict)
        fs_object = file_storage_instance._FileStorage__objects
        self.assertIs(instance_dict, fs_object)

    def test_new_method(self):
        """ Tests new() method """
        self.setUpClass()
        file_storage_instance = FileStorage()
        file_storage_instance.new(self.test_user_instance)
        self.assertIsNotNone(file_storage_instance.all())

    def test_save_method(self):
        """ Tests save() method """
        base_model_instance = BaseModel()
        file_storage_instance = FileStorage()
        file_storage_instance.new(base_model_instance)
        file_storage_instance.save()
        self.assertEqual(os.path.exists('file.json'), True)

    def test_reload_method(self):
        """ Tests reload() method """
        base_model_instance = BaseModel()
        file_storage_instance = FileStorage()
        file_storage_instance.new(base_model_instance)
        file_storage_instance.save()
        reloaded_data = file_storage_instance.reload()
        self.assertTrue(reloaded_data is file_storage_instance.reload())


if __name__ == '__main__':
    unittest.main()
