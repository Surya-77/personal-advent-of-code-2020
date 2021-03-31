import itertools

f = open("./InputData.txt", "r")
raw_data = f.read()

input_data = [int(i) for i in raw_data.split('\n')]
preamble_size = 25
required_value = 0


def extract_sub_arrays(array):
    result = []
    for i in range(len(array)):
        for j in range(i, len(array) + 1):
            sub_array = array[i:j]
            if len(sub_array) > 1:
                result.append(sub_array)
    return result


# Part 1

for i in range(preamble_size, len(input_data)):
    preamble = input_data[i - preamble_size:i:1]

    preamble_perms = itertools.permutations(preamble, r=2)
    # preamble_added = itertools.starmap(lambda x, y: x+y, preamble_perms)
    preamble_added = map(lambda x: sum(x), preamble_perms)
    is_input_present = map(lambda x: 1 if x == input_data[i] else 0, preamble_added)
    if 1 not in is_input_present:
        required_value = input_data[i]
        print("Non conforming value : {0}".format(required_value))
        break

# Part 2

sub_array_input_data = extract_sub_arrays(input_data)
sub_array_added = map(lambda x: sum(x), sub_array_input_data)
required_sub_array = sub_array_input_data[list(sub_array_added).index(required_value)]
required_second_value = min(required_sub_array) + max(required_sub_array)
print("Required sub array is : {0:<40} Required Value is {1}".format(str(required_sub_array), required_second_value))

# print(extract_sub_arrays(input_data[0:5]))
