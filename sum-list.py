"""Return the sum of all numbers in list.

For example:

    >>> sum_list([5, 3, 6, 2, 1])
    17
"""


def sum_list(num_list):
    """Return the sum of all numbers in a list."""

    total = 0

    for num in num_list:
        total += num

    return total


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
