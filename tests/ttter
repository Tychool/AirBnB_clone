#!/usr/bin/python3
"""This script contains unit test for console.py"""

import unittest
from unittest.mock import patch
from console import HBNBCommand
import io
import sys

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand()

    def tearDown(self):
        pass

    def test_prompting(self):
        with patch('builtins.input', return_value='quit'):
            self.assertTrue('(hbnb) ' in self.cmd.prompt)

    def test_help(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.cmd.do_help('')
            output = fake_out.getvalue().strip()
            self.assertTrue("Documented commands (type help <topic>):" in output)

    def test_exit(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.assertTrue(self.cmd.do_EOF(''))

    def test_create(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.cmd.do_create('BaseModel')
            output = fake_out.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_show(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.cmd.do_show('BaseModel')
            output = fake_out.getvalue().strip()
            self.assertTrue("** instance id missing **" in output)

    def test_all(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.cmd.do_all('')
            output = fake_out.getvalue().strip()
            self.assertTrue("[]" in output)

    def test_destroy(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.cmd.do_destroy('')
            output = fake_out.getvalue().strip()
            self.assertTrue("** class name missing **" in output)

    def test_update(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.cmd.do_update('')
            output = fake_out.getvalue().strip()
            self.assertTrue("** class name missing **" in output)

if __name__ == '__main__':
    unittest.main()

