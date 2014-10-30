#!/usr/bin/env python

# iterative
def bin_search(array, value):
    lo, hi = 0, len(array)

    while True:
        if lo == hi:
            return -1

        index = (lo + hi) // 2
        item = array[index]

        if value == item:
            return index
        if value > item:
            lo = index + 1
        else:
            hi = index

# recursive
def bin_search_r(array, value, lo, hi):
    if lo > hi:
        return -1

    index = (lo + hi) / 2
    item = array[index]

    if value == item:
        return index
    if value < item:
        return bin_search_r(array, value, lo, index-1)
    else:
        return bin_search_r(array, value, index+1, hi)
    return index

# main
def index(array, value, method='cycle'):
    # if sorted ( for small arays)
    if sorted(array) != array:
        if value in array:
            return array.index(value)
        return -1

    if method == 'cycle':
        return bin_search(array, value)
    elif method == 'recursive':
        return bin_search_r(array, value, 0, len(array))
    else:
        print "only 'cycle' or 'recursive' methods are available"

