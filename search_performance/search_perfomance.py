"""
    CS051P Lab Assignments: Search Performance

    Author: Dylan O'Connor

    Date: November 2, 2022

    The goal of this assignment is to implement a few basic search
    algorithms and measure their performance.  As such, it is also
    an introduction to algorithmic complexity.
"""
import random
import time
import csv


def list_of_integers(size):
    """
    Creates a random list of integers that range from 1 to size * 2 and fit in a list of size
    :param size: (int) the length of the list and half the size of the largest possible integer
    :return: (list) a newly created random list
    """
    # initializes a new list
    new_list = []

    # for every number in size, append a number between 1 and size * 2 to new list
    for num in range(size):
        new_list.append(random.randrange(1, size * 2))

    # return the new list
    return new_list


def linear_search(alist, value):
    """
    Goes through a list of elements first to last and searches for a value, returns the value if found
    :param alist: (list) a list of integers
    :param value: (int) a value
    :return: (int) the value or -1 if not found
    """
    # for loop goes through every element in alist
    for i in range(len(alist)):

        # returns i if value found
        if alist[i] == value:
            return i

    # returns -1 if not found
    return -1


def binary_search_helper(alist, value, start, end):
    """
    Takes a sorted list and divides it until it finds a value or doesn't
    :param alist: (list) a list of sorted integers
    :param value: (int) a value
    :param start: (int) the start place of list
    :param end: (int) the end place of the list
    :return: (int) the index of the value
    """
    # calculates midpoint location of list portion to the right or to the left
    n = (end - start) // 2 + start

    # base case, if value found, return value index, if value not found, return -1
    if alist[n] == value:
        return n
    elif end - start == 1:
        return -1

    # recursive case, if value smaller than indexed value, move to left
    elif alist[n] > value:
        return binary_search_helper(alist, value, start, n)

    # recursive case, if value larger than indexed value, move to right
    elif alist[n] < value:
        return binary_search_helper(alist, value, n, end)


def binary_search(alist, value):
    """
    Calls binary_search_helper to find a value in a sorted list
    :param alist: (list) a list of sorted integers
    :param value: (int) a value
    :return: (int) the index of the found value or -1
    """
    # calls helper function
    return binary_search_helper(alist, value, 0, len(alist))


def main_part1():
    """
    Tests linear_search and binary_search with found and not found values
    """
    # establishes a random list with 12 integers
    new_list = list_of_integers(12)
    print(new_list)

    # tests linear search with numbers in and out of range of random list
    print(linear_search(new_list, 4))
    print(linear_search(new_list, 9))
    print(linear_search(new_list, 27))
    print(linear_search(new_list, 400))

    # sorts list
    list.sort(new_list)
    print(new_list)

    # test binary search with numbers in and out of range of random list
    print(binary_search(new_list, 2))
    print(binary_search(new_list, 10))
    print(binary_search(new_list, 23))
    print(binary_search(new_list, 301))


def sorted_comparison(min_size, max_size):
    """
    Compares the speed of binary search and linear search when lists being used are pre-sorted
    :param min_size: (int) the minimum size of the list to be tested
    :param max_size: (int) the maximum size of hte list to be tested
    :return: (list) a list of lists for each test run of binary search and linear search
    """
    # initializes final list
    final_list = []

    # while loop that ends when max list size is reached
    while min_size <= max_size:

        # creates new list of random integers and sorts it
        new_list = list_of_integers(min_size)
        list.sort(new_list)

        # tests speed of linear search
        start = time.time()
        linear_search(new_list, 100)
        end = time.time()
        elapsed_time_in_seconds1 = end-start

        # tests speed of binary search
        start = time.time()
        binary_search(new_list, 100)
        end = time.time()
        elapsed_time_in_seconds2 = end-start

        # appends times of both tests to temp list
        tuple = (min_size, elapsed_time_in_seconds1, elapsed_time_in_seconds2)

        # appends full test values to final list
        final_list.append(tuple)

        # increases size of list
        min_size = min_size * 2

    # when all tests have been run, return a list of all test cases
    return final_list


def unsorted_comparison(min_size, max_size):
    """
    Compares run speed of binary search and linear search when only binary search lists have been sorted
    :param min_size: (int) the smallest list to be tested
    :param max_size: (int) the largest list to be tested
    :return: (list) a list of lists of all the tests
    """
    # initializes the final list
    final_list = []

    # while loop that ends when final test has run
    while min_size <= max_size:

        # initializes a random list that is min_size length
        new_list = list_of_integers(min_size)

        # tests speed of linear search
        start = time.time()
        linear_search(new_list, 100)
        end = time.time()
        elapsed_time_in_seconds1 = end - start

        # tests speed of binary search and sorts list
        start = time.time()
        list.sort(new_list)
        binary_search(new_list, 100)
        end = time.time()
        elapsed_time_in_seconds2 = end - start

        # appends binary and linear test speeds as well as test number to temp list
        tuple = (min_size, elapsed_time_in_seconds1, elapsed_time_in_seconds2)

        # appends temp_list to the final list
        final_list.append(tuple)

        # doubles size of test list
        min_size = min_size * 2

    # when all tests have run, return a list of all tests and times
    return final_list


def main():
    """
    Runs unsorted test comparison and sorted test comparison, writing into two csv files the results
    """
    # initializes unsorted test comparison and sorted test comparison to run many times
    unsorted_test = unsorted_comparison(2, 1048576)
    sorted_test = sorted_comparison(2, 1048576)

    # opens sorted.csv file to place sorted test results in
    file1 = open('sorted.csv', 'w', newline="")
    writer = csv.writer(file1)
    for elem in range(len(sorted_test)):
        writer.writerow(sorted_test[elem])
    file1.close()

    # opens unsorted.csv file to place unsorted test results in
    file2 = open('unsorted.csv', 'w', newline="")
    writer = csv.writer(file2)
    for elem in range(len(unsorted_test)):
        writer.writerow(unsorted_test[elem])
    file2.close()


if __name__ == "__main__":
    main()
    # main_part1()
