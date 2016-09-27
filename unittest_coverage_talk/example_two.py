# -*- coding: utf-8 -*-

class ExampleTwo(object):
    """
    Branch Coverage Example
    """

    def __init__(self):
        pass

    def is_in_list(self, word):
        """
        Check if the word is in the list.
        """
        word_list = ['hello', 'world', 'foo', 'bar']

        if word in word_list:
            return True

        return False
