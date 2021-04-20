from pprint import pprint
from copy import deepcopy
import itertools

f = open("./InputData.txt", "r")
raw_data = f.read()
grid = [[j for j in i] for i in raw_data.split('\n')]


def proper_bound(g, r_i, c_i):
    if (0 <= r_i < len(g)):
        if (0 <= c_i < len(g[0])):
            return True
        else:
            return False
    else:
        return False


def adjacent_seat_layout(g, r_i, c_i):
    r_range = [-1, 0, 1]
    c_range = [-1, 0, 1]
    a_s_i = list(itertools.product(r_range, c_range))
    a_s_i.remove((0,0))
    a_s = []
    for elem in a_s_i:
        if proper_bound(g, r_i+elem[0], c_i+elem[1]):
            a_s.append(g[r_i+elem[0]][c_i+elem[1]])
    return a_s


def cardinal_seat_count(g, r_i, c_i):
    max_r = len(g)
    max_c = len(g[0])
    occupied_seat_count = 0
    unoccupied_seat_count = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            first_seen_flag = False
            max_size = max(max_r, max_c)
            for k in range(0, max_size):
                curr_r = r_i
                curr_c = c_i
                if i > 0:
                    curr_r += i + k
                elif i < 0:
                    curr_r += i - k
                else:
                    curr_r += i
                if j > 0:
                    curr_c += j + k
                elif j < 0:
                    curr_c += j - k
                else:
                    curr_c += j
                if proper_bound(g, curr_r, curr_c) and (i, j) != (0,0):
                    if g[curr_r][curr_c] == '#' and first_seen_flag is False:
                        occupied_seat_count += 1
                        first_seen_flag = True
                    elif g[curr_r][curr_c] == 'L' and first_seen_flag is False:
                        unoccupied_seat_count += 1
                        first_seen_flag = True
    return occupied_seat_count, unoccupied_seat_count

# Part 1

previous_occupied_seats = sum(i.count('#') for i in grid)
print("Round Count:\t{0}\nOccupied Seats:\t{1}\n".format(0, previous_occupied_seats))
# pprint([''.join(i) for i in grid])
print("\n")

for r_count in range(1000):

    current_grid = deepcopy(grid)
    for row_index in range(len(grid)):
        for column_index in range(len(grid[0])):
            adjacent_seat_list = adjacent_seat_layout(grid, row_index, column_index)
            if grid[row_index][column_index] == 'L':
                if '#' not in adjacent_seat_list:
                    current_grid[row_index][column_index] = '#'
            elif grid[row_index][column_index] == '#':
                if adjacent_seat_list.count('#') >= 4:
                    current_grid[row_index][column_index] = 'L'
            else:
                continue
    grid = deepcopy(current_grid)

    occupied_seats = sum(i.count('#') for i in grid)
    print("Round Count:\t{0}\nOccupied Seats:\t{1}\n".format(r_count, occupied_seats))
    # pprint([''.join(i) for i in grid])
    print("\n")

    if occupied_seats == previous_occupied_seats:
        break
    else:
        previous_occupied_seats = occupied_seats

# Part 2

previous_occupied_seats = sum(i.count('#') for i in grid)
print("Round Count:\t{0}\nOccupied Seats:\t{1}\n".format(0, previous_occupied_seats))
# pprint([''.join(i) for i in grid])
print("\n")

for r_count in range(1000):

    current_grid = deepcopy(grid)
    for row_index in range(len(grid)):
        for column_index in range(len(grid[0])):
            occupied_count, unoccupied_count  = cardinal_seat_count(grid, row_index, column_index)
            if grid[row_index][column_index] == 'L':
                if occupied_count == 0:
                    current_grid[row_index][column_index] = '#'
            elif grid[row_index][column_index] == '#':
                if occupied_count >= 5:
                    current_grid[row_index][column_index] = 'L'
            else:
                continue
    grid = deepcopy(current_grid)

    occupied_seats = sum(i.count('#') for i in grid)
    print("Round Count:\t{0}\nOccupied Seats:\t{1}\n".format(r_count, occupied_seats))
    # pprint([''.join(i) for i in grid])
    print("\n")

    if occupied_seats == previous_occupied_seats:
        break
    else:
        previous_occupied_seats = occupied_seats
