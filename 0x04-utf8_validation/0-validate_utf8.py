#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """ tracking the number of consecutive 1s in the most significant bit"""
    num_bytes = 0

    for byte in data:
        """ Check if the most significant bit is 0 for a single-byte character"""
        if num_bytes == 0:
            if (byte >> 7) == 0:
                continue
             # Checking for consecutive 1s in the most significant bit
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
             #Check if the byte is a continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    """Check if there are any incomplete multi-byte characters"""
    return num_bytes == 0
