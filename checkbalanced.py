"""Is the tree at this node balanced?

To make this a bit more readable, let's alias our class name:

    >>> N = BinaryNode

For a tree of 1 item:

    >>> tree1 = N(1)
    >>> tree1.is_balanced()
    True

For a tree of 2 items:

  1
 /
2

    >>> tree2 = N(1,
    ...           N(2))
    >>> tree2.is_balanced()
    True

Three:

  1
 / \
2   3

    >>> tree3 = N(1,
    ...           N(2), N(3))
    >>> tree3.is_balanced()
    True

Four:

     1
    / \
   2   4
  /
 3

    >>> tree4 = N(1,
    ...           N(2,
    ...             N(3)),
    ...           N(4))
    >>> tree4.is_balanced()
    True

Five:

     1
   /---\
  2     5
 / \
3   4

    >>> tree5 = N(1,
    ...           N(2,
    ...             N(3), N(4)),
    ...           N(5))
    >>> tree5.is_balanced()
    True

Imbalanced Four:

    1
   /
  2
 / \
3   4

    >>> tree4i = N(1,
    ...            N(2,
    ...              N(3), N(4)))
    >>> tree4i.is_balanced()
    False
"""


class UnbalancedTreeException(Exception):
    pass


class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_balanced(self):
        """Is the tree at this node balanced?"""

        # if calling balanced height doesn't throw an exception, the tree is balanced
        try:
            self.balanced_height()
        except UnbalancedTreeException:
            return False

        return True

    # this could also be changed to a static method
    def balanced_height(self):
        """Returns balanced height of the tree at this node."""

        # check the balanced height of the left branch and that of the right branch

        if self.left is None:
            left_height = 0
        else:
            left_height = 1 + self.left.balanced_height()

        if self.right is None:
            right_height = 0
        else:
            right_height = 1 + self.right.balanced_height()

        # if the difference in heights of the left and right branches are
        # greater than one, raise exception
        if abs(left_height - right_height) > 1:
            raise UnbalancedTreeException

        # the balanced height is the max height of the left and right branches
        height = max(left_height, right_height)

        return height


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED! GO GO GO!\n"
