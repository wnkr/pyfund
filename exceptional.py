'''
A module for demonstrationg exceptions.
'''

import sys
from math import log

def convert(s):
    '''Convert to an integer.'''
    try:
        return int(s)
    except (ValueError, TypeError) as ex:
        print('Conversion error: {}' \
            .format(str(ex)),
            file=sys.stderr)
        raise

def string_log(s):
    v = convert(s)
    return log(v)