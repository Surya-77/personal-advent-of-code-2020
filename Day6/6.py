import functools
import string

f = open("./TestData.txt", "r")
raw_data = f.read()

data = raw_data.split('\n\n')
processed_data = [entry.split('\n') for entry in data]

flat_data = [functools.reduce(lambda a, b: a + b, entry) for entry in processed_data]
set_data = [map(lambda a: [i for i in a], processed_data)]

def get_union(input_list):
    total_length = 0
    for element in input_list:
        total_length += len(set(element))
    return total_length

def get_intersection(input_list):
    total_length = 0
    return None

print("Total questions answered : {0}".format(get_union(flat_data)))
