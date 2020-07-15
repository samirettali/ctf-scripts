#!/usr/bin/env python3
import os
import csv
import pprint
from collections import Counter

# This script reads a bunch of .csv files and finds anomalies regarding
# Benford's law. Used to solve Benford's law firm challenge from DawgCTF 2020.

expected = {
    1: 30.1,
    2: 17.6,
    3: 12.5,
    4: 9.7,
    5: 7.9,
    6: 6.7,
    7: 5.8,
    8: 5.1,
    9: 4.6
}

total_differences = {}
for filename in os.listdir('.'):
    if filename.endswith('.csv'):
        with open(filename) as csvfile:
            numbers = ''
            reader = csv.reader(csvfile, delimiter=',')
            for section in reader:
                total = 0
                while row := next(reader):
                    cost = row[1][1:]
                    first_number = cost[0]
                    numbers += first_number
            occurrences = Counter(numbers)
            frequencies = {}
            differences = {}
            differences_sum = 0
            for n in occurrences:
                frequencies[int(n)] = float(occurrences[n] / len(numbers) * 100)
                differences[int(n)] = abs(frequencies[int(n)] - expected[int(n)])
                differences_sum += abs(frequencies[int(n)] - expected[int(n)])
            total_differences[filename] = differences_sum
print(sorted(total_differences.items(), key=lambda d:(d[1], d[0]), reverse=True))
