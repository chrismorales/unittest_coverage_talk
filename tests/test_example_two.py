import unittest


class TestExampleTwo(unittest.TestCase):
    """
    All test cases for the methods defined within the ExampleTwo class.
    """

    def _makeOne(self):
        """ Import the class and return an instance. """
        from unittest_coverage_talk.talk.example_two import ExampleTwo
        return ExampleTwo()

    def _callFUT(self, word):
        """ Creates an instance and calls the function under test. """
        instance = self._makeOne()
        return instance.is_in_list(word)

    def test_word_is_in_list(self):
        """
        Given a word in the list we expect the function to return True.
        """
        test_word = 'hello'
        expected_boolean = True
        returned_boolean = self._callFUT(test_word)

        self.assertEqual(expected_boolean, returned_boolean)

    def test_word_is_not_in_list(self):
        """
        Given a word in the list we expect the function to return True.
        """
        test_word = 'buzzwords'
        expected_boolean = False
        returned_boolean = self._callFUT(test_word)

        self.assertEqual(expected_boolean, returned_boolean)
