def is_rotated_string(str1, str2):
    '''
    Check if string2 is a rotated substring of string1.

    >>> is_rotated_string('waterbottle', 'erbottlewat')
    True

    >>> is_rotated_string('waters', 'watesr')
    False

    >>> is_rotated_string('waters', 'water')
    False

    is_rotated_string('', 'water')
    False
    '''

    if len(str1) > 0 and len(str2) and \
    len(str1) == len(str2) > 0:
        
        temp_string = str1 * 2

        if str2 in temp_string:
            return True
        else:
            return False

    return False


if __name__ == '__main__':
    import doctest


if doctest.testmod().failed == 0:
    print "\n*** ALL TESTS PASSED. GO YOU!\n"