#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 4 by Diandra Vega"""


import random
import time
import pprint


PPRINT = pprint.PrettyPrinter(indent=4)


def list_generator(num):
    """This function will generate a list of random numbers using xrange().
    The maximum range is argument passed plus one. The size of the list
    will be equivalent to integer passed as argument.

    ARGS:
        num (int): Integer determining how large list should be.

    RETURNS:
        list: Returns a list of random numbers.

    EXAMPLES:
        >>> list_generator(10)
        [4, 2, 6, 7, 1, 9, 3, 10, 5, 8]
    """
    a_list = random.sample(xrange(1, num + 1), num)
    return a_list


def sequential_search(a_list, item):
    """Performs a sequential search on a list.

    ARGS:
        a_list (list): List that function will search through.
        item (int): Integer to search in list for.

    RETURNS:
        bool: Returns True or False value if item is found.
        float: Returns two float values of start time and end time of function.

    EXAMPLES:
        >>> sequential_search(list_generator(100), 5)
        (True, 1551225259.068, 1551225259.068)
    """
    start = time.time()

    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end = time.time()

    return found, start, end


def ordered_sequential_search(a_list, item):
    """Performs an ordered sequential search on a list.

    ARGS:
        a_list (list): List that function will search through.
        item (int): Integer to search in list for.

    RETURNS:
        bool: Returns True or False value if item is found.
        float: Returns two float values of start time and end time of function.

    EXAMPLES:
        >>> ordered_sequential_search(list_generator(100), 5)
        (False, 1551225403.493, 1551225403.493)
    """
    start = time.time()

    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end = time.time()

    return found, start, end


def binary_search_iterative(a_list, item):
    """Performs a binary search iteratively on a list.

    ARGS:
        a_list (list): List that function will search through.
        item (int): Integer to search in list for.

    RETURNS:
        bool: Returns True or False value if item is found.
        float: Returns two float values of start time and end time of function.

    EXAMPLES:
        >>> binary_search_iterative(list_generator(100), 5)
        (False, 1551225481.882, 1551225481.882)
    """
    start = time.time()

    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()

    return found, start, end


def binary_search_recursive(a_list, item):
    """Performs a binary search iteratively on a list.

    ARGS:
        a_list (list): List that function will search through.
        item (int): Integer to search in list for.

    RETURNS:
        list: Returns a list of a binary search iterative output on same list.
        float: Returns two float values of start time and end time of function.

    EXAMPLES:
        >>> binary_search_recursive(list_generator(100), 5)
        ([False, 1551225535.227, 1551225535.227], 1551225535.227,
        1551225535.227)
    """
    start = time.time()

    if len(a_list) == 0:
        end = time.time()
        return False, start, end
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        end = time.time()
        return True, start, end
    else:
        if item < a_list[midpoint]:
            end = time.time()
            return list(binary_search_iterative(a_list[:midpoint],
                                                item)), start, end
        else:
            end = time.time()
            return list(binary_search_iterative(a_list[midpoint + 1:],
                                                item)), start, end


def main(num):
    """Main function of the program calculates the average times it takes
    for all search functions in this program to complete from start to finish.

    ARGS:
        num (int): Number of lists you want generated that search functions
            will run searches on.

    RETURNS:
        tuple: Returns a tuple of strings stating average time each search
            took to complete.

    EXAMPLES:
        >>> import pprint
        >>> pprint.pprint(main(500))
        ('Sequential Search took 1551225619.7350492 seconds to run, on average',
         'Ordered Sequential Search took 1551225619.7350492 seconds to run, on average',
         'Binary Search Iterative took 1551225619.7350492 seconds to run, on average',
         'Binary Search Recursive took 1551225619.7350492 seconds to run, on average')
    """
    seq_srch_runtime = []
    ord_seq_srch_runtime = []
    bin_srch_iter_runtime = []
    bin_srch_recur_runtime = []


    for _ in range(100):
        a_list = list_generator(num)
        a_list.sort()

        # Sequential Search Benchmark #
        seq_srch_runtime.append(list(sequential_search(a_list, -1)))
        # Ordered Sequential Search Benchmark #
        ord_seq_srch_runtime.append(list(ordered_sequential_search(a_list, -1)))
        # Binary Search Iterative Benchmark #
        bin_srch_iter_runtime.append(list(binary_search_iterative(a_list, -1)))
        # Binary Search Recursive Benchmark #
        bin_srch_recur_runtime.append(list(binary_search_recursive(a_list, -1)))


    ## Remove bool values from lists and get average ##
    def get_bench_avg(bench):
        """Calculates the average time it takes a search to run by
        calculating sum of start and end times in each list searched
        divided by two. The averages are then stored in a list where the
        total average is later calculated by taking the sum of each list
        divided by 100.

        ARGS:
            bench (list): Provide a list of start and end times from
                100 lists searched in main function.

        RETURNS:
            float: Returns a floating int for average seconds it took in epoch time
                to complete a search on 100 lists.

        EXAMPLES:
            >>> get_bench_avg(seq_srch_runtime)
            1551226307.4
        """
        avg_times = []

        if bench == bin_srch_recur_runtime:
            for val in bench:
                avg = sum(val[1:]) / 2
                avg_times.append(avg)
            total_avg = sum(avg_times) / 100
        else:
            for val in bench:
                if False in val:
                    val.remove(False)
                elif True in val:
                    val.remove(True)
                avg = sum(val) / 2
                avg_times.append(avg)

            total_avg = sum(avg_times) / 100
        return total_avg

    seq_srch = "Sequential Search took {} seconds to run, on average".format(
        "%10.7f" % get_bench_avg(seq_srch_runtime))
    ord_seq_srch = "Ordered Sequential Search took {} seconds to run, on " \
                   "average".format("%10.7f" % get_bench_avg(ord_seq_srch_runtime))
    bin_srch_iter = "Binary Search Iterative took {} seconds to run, on " \
                   "average".format("%10.7f" % get_bench_avg(bin_srch_iter_runtime))
    bin_srch_recur = "Binary Search Recursive took {} seconds to run, on " \
                   "average".format("%10.7f" % get_bench_avg(bin_srch_recur_runtime))

    return seq_srch, ord_seq_srch, bin_srch_iter, bin_srch_recur


PPRINT.pprint(main(500))
PPRINT.pprint(main(1000))
PPRINT.pprint(main(10000))
