"""
    Test cases for Search Performance lab

    This starter includes a set of basic sanity checks for the
    assigned functions in part 1 and part 2 of this lab.  The
    provided tests cases check returned types and values for
    the simplest cases.

    Extend these test cases (especially linear_search_tester
    and binary_search_tester) to better exercise the interesting
    situations for those searches.  You will be graded on the
    completeness of the added test cases.
"""
from search_performance import *


def list_builder_tester():
    """
    Run a series of tests for the list builder
    :return (boolean): were all tests successful
    """
    # value we expect to see
    list_size = 64
    min_value = 1
    max_value = 2 * list_size

    result = list_of_integers(list_size)

    # confirm the size of the list
    assert(len(result) == list_size)

    # validate the contents
    for value in result:

        # check the type
        assert(type(value) == int)

        # check vs max/minimum value
        assert(value >= min_value)
        assert(value <= max_value)

    # test larger list
    list_size = 100
    max_value = list_size * 2

    result = list_of_integers(list_size)

    # confirm the size of the list
    assert(len(result) == list_size)

    # validate the contents
    for value in result:

        # check the type
        assert(type(value) == int)

        # check vs max/minimum value
        assert(value >= min_value)
        assert(value <= max_value)

        # check for value not in list
        assert(value != list_size * 2 + 1)

    return True


def linear_search_tester():
    """
    Run a series of tests for linear_search
    :return (boolean): were all tests successful
    """

    unsorted_list = [8, 2, 6, 4]

    # find a number in the middle of the list
    result = linear_search(unsorted_list, 2)
    assert(type(result == int))
    assert(result == 1)

    # find a number that is not in the list
    result = linear_search(unsorted_list, 5)
    assert(type(result == int))
    assert(result == -1)

    # testing larger list with more diverse numbers
    unsorted_list = [1, 3, 10, 2, 9, 102, 1, 10, 4]

    # find a number far left
    result = linear_search(unsorted_list, 3)
    assert (result == 1)

    # find a number far right
    result = linear_search(unsorted_list, 4)
    assert (result == 8)

    return True


def binary_search_tester():
    """
    Run a series of tests for binary_search
    :return (boolean): were all tests successful
    """
    sorted_list = [2, 4, 6, 8]

    # find a number in the middle of the list
    result = binary_search(sorted_list, 4)
    assert(type(result == int))
    assert(result == 1)

    # find a number that is not in the list
    result = binary_search(sorted_list, 5)
    assert(type(result == int))
    assert(result == -1)

    # test larger list with more diverse integers
    sorted_list = [1, 3, 10, 12, 190, 1304, 13000]

    # find a number that is first
    result = binary_search(sorted_list, 1)
    assert(result == 0)

    # find a number that is far left
    result = binary_search(sorted_list, 3)
    assert (result == 1)

    # find a number that is far right
    result = binary_search(sorted_list, 1304)
    assert(result == 5)

    # find a number at the very end of the list
    result = binary_search(sorted_list, 13000)
    assert(result == 6)

    return True


def sorted_search_tester():
    """
    Run a series of tests for sorted searches
    :return (boolean): were all tests successful
    """
    result = sorted_comparison(2, 8)

    # confirm the number of tupples
    assert(len(result) == 3)

    # confirm count and types of values in each tupple
    size = 2
    for index in range(3):
        (count, linear, binary) = result[index]
        assert(type(count) == int)
        assert(type(linear) == float)
        assert(type(binary) == float)
        assert(count == size)
        size *= 2

    return True


def unsorted_search_tester():
    """
    Run a series of tests for sorted searches
    :return (boolean): were all tests successful
    """
    result = unsorted_comparison(2, 8)

    # confirm the number of tupples
    assert(len(result) == 3)

    # confirm count and types of values in each tupple
    size = 2
    for index in range(3):
        (count, linear, binary) = result[index]
        assert(type(count) == int)
        assert(type(linear) == float)
        assert(type(binary) == float)
        assert(count == size)
        size *= 2

    return True


def main():
    """
    exercise the assigned methods
    """
    print("testing linear search ... " +
          "PASS" if linear_search_tester() else "FAIL")

    print("")
    print("testing binary search ... " +
          "PASS" if binary_search_tester() else "FAIL")

    print("")
    print("testing list of integers ... " +
          "PASS" if list_builder_tester() else "FAIL")

    print("")
    print("testing sorted_comparison ... " +
          "PASS" if sorted_search_tester() else "FAIL")

    print("")
    print("testing unsorted_comparison ... " +
          "PASS" if unsorted_search_tester() else "FAIL")


if __name__ == "__main__":
    main()
