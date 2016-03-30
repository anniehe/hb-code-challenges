"""Calculate possible change from combinations of dimes and pennies.

Given an infinite supply of dimes and pennies, find the different
amounts of change can be created with exact `num_coins` coins?

For example, when num_coins = 3, you can create:

    3 = penny + penny + penny
   12 = dime + penny + penny
   21 = dime + dime + penny
   30 = dime + dime + dime

For example:

    >>> coins(0) == {0}
    True

    >>> coins(1) == {1, 10}
    True

    >>> coins(2) == {2, 11, 20}
    True

    >>> coins(3) == {3, 12, 21, 30}
    True

    >>> coins(4) == {4, 13, 22, 31, 40}
    True

    >>> coins(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
    True
"""


PENNY = 1
DIME = 10


def add_coins(num_coins, total, change):
    """Add combinations of coins to total.

    If used up available number of coins, return.

    Otherwise, recursively call until that condition.

        >>> change = set()
        >>> add_coins(num_coins=1, total=0, change=change)
        >>> change == {1, 10}
        True

    """

    # Base case:
    # All available coins used up,
    # so add total to change to keep track of this combo
    # and stop recursing
    if num_coins == 0:
        change.add(total)
        return

    # Two recursion paths possible:
    # one adding penny to total, another adding dime to total
    # Each time a coin is added, there is one less coin available so num_coins -= 1
    add_coins(num_coins - 1, total + PENNY, change)
    add_coins(num_coins - 1, total + DIME, change)


def coins(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    """

    change = set()

    add_coins(num_coins=num_coins, total=0, change=change)

    return change


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAN TAKE THAT TO THE BANK!\n"
