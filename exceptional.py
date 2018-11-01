'''
A module for demonstrationg exceptions.
'''

import sys

def convert(s):
    '''Convert to an integer.'''
    try:
        return int(s)
    except (ValueError, TypeError) as ex:
        print('Conversion error: {}' \
            .format(str(ex)),
            file=sys.stderr)
        return -1