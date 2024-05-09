#!/usr/bin/python3
"""Determines a valid UTF-8 encoding"""


def validUTF8(data):
    """
    B1 checks if significant byte is 1
    B2 checks if second significant byte is 0
    nbytes keeps track of how many 1s before 0 occurs
    data represented by a list of integers to check
    """

    B1 = 1 << 7
    B2 = 1 << 6
    nbytes = 0

    if not data or len(data) == 0:
        return True

    for num in data:
        bit = 1 << 7
        if nbytes == 0:
            while (bit & num):
                nbytes += 1
                bit = bit >> 1

            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:

            if not (num & B1 and not (num & B2)):
                return False
        nbytes -= 1

    if nbytes:
        return False
    else:
        return True
