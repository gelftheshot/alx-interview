#!/usr/bin/python3
""" a python script to handle log """
import sys

total = 0
stat_dic = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}

i = 0
try:
    for line in sys.stdin:
        line = line.strip()
        line_arr = line.split()
        total += int(line_arr[-1])
        stat_dic[line_arr[-2]] += 1
        i += 1
        if i == 10:
            print(f'File size: {total}')
            for key, value in stat_dic.items():
                if value != 0:
                    print(f'{int(key)}: {value}')
            i = 0
except KeyboardInterrupt:
    print(f'File size: {total}')
    for key, value in stat_dic.items():
        if value != 0:
            print(key, ' : ', value)
    raise
