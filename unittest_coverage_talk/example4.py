# -*- coding: utf-8 -*-

def peep_hole(username):
    """
    A list of special characters is defined and the username cannot have
    any special characters defined. If it does return False otherwise return
    True.
    """
    special_chars = ('@', '#', '$', '%', '^', '&', '*', '(', ')')
    for char in special_chars:
        if char in username:
            return False
        else: 
            continue
    return True
