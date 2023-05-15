#!/usr/bin/python3

import sys


def print_stats(file_size, status_codes):
    """Prints the statistics."""
    print("File size: {}".format(file_size))
    for key in sorted(status_codes):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    count = 0
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0,
                    "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        # read stdin line by line
        for line in sys.stdin:
            # increment line count
            count += 1
            # split line into list of strings
            split_line = line.split()
            # validation for correct format of line (2 <= elements <= 9)
            if len(split_line) >= 2 and len(split_line) <= 9:
                # check that the file size is a valid integer
                if split_line[-1].isdigit():
                    # add the file size to the total
                    file_size += int(split_line[-1])
                # check that the status code is valid
                if split_line[-2] in status_codes:
                    # increment the status code count
                    status_codes[split_line[-2]] += 1
            # print stats every 10 lines
            if count % 10 == 0:
                print_stats(file_size, status_codes)
        # print final stats at the end
        print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        # print final stats if keyboard interrupt
        print_stats(file_size, status_codes)
        raise
