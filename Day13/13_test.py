# Test Part 1

# def yield_next_multiple(input_number):
#     output_number = 0
#     while True:
#         yield output_number
#         output_number += input_number
#
#
# sequence = yield_next_multiple(5)
# for i in range(5):
#     print(next(sequence))

# Test Part 2

# main_sequence = range(10000000000000000)
# main_seed_list = [1789,37,47,1889]
#
# def yield_iterator(seed, sequence, offset):
#     for i in sequence:
#         if (i + offset) % seed == 0:
#             yield i
#
#
# def yield_looper(seed_list, sequence):
#     next_seq = sequence
#     offset = 0
#     for seed in seed_list:
#         if seed != 0:
#             next_seq = yield_iterator(seed, next_seq, offset)
#         offset += 1
#     return next_seq
#
#
# seed_iterator = yield_looper(main_seed_list, main_sequence)
# print(next(seed_iterator))


# Test Part 4 - Nope

# import math
#
# f = open("TestData2.txt", "r")
# raw_data = f.read()
#
# reqd_time, time_intervals = int(raw_data.split('\n')[0]), raw_data.split('\n')[1].split(',')
# essential_intervals = [int(i) for i in time_intervals if i != 'x']
#
# t_list = [int(i) if i != 'x' else int(0) for i in time_intervals]
# i_list = [i for i, v in enumerate(t_list) if v != 0]
# t_list[:] = [i for i in t_list if i != 0]
#
# print(f"{t_list}\n{i_list}")
#
# t_1 = sum(int(math.prod(t_list) / i) for i in t_list)
# t_2 = sum(i_list[i] * int(math.prod(t_list) / v) for i, v in enumerate(t_list))
# t_prod = math.prod(t_list)
#
# print(f"T1:\t{t_1}\n"
#       f"T2:\t{t_2}\n"
#       f"T_PROD:\t{t_prod}\n")
#
#
# def calculate_if_integer(num):
#     y = ((num * t_1) + t_2) / t_prod
#     if y.is_integer():
#         return num
#     else:
#         return False
#
#
# def get_multiples(num):
#     inp = num
#     while True:
#         yield inp
#         inp += num
#
#
# get_multiple = get_multiples(1)
# while True:
#     next_multiple = next(get_multiple)
#     if calculate_if_integer(next_multiple):
#         print(next_multiple)
#         break

# Method 5

from functools import reduce

f = open("TestData2.txt", "r")
raw_data = f.read()

reqd_time, time_intervals = int(raw_data.split('\n')[0]), raw_data.split('\n')[1].split(',')
essential_intervals = [int(i) for i in time_intervals if i != 'x']

t_list = [int(i) if i != 'x' else int(0) for i in time_intervals]
i_list = [i for i, v in enumerate(t_list) if v != 0]
t_list[:] = [i for i in t_list if i != 0]


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1



t_i_list = []

for i in range(len(t_list)):
    t_i_list.append(t_list[i] - i_list[i])

print(chinese_remainder(t_list, t_i_list))
