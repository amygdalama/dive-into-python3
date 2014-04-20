import re
from functools import reduce

ROMANS = ('M', 'D', 'C', 'L', 'X', 'V', 'I')
VALUES = (1000, 500, 100, 50, 10, 5, 1)


def valid_roman_numeral(s):
    """Checks to see if the string s is a valid Roman numeral.

    Keyword arguments:
    s -- string of characters

    Returns: Match object if s is a valid Roman numeral and None otherwise
    """
    
    s = s.upper()
    thousands = r'(M{,3})'
    hundreds = r'(D?C{,3}|CD|CM)'
    tens = r'(L?X{,3}|XL|XC)'
    ones = r'(V?I{,3}|IV|IX)'
    pattern = r'^' + thousands + hundreds + tens + ones + r'$'

    return re.search(pattern, s)


if __name__ == '__main__':

    print(valid_roman_numeral('I'))