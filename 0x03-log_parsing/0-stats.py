#!/usr/bin/python3
""" a python script to handle log """
import sys


if __name__ == "__main__":
    stat_dic = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    count = 1
    file_size = 0

    def Read_line(line):
        """ Read, parse and grab data"""
        try:
            parsed_line = line.split()
            status_code = parsed_line[-2]
            if status_code in stat_dic.keys():
                stat_dic[status_code] += 1
            return int(parsed_line[-1])
        except Exception:
            return 0

    def print_stats():
        """print stats in ascending order"""
        print("File size: {}".format(file_size))
        for key in sorted(stat_dic.keys()):
            if stat_dic[key]:
                print("{}: {}".format(key, stat_dic[key]))

    try:
        for line in sys.stdin:
            file_size += Read_line(line)
            if count % 10 == 0:
                print_stats()
            count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
