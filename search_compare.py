#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 4 by Diandra Vega"""


import random
from timeit import default_timer as timer


def list_generator(num):
    """Docstring for list generator"""
    a_list = random.sample(xrange(1, 50000), num)
    return a_list


def sequential_search(a_list, item):
    """Docstring 1"""
    start = timer()

    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end = timer()

    return found, start, end


def ordered_sequential_search(a_list, item):
    """Docstring 2"""
    start = timer()

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

    end = timer()

    return found, start, end


def binary_search_iterative(a_list, item):
    """Docstring 3"""
    start = timer()

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

    end = timer()

    return found, start, end


def binary_search_recursive(a_list, item):
    """Docstring 4"""
    start = timer()

    if len(a_list) == 0:
        end = timer()
        return False, start, end
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        end = timer()
        return True, start, end
    else:
        if item < a_list[midpoint]:
            end = timer()
            return list(binary_search_iterative(a_list[:midpoint],
                                                item)), start, end
        else:
            end = timer()
            return list(binary_search_iterative(a_list[midpoint + 1:],
                                           item)), start, end


def main(num):
    """Search benchmarking docstring"""
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
        """Docstrinnnng"""
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

    seq_srch = "Sequential Search took {0:4.5f} seconds to run, on average".format(
        get_bench_avg(seq_srch_runtime))
    ord_seq_srch = "Ordered Sequential Search took {0:4.5f} seconds to run, on " \
                   "average".format(get_bench_avg(ord_seq_srch_runtime))
    bin_srch_iter = "Binary Search Iterative took {0:4.5f} seconds to run, on " \
                   "average".format(get_bench_avg(bin_srch_iter_runtime))
    bin_srch_recur = "Binary Search Recursive took {0:4.5f} seconds to run, on " \
                   "average".format(get_bench_avg(bin_srch_recur_runtime))

    return seq_srch, ord_seq_srch, bin_srch_iter, bin_srch_recur


print main(500)
print main(1000)
print main(10000)