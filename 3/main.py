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

oxygen_arr = data
for i in range(width):
    ones = len([int(j[i]) for j in oxygen_arr if int(j[i]) == 1 ])
    zeros = len([int(j[i]) for j in oxygen_arr if int(j[i]) == 0 ])
    if ones >= zeros:
        md = 1
    else:
        md = 0
    oxygen_arr = list(filter(lambda x : int(x[i]) == md, oxygen_arr))
oxygen = int(oxygen_arr[0], 2)


co2_arr = data
for i in range(width):
    if len(co2_arr) == 1:
        break
    ones = len([int(j[i]) for j in co2_arr if int(j[i]) == 1 ])
    zeros = len([int(j[i]) for j in co2_arr if int(j[i]) == 0 ])
    if ones >= zeros:
        md = 0
    else:
        md = 1
    co2_arr = list(filter(lambda x : int(x[i]) == md, co2_arr))
co2 = int(co2_arr[0], 2)

print('Part Two : %d' % (oxygen * co2))
