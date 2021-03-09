import math

print("Running program to solve ...")

f = open("D:\Projects\AdventOfCode\Day1\InputData.txt", "r")
data = f.read()
data_list = data.split('\n')
data_list = list(map(int, data_list)) 

def append_to_subset(input_set, subset):
    for element in input_set:
        subset.append([element])
    return subset


def generate_size_two_subset(input_list):
    answer = []
    for index_1, element_1 in enumerate(input_list):
        for index_2, element_2 in enumerate(input_list):
                if index_1 != index_2:
                    answer.append([element_1, element_2])
    return answer
    
def generate_size_three_subset(input_list):
    answer = []
    for index_1, element_1 in enumerate(input_list):
        for index_2, element_2 in enumerate(input_list):
            for index_3, element_3 in enumerate(input_list):
                if index_1 != index_2 and index_2 != index_3 and index_1 != index_3:
                    answer.append([element_1, element_2, element_3])
    return answer

def find_the_value_new(input_list):
    answer = []
    for element in input_list:
        if sum(element) == 2020:
            return [math.prod(element), element]
    return None

answer_1_1, answer_1_2 = find_the_value_new(generate_size_two_subset(data_list))
answer_2_1, answer_2_2 = find_the_value_new(generate_size_three_subset(data_list))

print("Answer is {0} formed by {1}".format(answer_1_1, answer_1_2))
print("Answer is {0} formed by {1}".format(answer_2_1, answer_2_2))

