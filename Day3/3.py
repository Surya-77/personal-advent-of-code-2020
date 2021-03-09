f = open("D:\Projects\AdventOfCode\Day3\InputData.txt", "r")
data = f.read()

input_data = data.split('\n')
answer_list = []
def tree_counter(x_move, y_move):
    x_max_len = len(input_data)
    y_max_len = len(input_data[0])

    x_pos = 0
    y_pos = 0
    tree_count = 0
    free_count = 0
    while True:    
        x_pos = x_pos + x_move
        if (x_pos >= x_max_len):
            break
        y_pos = (y_pos + y_move) % y_max_len
        if (input_data[x_pos][y_pos]) == '#':
            tree_count += 1
        if (input_data[x_pos][y_pos]) == '.':
            free_count += 1
    print("For {2},{3} Trees : {0} Free Land : {1}".format(tree_count, free_count, x_move, y_move))
    return (tree_count, free_count)

answer_list.append(tree_counter(1,1))
answer_list.append(tree_counter(1,3))
answer_list.append(tree_counter(1,5))
answer_list.append(tree_counter(1,7))
answer_list.append(tree_counter(2,1))

final_answer = 1
for i in range(5):
    final_answer *= answer_list[i][0]

print(final_answer)