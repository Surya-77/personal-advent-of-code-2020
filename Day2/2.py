f = open("D:\Projects\AdventOfCode\Day2\InputData.txt", "r")
data = f.read()

input_data = data.split('\n')
input_data = [element.split(':') for element in input_data]

def solution_part_1(input_data):
    valid_passes = 0
    for element in input_data:
        is_correct = False
        count = element[0].split(' ')[0]
        lower_count = int(count.split('-')[0])
        upper_count = int(count.split('-')[1])
        letter = element[0].split(' ')[1]
        text = element[1]
        if text.count(letter) <= upper_count and text.count(letter) >= lower_count:
            valid_passes += 1
            is_correct = True
        # print("{0:4}{1:4}{2:>3}{3:25}{4:6}\n".format(lower_count, upper_count, letter, text, is_correct))
    return valid_passes

def solution_part_2(input_data):        
    valid_passes = 0
    for element in input_data:
        is_correct = False
        count = element[0].split(' ')[0]
        lower_count = int(count.split('-')[0])
        upper_count = int(count.split('-')[1])
        letter = element[0].split(' ')[1]
        text = element[1].split(' ')[1]
        lower_count_text = text[lower_count-1]
        upper_count_text = text[upper_count-1]
        a = bool(lower_count_text == letter)
        b = bool(upper_count_text == letter)
        if  (a is False and b is True) ^ (a is True and b is False):
            valid_passes += 1
            is_correct = True
        print("{0:4}{1:4}{2:>3}{3:25}{4:>3}{5:>3}{6:6}\n".format(lower_count, upper_count, letter, text, lower_count_text, upper_count_text, is_correct))
    return valid_passes

# print('{0:42}{1:6}'.format('Number of valid passes for Part 1 is ',solution_part_1(input_data)))
print('{0:42}{1:6}'.format('Number of valid passes for Part 2 is ', solution_part_2(input_data)))