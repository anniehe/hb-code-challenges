"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""

    # Convert string to list of tokens with operators and numbers
    # For example: "+ 1 2" -> ["+", "1", "2"]
    tokens = s.split()

    # Start with the right-most number
    num2 = int(tokens.pop())

    while tokens:
        # Grab the right-most number
        num1 = int(tokens.pop())

        # Grab the right-most operator
        operator = tokens.pop()

        # Do math using the result as the right-hand value (num2) for next time

        if operator == "+":
            num2 = num1 + num2

        elif operator == "-":
            num2 = num1 - num2

        elif operator == "*":
            num2 = num1 * num2

        elif operator == "/":
            num2 = num1 / num2

    # When token list is empty, num2 is the result of last operation

    return num2


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n"
