"""Check if pattern matches.

Given a "pattern string" starting with "a" and including only "a" and "b"
characters, check to see if a provided string matches that pattern.

For example, the pattern "aaba" matches the string "foofoogofoo" but not
"foofoofoodog".

Patterns can only contain a and b and must start with a:

    >>> pattern_match("b", "foo")
    Traceback (most recent call last):
    ...
    AssertionError: invalid pattern

    >>> pattern_match("A", "foo")
    Traceback (most recent call last):
    ...
    AssertionError: invalid pattern

    >>> pattern_match("abc", "foo")
    Traceback (most recent call last):
    ...
    AssertionError: invalid pattern

The pattern can contain only a's:

    >>> pattern_match("a", "foo")
    True

    >>> pattern_match("aa", "foofoo")
    True

    >>> pattern_match("aa", "foobar")
    False

It's possible for a to be zero-length (a='', b='hi'):

    >>> pattern_match("abbab", "hihihi")
    True

Or b to be zero-length (a='foo', b=''):

    >>> pattern_match("aaba", "foofoofoo")
    True

Or even for a and b both to be zero-length (a='', b=''):

    >>> pattern_match("abab", "")
    True

But, more typically, both are non-zero length:

    >>> pattern_match("aa", "foodog")
    False

    >>> pattern_match("aaba" ,"foofoobarfoo")
    True

    >>> pattern_match("ababab", "foobarfoobarfoobar")
    True

Tricky: (a='foo', b='foobar'):

    >>> pattern_match("aba" ,"foofoobarfoo")
    True
"""


def matches(pattern, a, b, astring):
    """Does astring match pattern using proposed values for a and b?

        >>> matches("aaba", "foo", "bar", "foofoobarfoo")
        True

        >>> matches("aaba", "foo", "nope", "foofoobarfoo")
        False
    """

    test_string = ""

    for p in pattern:
        if p == "a":
            test_string += a
        else:
            test_string += b
        # Or using ternary operator
        # test_string += a if p == "a" else b

    return test_string == astring


def pattern_match(pattern, astring):
    """Can we make this pattern match this string?"""

    # Q&D sanity check on pattern

    assert (pattern.replace("a", "").replace("b", "") == ""
            and pattern.startswith("a")), "invalid pattern"

    a_count = pattern.count("a")    # number of times a appears in pattern
    b_count = pattern.count("b")    # number of times b appears in pattern
    first_b = pattern.find("b")     # index of first b (-1 if not in pattern)

    # Check every possible length of a, from 0 to the max
    # Max is determined by count of how many a's must appear

    astring_length = len(astring)
    max_length = astring_length / a_count

    for a_length in range(0, max_length + 1):

        # For this length of a, find required length of b
        if b_count:
            b_length = (astring_length - (a_length * a_count)) / float(b_count)
        else:
            b_length = 0

        # Fast fail optimization: b_length must be int and >= 0
        if int(b_length) != b_length or b_length < 0:
            continue

        # Find where b would need to begin
        b_start = first_b * a_length

        # Check if this is a match using matches() helper function
        if matches(pattern=pattern,
                   a=astring[0:a_length],
                   b=astring[b_start:b_start + int(b_length)],
                   astring=astring):
            return True

    return False


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WE'RE WELL-MATCHED!\n"
