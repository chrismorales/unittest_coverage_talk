# -*- coding: utf-8 -*-

import unittest


class BaseCoverageExample(unittest.TestCase):
    """
    All of the test cases for the methods that are defined within the
    CoverageExample class.
    """

    def _makeOne(self):
        """ Imports the class and return an instance. """
        from unittest_coverage_talk.example import ExampleOne
        return ExampleOne()

    def _callFUT(self):
        """ Calls the function under test and returns the output. """
        instance = self._makeOne()
        return instance.hello_world()

    def test_example_one_returns_expected_string(self):
        """
        Calling the function under test a string is returned and we expect the
        the string defined in the test to be equal.
        """

        expected_return = "Hello World"
        returned_value = self._callFUT()

        self.assertEqual(expected_return, returned_value)


