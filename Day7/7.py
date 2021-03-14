import re
import itertools
import pprint

f = open("./TestData.txt", "r")
raw_data = f.read()

list_data = raw_data.split('\n')
pd = []

for entry in list_data:
    pass_1 = re.sub("(contain)|(bags*)|(\,+)|(\.+)|(no\s+other)", " ", entry)
    pass_2 = re.sub("(\s{2,})|([ \t]+$)",",",pass_1)
    pass_3 = re.sub(",(?!.*,)", "",pass_2)
    pd.append(pass_3.split(','))

pd_flag = [[False for column in row] for row in pd]

target_bag = 'shiny gold'
other_target_bag = 'shiny gold'
count = 0
i = 0



# list_of_bag_colors = []
# list_of_sub_bag_colors = []
# list_of_sub_bag_contents = []
# for entry in pd:
#     bag_color = entry[0]
#     sub_bag_colors = list(map(lambda a:' '.join(a.split(' ')[1:]), entry[1:]))
#     sub_bag_count = list(map(lambda a:a.split(' ')[0], entry[1:]))
#     sub_bag_contents = list(zip(sub_bag_colors, sub_bag_count))
#     list_of_bag_colors.append(bag_color)
#     list_of_sub_bag_colors.append(sub_bag_colors)
#     list_of_sub_bag_contents.append(sub_bag_contents)

# dict_of_entries = {}
# for entry in zip(list_of_bag_colors, list_of_sub_bag_contents):
#     if len(entry[1]) > 0:
#         sub_entry_dict = {}
#         for sub_entry in entry[1]:
#             sub_entry_dict[sub_entry[0]] = sub_entry[1]
#         dict_of_entries[entry[0]] = sub_entry_dict

# pprint.pprint(dict_of_entries)

# for outer_entry in dict_of_entries:
#     for inner_entry in dict_of_entries:
#         if outer_entry in dict(dict_of_entries[inner_entry].keys()):a
#             dict_of_entries[outer_entry]








