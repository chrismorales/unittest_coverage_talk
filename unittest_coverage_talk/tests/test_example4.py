# -*- coding: utf-8 -*-
import unittest


class PeepHoleTest(unittest.TestCase):
    """
    Uses the BaseCoverageExample class which allows this test class to use the
    _makeOne method as a helper to get an instance for testing.
    """

    def _callFUT(self, username):
        """ Calls the function under test and returns the output. """
        from unittest_coverage_talk.example4 import peep_hole 
        return peep_hole(username) 

    def test_contains_special_char_returns_true(self):
        """
        Given a password defined in the list we expect the function to return
        True.
        """
        test_username = 'zerocool'

        expected_boolean = True
        returned_boolean = self._callFUT(test_username)

        self.assertEquals(expected_boolean, returned_boolean)

    def test_contains_special_char_returns_false(self):
        """
        Given a password not in the list we expect the function to return False.
        """
        test_username = 'usern@me'

        expected_boolean = False
        returned_boolean = self._callFUT(test_username)

        self.assertEquals(expected_boolean, returned_boolean)

