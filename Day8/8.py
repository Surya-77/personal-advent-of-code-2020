import re
import itertools

f = open("./InputData.txt", "r")
raw_data = f.read()
instruction_set = [i.split(' ') for i in raw_data.split('\n')]
visited_locations = []
instruction_set_length = len(instruction_set)

kill_count = 0
acc = 0
curr_loc = 0
    
while kill_count < 10000:

    instr = instruction_set[curr_loc][0]
    instr_value = int(instruction_set[curr_loc][1])
    
    if curr_loc not in visited_locations:
        visited_locations.append(curr_loc)
    else:
        break

    if instr == 'nop':
        new_loc = (curr_loc + 1) % instruction_set_length
    if instr == 'acc':
        acc += instr_value
        new_loc = (curr_loc + 1) % instruction_set_length
    if instr == 'jmp':
        new_loc = (curr_loc + instr_value) % instruction_set_length
    curr_loc = new_loc

    kill_count += 1

print("Accumulator Value : {:0} Run Time : {:1}".format(acc, kill_count))

# Part 2

req_indices = [j_i for j_i, j_v in enumerate([i[0] for i in instruction_set]) if j_v == 'jmp' or j_v == 'nop']

print("Indices {0}".format(req_indices))
for index in req_indices:
    
    term_flag = False
    kill_count = 0
    acc = 0
    curr_loc = 0
    visited_locations = []

    instruction_set_mod = instruction_set[:]
    if instruction_set_mod[index][0] == 'nop':
        instruction_set_mod[index] = ['jmp', instruction_set_mod[index][1]]
    elif instruction_set_mod[index][0] == 'jmp':
        instruction_set_mod[index] = ['nop', instruction_set_mod[index][1]]

    # print("\nOriginal : ", instruction_set)
    # print("\nModified : ", instruction_set_mod)
    # print("\n")

    while kill_count < 100000:

        instr = instruction_set_mod[curr_loc][0]
        instr_value = int(instruction_set_mod[curr_loc][1])
        
        if curr_loc not in visited_locations:
            visited_locations.append(curr_loc)
        else:
            break

        if instr == 'nop':
            new_loc = (curr_loc + 1) % instruction_set_length  
        if instr == 'acc':
            acc += instr_value
            new_loc = (curr_loc + 1) % instruction_set_length  
        if instr == 'jmp':
            new_loc = (curr_loc + instr_value) % instruction_set_length  
        
        if curr_loc == (instruction_set_length - 1) and new_loc == 0:
            term_flag = True
            break
        else:
            curr_loc = new_loc
    
        kill_count += 1

    print("Accumulator Value : {0:<12} Run Time : {1:<8} Term : {2}".format(acc, kill_count, term_flag))
    
    if term_flag == True:
        break

    