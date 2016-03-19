"""Given a list of numbers 1...max_num, find which one is missing in a list.

For example:

    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8

    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8
"""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list
    """

    # # SOLUTION 1 - O(n) runtime, O(n) runspace
    # # Keep track of seen numbers

    # seen = [False] * max_num

    # # Change to True for each number that's found in nums
    # for n in nums:
    #     seen[n - 1] = True

    # # The False value is the missing number
    # return seen.index(False) + 1


    # # SOLUTION 2 - O(n log n) runtime, O(1) runspace
    # # Sort and scan for missing number

    # nums.append(max_num + 1)
    # nums.sort()
    # last = 0

    # for num in nums:
    #     if num != last + 1:
    #         return last + 1
    #     last += 1

    # raise Exception("None are missing!")


    # SOLUTION 3 - O(n) runtime, O(1) runspace

    # Compare expected and actual sum to find missing number

    expected = sum(range(max_num + 1))

    return expected - sum(nums)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"
