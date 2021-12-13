#!/usr/bin/env python3

with open('input.txt') as f:
    data = [int(line) for line in f]

part1 = lambda arr : len(list(filter(lambda x : x[1]> x[0],zip(arr, arr[1:]))))
print('Part One : %d' % part1(data))

part2 = list(map(lambda x : sum(x),zip(data, data[1:], data[2:])))
print('Part Two : %d' % part1(part2))
