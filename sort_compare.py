#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 4 by Diandra Vega"""


import time
import random
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


def insertion_sort(a_list):
    """Performs an insertion sort on a list.

    ARGS:
        a_list (list): List to be sorted.

    RETURNS:
        float: Returns two float values for start time of function and end
            time of function.

    EXAMPLES:
        >>> insertion_sort(list_generator(20))
        (1551226566.044, 1551226566.044)
    """
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    end = time.time()
    return start, end


def shell_sort(a_list):
    """Performs a shell sort on a list.

    ARGS:
        a_list (list): List to be sorted.

    RETURNS:
        float: Returns two float values for start time of function and end
            time of function.

    EXAMPLES:
        >>> shell_sort(list_generator(20))
        (1551226566.044, 1551226566.044)
    """
    start = time.time()
    sublist_count = len(a_list) // 2

    def gap_insertion_sort(a_list, start, gap):
        """Performs a gap insertion sort within shell sort function."""
        for i in range(start + gap, len(a_list), gap):
            current_value = a_list[i]
            position = i

            while position >= gap and a_list[position - gap] > current_value:
                a_list[position] = a_list[position - gap]
                position = position - gap

            a_list[position] = current_value

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2
    end = time.time()

    return start, end


def python_sort(a_list):
    """Wrapper function on python sort for a list.

    ARGS:
        a_list (list): List to be sorted.

    RETURNS:
        float: Returns two float values for start time of function and end
            time of function.

    EXAMPLES:
        >>> python_sort(list_generator(20))
        (1551226566.044, 1551226566.044)
    """
    start = time.time()
    a_list.sort()
    end = time.time()
    return start, end


def main(num):
    """Calculates average times it takes to sort on a list with insertion
    sort, shell sort, and regular python sort.

    ARGS:
        num (int): Length of list to be generated for benchmarking.

    RETURNS:
        tuple: Returns tuple of strings specifying the average time it took
            for each sort function to complete.

    EXAMPLES:
        >>> import pprint
        >>> pprint.pprint(main(500))
        ('Insertion Sort took 1551226563.2550001 seconds to run, on average',
        'Shell Sort took 1551226563.2550001 seconds to run, on average',
        'Python Sort took 1551226563.2550001 seconds to run, on average')
    """
    a_list = list_generator(num)

    def get_bench_avg(benchmark):
        """Docstring"""
        avg_times = sum(benchmark) / 2
        return avg_times

    ins_sort_rt = "Insertion Sort took {} seconds to run, on average".format(
        "%10.7f" % get_bench_avg(list(insertion_sort(a_list))))
    shell_sort_rt = "Shell Sort took {} seconds to run, on average".format(
        "%10.7f" % get_bench_avg(list(shell_sort(a_list))))
    python_sort_rt = "Python Sort took {} seconds to run, on average".format(
        "%10.7f" % get_bench_avg(list(python_sort(a_list))))

    return ins_sort_rt, shell_sort_rt, python_sort_rt

PPRINT.pprint(main(500))
PPRINT.pprint(main(1000))
PPRINT.pprint(main(10000))
