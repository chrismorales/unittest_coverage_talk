# -*- coding: utf-8 -*-

import unittest


class GetNumberTest(unittest.TestCase):

    def _callFUT(self, odd_number):
        """Import get_number FUT, call it with passed odd_number"""
        from unittest_coverage_talk.example2 import get_number
        return get_number(odd_number)

    # def test_get_number_return_int_value_of_one(self):
    #     """
    #     Given a word in the list we expect the function to return True.
    #     """
    #     test_odd_number = True
    #     expected_number = 1
    #     returned_number = self._callFUT(test_odd_number)

    #     self.assertEqual(expected_number, returned_number)


    # def test_get_number_return_int_value_of_two(self):
    #     """
    #     Given a word in the list we expect the function to return True.
    #     """
    #     test_odd_number = False
    #     expected_number = 1
    #     returned_number = self._callFUT(test_odd_number)

    #     self.assertEqual(expected_number, returned_number)
