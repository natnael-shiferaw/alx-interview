#!/usr/bin/python3
"""
Module: log_parsing

This module provides functionality to parse logs from standard
input and print statistics.

Functions:
    print_stats(stats, file_size):
        Print the accumulated statistics and file size.

"""

import sys

if __name__ == '__main__':
    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """
        Print the accumulated statistics and file size.

        Args:
            stats (dict): A dictionary of status codes and their counts.
            file_size (int): The total file size.
        """
        print("File size: {:d}".format(file_size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            
            # Update status code count if present in the data
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except IndexError:
                pass
            
            # Update file size if present in the data
            try:
                filesize += int(data[-1])
            except (IndexError, ValueError):
                pass
            
            # Print statistics every 10 lines
            if count % 10 == 0:
                print_stats(stats, filesize)
        
        # Print final statistics after processing all lines
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        # Print statistics if the program is interrupted
        print_stats(stats, filesize)
        raise
