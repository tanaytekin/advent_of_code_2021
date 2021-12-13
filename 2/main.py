#!/usr/bin/env python3

with open('input.txt') as f:
    data = [line.split() for line in f]

horizontal = sum([int(item[1]) for item in data if item[0]=='forward'])
depth = sum([int(item[1]) for item in data if item[0]=='down']) - sum([int(item[1]) for item in data if item[0]=='up']) 

print('Part One : %d' % (horizontal * depth))

depth, aim = 0, 0
for item in data:
    if item[0] == 'up':
        aim -= int(item[1])
    elif item[0] == 'down':
        aim += int(item[1])
    elif item[0] == 'forward':
        depth += aim * int(item[1])

print('Part Two : %d' % (horizontal * depth))
