import itertools

f = open("./InputData.txt", "r")
raw_data = f.read()
input_data = [int(i) for i in raw_data.split('\n')]
max_jolt = max(input_data) + 3
input_data.append(max_jolt)
source_jolt = 0
transitions = []
possible_choices = []
for count in range(len(input_data)):
    choices = []
    for element in input_data:
        if (element - source_jolt) <= 3:
            choices.append(element)
    if len(choices) == 0:
        break
    best_choice = min(choices)
    possible_choices.append(choices)

    transitions.append([source_jolt, best_choice])
    print("{0:<10}{1:<20}{2}".format(source_jolt, str(choices), best_choice))
    source_jolt = best_choice
    if source_jolt in input_data:
        input_data.remove(source_jolt)

transition_diffs = [i[1] - i[0] for i in transitions]
transition_diffs_set = list(set(transition_diffs))
transition_diffs_set_occurences = [transition_diffs.count(i) for i in transition_diffs_set]
print("Set : {0:>33}\nOccurences : {1:>26}".format(str(transition_diffs_set), str(transition_diffs_set_occurences)))
print("Answer 1 : {0:>24}".format(transition_diffs_set_occurences[0] * transition_diffs_set_occurences[1]))

for choice in possible_choices:
    if len(choice) > 3:
        pass


def reduce_choices(input_list):
    redundant_choices = []
    for choice in input_list:
        if len(choice) > 1:
            for element in choice:
                if element not in redundant_choices:
                    redundant_choices.append(element)

    flat_possible_choices = list(set(itertools.chain.from_iterable(input_list)))
    unique_choices = list(set(flat_possible_choices) - set(redundant_choices))

    output_list = input_list[:]
    for choice in input_list:
        if len(choice) == 1:
            if choice[0] in unique_choices:
                output_list.remove(choice)
    return output_list


def get_combos(input_list):
    cart_prod = [hash(frozenset(i)) for i in list(itertools.product(*input_list))]
    cart_prod = list(set(cart_prod))
    output = len(cart_prod)
    # print("Combos : {0}".format(output))
    return output

reduced_choices = reduce_choices(possible_choices)
divided_list_index = []
count = 0
for i, v in enumerate(reduced_choices):
    count += 1
    if len(v) == 1:
        divided_list_index.append(count)
        count = 0

iterator_of_reduced_choices = iter(reduced_choices)
divided_list = [list(itertools.islice(iterator_of_reduced_choices, i)) for i in divided_list_index]

ans = 1
for sub_list in divided_list:
    ans *= get_combos(sub_list)


print("Combos : {0}".format(ans))

