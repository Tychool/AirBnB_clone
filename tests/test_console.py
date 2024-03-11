#!/usr/bin/python3
"""This script contains unit test for console.py"""
"""Test cases for the console module"""

import unittest
from unittest.mock import patch
from io import StringIO
import os
import console
from console import HBNBCommand
import io
import sys
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for the HBNBCommand."""
    
    @classmethod
    def setUpClass(cls):
        """Set up the HBNBCommand instance"""
        cls.hbnb_command = HBNBCommand()

    def tearDown(self):
        """Clean up after the test."""
        pass

    def test_prompting(self):
        """Test if prompt includes '(hbnb) '."""
        with patch('builtins.input', return_value='quit'):
            self.assertTrue('(hbnb) ' in self.cmd.prompt)

    def test_help(self):
        """Test help command."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.cmd.do_help('')
            out = fake_out.getvalue().strip()
            self.assertTrue("Documented commands (type help <topic>):" in out)

    def test_exit(self):
        """Test exit command."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.assertTrue(self.cmd.do_EOF(''))

    def test_create(self):
        """Test create command."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.cmd.do_create('BaseModel')
            output = fake_out.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_show(self):
        """Test show command."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.cmd.do_show('BaseModel')
            output = fake_out.getvalue().strip()
            self.assertTrue("** instance id missing **" in output)
    @classmethod
    def tearDownClass(cls):
        """Clean up the HBNBCommand instance"""
        del cls.hbnb_command

    def test_all(self):
        """Test all command."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.cmd.do_all('')
            output = fake_out.getvalue().strip()
            self.assertTrue("[]" in output)

    def test_destroy(self):
        """Test destroy command."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.cmd.do_destroy('')
            output = fake_out.getvalue().strip()
            self.assertTrue("** class name missing **" in output)

    def test_update(self):
        """Test update command."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.cmd.do_update('')
            output = fake_out.getvalue().strip()
            self.assertTrue("** class name missing **" in output)


if __name__ == '__main__':
    unittest.main()
