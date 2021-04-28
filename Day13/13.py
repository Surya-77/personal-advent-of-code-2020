# Main program
from functools import reduce

f = open("InputData.txt", "r")
raw_data = f.read()

reqd_time, time_intervals = int(raw_data.split('\n')[0]), raw_data.split('\n')[1].split(',')
essential_intervals = [int(i) for i in time_intervals if i != 'x']
all_intervals = [int(i) if i != 'x' else int(0) for i in time_intervals]


def get_next_time_interval(inp_interval):
    output_number = 0
    while True:
        yield output_number
        output_number += inp_interval


def get_earliest_departing_bus(my_time, bus_intervals):
    best_interval = 0
    best_time = max(bus_intervals)
    for interval in bus_intervals:
        next_time = ((my_time // interval) + 1) * interval
        wait_time = next_time - my_time
        if best_time >= wait_time:
            best_time = wait_time
            best_interval = interval
    return best_time, best_interval


def yield_iterator(seed, sequence, offset):
    for i in sequence:
        if (i + offset) % seed == 0:
            yield i


def yield_looper(seed_list, sequence):
    next_seq = sequence
    offset = 0
    for seed in seed_list:
        if seed != 0:
            next_seq = yield_iterator(seed, next_seq, offset)
        offset += 1
    return next_seq


part_1_time, part_1_interval = get_earliest_departing_bus(reqd_time, essential_intervals)
print(f"Wait time:\t\t{part_1_time}\n"
      f"Bus to wait:\t{part_1_interval}\n"
      f"Part 1 Answer:\t{part_1_time * part_1_interval}")

t_list = [int(i) if i != 'x' else int(0) for i in time_intervals]
i_list = [i for i, v in enumerate(t_list) if v != 0]
t_list[:] = [i for i in t_list if i != 0]
t_i_list = []
for i in range(len(t_list)):
    t_i_list.append(t_list[i] - i_list[i])


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


part_2_answer = chinese_remainder(t_list, t_i_list)
print(f"Part 2 Answeer:\t{part_2_answer}\n")
