import functools
import string

f = open("./InputData.txt", "r")
raw_data = f.read()

data = raw_data.split('\n\n')
list_data = [entry.split('\n') for entry in data]

flat_data = [functools.reduce(lambda a, b: a + b, entry) for entry in list_data]
set_data = [[set(list(i)) for i in entry] for entry in list_data]

def get_union(input_list):
    total_count = 0
    for element in input_list:
        union_count = len(set(element)) 
        total_count += union_count
    return total_count

def get_intersection(input_list):
    total_count = 0
    for entry in set_data:
        intersection_count = len(entry[0].intersection(*entry))
        total_count += intersection_count
    return total_count

print("Total Union Count : {0:>12} \nTotal Intersection Count : {1:>5}".format(
    get_union(flat_data), get_intersection(set_data)))
