#!/usr/bin/python3
"""Test cases for the console module"""

import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import console
from console import HBNBCommand
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """Test cases for the console module"""

    @classmethod
    def setUpClass(cls):
        """Set up the HBNBCommand instance"""
        cls.hbnb_command = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Clean up the HBNBCommand instance"""
        del cls.hbnb_command

    def tearDown(self):
        """Remove the JSON file created during testing"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_compliance(self):
        """Test PEP8 compliance of the console module"""
        style_checker = pep8.StyleGuide(quiet=True)
        pep8_errors = style_checker.check_files(["console.py"])
        self.assertEqual(pep8_errors.total_errors, 0, 'PEP8 Failed')

    def test_docstrings(self):
        """Check docstrings of methods in the console module"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_empty_input(self):
        """Test behavior of emptyline method"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.hbnb_command.onecmd("\n")
            self.assertEqual('', output.getvalue())

    def test_quit_command(self):
        """Test behavior of quit method"""
        with patch('sys.stdout', new=StringIO()) as output:
            with self.assertRaises(SystemExit):
                self.hbnb_command.onecmd("quit")
            self.assertEqual('', output.getvalue())
