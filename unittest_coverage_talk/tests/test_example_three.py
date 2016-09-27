# -*- coding: utf-8 -*-

import unittest


class TestExampleThree(unittest.TestCase):
    """
    All test cases for the methods defined within the ExampleTwo class.
    """

    def _makeOne(self):
        """ Import the class and return an instance. """
        from unittest_coverage_talk.example_three import ExampleThree
        return ExampleThree()

    def _callFUT(self, username):
        """ Creates an instance and calls the function under test. """
        instance = self._makeOne()
        return instance.contains_special_char(username)

    def test_contains_special_char_returns_false(self):
        """
        Given a username within the list we expect the function to return True.
        """
        test_username = 'usern@me'
        expected_boolean = False
        returned_boolean = self._callFUT(test_username)

        self.assertEqual(expected_boolean, returned_boolean)

    def test_contain_special_char_returns_true(self):
        """
        Given a username with no special character we expect the function to
        return "valid"
        """
        test_username = "zerocool"
        expected_boolean = True
        returned_boolean = self._callFUT(test_username)

        self.assertEquals(expected_boolean, returned_boolean)
