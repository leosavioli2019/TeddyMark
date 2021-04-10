import sys

def systemClear():
    if 'win' in sys.platform:
        return 'cls'
    elif sys.platform == 'linux':
        return 'clear'
    elif sys.platform == 'darwin':
        return 'clear'

def directory():
    if 'win' in sys.platform:
        return '\\'
    elif sys.platform == 'linux':
        return '/'
    elif sys.platform == 'darwin':
        return '/'