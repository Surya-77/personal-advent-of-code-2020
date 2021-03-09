f = open("./InputData.txt", "r")
raw_data = f.read()

data = raw_data.split('\n')

def calculate_seat_number(code_list, low, high):
    current_low = low
    current_high = high
    for letter in code_list:
        mid = (max(current_high, current_low) - min(current_high, current_low)) // 2 + min(current_low, current_high)
        if letter  == 'F' or  letter == 'L':
            current_high = mid
        if  letter == 'B' or letter == 'R':
            current_low = mid + 1
        # print("Letter : {0} Low : {1} High : {2} Mid : {3}".format(letter, current_low, current_high, mid))
    final_number = min(current_low, current_high)
    return final_number

# row_id = calculate_seat_number('FFFBBBFRRR'[:7],0,127)
# column_id = calculate_seat_number('FFFBBBFRRR'[-3:],0,7)
# seat_id = row_id * 8 + column_id
# print("Row ID: {0} Column ID: {1} Seat ID:{2}".format(row_id, column_id, seat_id))

seat_id_list = []
seat_id_max = 0
for entry in data:
    row_id = calculate_seat_number(entry[:7],0,127)
    column_id = calculate_seat_number(entry[-3:],0,7)
    seat_id = row_id * 8 + column_id
    print("Code: {4} Row ID: {0:<5} Column ID: {1:<7} Seat ID:{2:<7} Max Seat ID:{3}".format(
        row_id, column_id, seat_id, seat_id_max, entry))
    seat_id_max = max(seat_id, seat_id_max)
    seat_id_list.append(seat_id)

possible_seat_id_list = range(min(set(seat_id_list)), max(set(seat_id_list))+1)
empty_seats = list(set(possible_seat_id_list) - set(seat_id_list))


print("Max Seat ID: {0}".format(seat_id_max))
print("Empty Seat ID: {0}".format(empty_seats[0]))

        