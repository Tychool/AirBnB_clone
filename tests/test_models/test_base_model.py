#!/usr/bin/python3
"""This script contains the unit test module for BaseModel
"""

from models.base_model import BaseModel
import pep8
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Unit test for BaseModel
    """

    @classmethod
    def setUpClass(cls):
        """ Sets up instance """
        cls.base_model_instance = BaseModel()
        cls.base_model_instance.name = "Betty"
        cls.base_model_instance.my_number = 100

    @classmethod
    def tearDownClass(cls):
        """ Deletes instance """
        del cls.base_model_instance

    def test_pep8(self):
        """ check PEP8 styling """
        style_checker = pep8.StyleGuide(quiet=True)
        pep8_errors = style_checker.check_files(['models/base_model.py'])
        self.assertEqual(pep8_errors.total_errors, 0, 'Fails PEP8')

    def test_docstrings(self):
        """ look for docstrings """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_id_generation(self):
        """ check uid gen"""
        base_model_instance1 = BaseModel()
        base_model_instance2 = BaseModel()
        self.assertIsInstance(base_model_instance1, BaseModel)
        self.assertTrue(hasattr(base_model_instance1, "id"))
        self.assertNotEqual(base_model_instance1.id, base_model_instance2.id)
        self.assertIsInstance(base_model_instance1.id, str)
        self.assertIsInstance(base_model_instance2, BaseModel)
        self.assertTrue(hasattr(base_model_instance2, "id"))
        self.assertIsInstance(base_model_instance2.id, str)

    def test_created_updated_consistency(self):
        """ check consitency of serialization: """
        self.setUpClass()
        self.assertTrue(isinstance(self.base_model_instance, BaseModel))
        created = self.base_model_instance.created_at
        updated = self.base_model_instance.updated_at
        self.assertEqual(created, updated)


if __name__ == '__main__':
    unittest.main()
