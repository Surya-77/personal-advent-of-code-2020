f = open("D:\Projects\AdventOfCode\Day5\TestData.txt", "r")
raw_data = f.read()

data = raw_data.split('\n')

def calculate_seat_number(code_list):
    seat_range_row = [0,127]
    for letter in code_list:
        mid_point = (seat_range_row[1] - seat_range_row[0])
        if letter == 'F':
            seat_range_row[0] = seat_range_row[0]
            seat_range_row[1] = mid_point // 2
        elif letter  == 'B':
            seat_range_row[0] = mid_point // 2 + 1
            seat_range_row[1] = seat_range_row[1]
        print(code_list, letter, seat_range_row)
    return seat_range_row

print(calculate_seat_number('FBFBBFFRLR'))