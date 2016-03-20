"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def is_prime(num):
    """Is num a prime number?

    num will always be a positive integer.

    A prime number is an integer >= 2 that is only evenly divisible by itself and 1.

    >>> is_prime(0)
    False

    >>> is_prime(1)
    False

    >>> is_prime(2)
    True

    >>> is_prime(3)
    True

    >>> is_prime(4)
    False

    >>> is_prime(7)
    True

    >>> is_prime(25)
    False
    """

    assert num >= 0, "Num should be a positive integer."

    # Definition: 0 and 1 are not prime
    if num < 2:
        return False

    # Definition: 2 is prime
    if num == 2:
        return True

    # All even numbers are divisible by 2, so not prime
    if num % 2 == 0:
        return False

    # Now, only need to check odd numbers from 3 to sqrt(num)
    # that evenly divides num

    n = 3

    while n * n <= num:
        if num % n == 0:
            return False
        # Go to next odd number
        n += 2

    return True


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    primes = []
    num = 2

    while count > 0:
        if is_prime(num):
            primes.append(num)
            count -= 1

        num += 1

    return primes


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
