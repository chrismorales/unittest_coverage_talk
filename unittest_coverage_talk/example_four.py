# -*- coding: utf-8 -*-

class ExampleFour(object):
    """
    Resolved Peephole Optimization
    Solution One.
    """

    def __init__(self):
        pass

    def contains_special_char(self, username):
        """
        A list of special characters is defined and the username cannot have
        any special characters defined. If it does return False otherwise return
        True.
        """
        special_chars = ('@', '#', '$', '%', '^', '&', '*', '(', ')')
        for char in special_chars:
            if char not in username:
                continue
            else:
                return False
        return True
