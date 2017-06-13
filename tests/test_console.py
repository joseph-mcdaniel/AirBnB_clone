#!/usr/bin/python3
import unittest
import sys
from console import HBNBCommand
from unittest.mock import create_autospec


class TestConsole(unittest.TestCase):
    def setUp(self):
        """ standard setUp """
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        """ create """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_exit(self):
        """ test exit command """
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))
        self.assertTrue(cli.onecmd("EOF"))

    def test_class_error(self):
        """ show error whenn class is missing or doesn't exist """
        cli = self.create()
        self.assertFalse(cli.onecmd("create"))
        self.assertEqual("** class name missing **", self._last_write())
        self.mock_stdout.reset_mock()
        self.assertFalse(cli.onecmd("create my_model"))
        self.assertEqual("** class doesn't exist **", self._last_write())

    def _last_write(self, nr=None):
        """:return: last `n` output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0],
                           self.mock_stdout.write.call_args_list[-nr:]))

if __name__ == "__main__":
    unittest.main()