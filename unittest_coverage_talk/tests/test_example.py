# -*- coding: utf-8 -*-

import unittest

class HelloWorldTest(unittest.TestCase):

    def _callFUT(self):
        '''Imports, calls the function under test and returns the output'''

        from unittest_coverage_talk.example import hello_world
        return hello_world()

    def test_example_one_returns_hello_world_string(self):
        '''
	Test that the string returned by hello_world method is equal to "Hello World"
        '''

        expected_return = "Hello World"
        returned_value = self._callFUT()

        self.assertEqual(expected_return, returned_value)
