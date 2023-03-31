#!/usr/bin/python3
"""
Module to find the hightest number in an array
"""

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: A peak in the list.

    """
    n = len(list_of_integers)
    if n == 0:
        return None
    elif n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)

    for i in range(1, n - 1):
        if list_of_integers[i] >= list_of_integers[i-1] and list_of_integers[i] >= list_of_integers[i+1]:
            return list_of_integers[i]

    return max(list_of_integers[0], list_of_integers[n-1])

