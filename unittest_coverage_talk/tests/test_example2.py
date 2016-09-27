# -*- coding: utf-8 -*-

import unittest

class GetNumberTest(unittest.TestCase):

    def _callFUT(self, odd_number):
        """Import get_number FUT, call it with passed odd_number"""
        from unittest_coverage_talk.example2 import get_number
        return get_number(odd_number)

    def test_get_number_return_int_value_of_one(self):
        """
        Test if get_number returns 1 when odd_number=True is passed in
        """
        test_odd_number = True
        expected_number = 1
        returned_number = self._callFUT(test_odd_number)

        self.assertEqual(expected_number, returned_number)

#    def test_get_number_return_int_value_of_two(self):
#        """
#        Test if get_number returns 2 when odd_number=False is passed in
#        """
#        test_odd_number = False
#        expected_number = 2
#        returned_number = self._callFUT(test_odd_number)

#        self.assertEqual(expected_number, returned_number)
