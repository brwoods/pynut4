"""
>>> a, o = 100, 101
>>> ª, º = 200, 201

# not "100 101 200 201"
>>> print(a, o, ª, º)
200 201 200 201
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
