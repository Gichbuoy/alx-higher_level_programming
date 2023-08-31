#!/usr/bin/python3
"""function that finds a peak ina list of unsorted int"""


def find_peak(list_of_integers):
    """define fxn that lists integers."""
    if list_of_integers == []:
        return None

    x = len(list_of_integers)
    if x == 1:
        return list_of_integers[0]
    elif x == 2:
        return max(list_of_integers)

    fnd = int(x / 2)
    peak = list_of_integers[fnd]
    if peak > list_of_integers[fnd - 1] and peak > list_of_integers[fnd + 1]:
        return peak
    elif peak < list_of_integers[fnd - 1]:
        return find_peak(list_of_integers[:fnd])
    else:
        return find_peak(list_of_integers[fnd + 1:])
