"""Given int, print each digit in reverse order, starting with the ones place.

For example::

    >>> print_digits(1)
    1

    >>> print_digits(413)
    3
    1
    4

    >>> print_digits(7331)
    1
    3
    3
    7

"""


def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""

    while not num % 10 == num:

        digit = num % 10
        print digit
        num = num / 10

    print num


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WOWZA!\n"
