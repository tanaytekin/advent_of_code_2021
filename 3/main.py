#!/usr/bin/env python3

from statistics import mode

with open('input.txt') as f:
    data = [line for line in f]

width = len(data[0]) - 1
height = len(data)

gamma_str, epsilon_str = "", ""


for i in range(width):
    md = mode(map(lambda x : int(x[i]), data))
    gamma_str += str(md) 
    epsilon_str += '1' if md == 0 else '0'

gamma = int(gamma_str, 2)
epsilon = int(epsilon_str, 2)

print('Part One : %d' % (gamma * epsilon))


def part2(oxygen):
    arr = data
    for i in range(width):
        if len(arr) == 1:
            return int(arr[0], 2)
        ones = len([int(j[i]) for j in arr if int(j[i]) == 1 ])
        zeros = len([int(j[i]) for j in arr if int(j[i]) == 0 ])
        if ones >= zeros:
            md = 1 if oxygen else 0
        else:
            md = 0 if oxygen else 1
        arr = list(filter(lambda x : int(x[i]) == md, arr))
    return int(arr[0], 2)


(oxygen, co2) = (part2(True), part2(False))

print('Part Two : %d' % (oxygen * co2))
