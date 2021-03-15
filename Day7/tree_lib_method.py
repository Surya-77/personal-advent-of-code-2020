import re
import itertools
import pprint
from treelib import Tree, Node
from copy import deepcopy

f = open("./InputData.txt", "r")
raw_data = f.read()

list_data = raw_data.split('\n')
pd = []

for entry in list_data:
    pass_1 = re.sub("(contain)|(bags*)|(\,+)|(\.+)|(no\s+other)", " ", entry)
    pass_2 = re.sub("(\s{2,})|([ \t]+$)",",",pass_1)
    pass_3 = re.sub(",(?!.*,)", "",pass_2)
    pd.append(pass_3.split(','))

pd_flag = [[False for column in row] for row in pd]

tree_list = []
for i in range(len(pd)):
    tree_list.append(Tree())
    tree_list[i].create_node(pd[i][0], pd[i][0])
    for j in range(1, len(pd[i])):
        bag_name = ' '.join(pd[i][j].split(' ')[1:])
        bag_count = int(pd[i][j].split(' ')[0])
        tree_list[i].create_node(bag_name, bag_name, parent=pd[i][0], data=bag_count)

target_bag = 'shiny gold'
copy_target = None
checked_list = []

# pprint.pprint("Original Tree")
# for i in tree_list:
#     i.show()

loop_count = 0
for loop_count in range(len(tree_list)):
    for i in tree_list:
        if (i.contains(target_bag)) and (i.root != target_bag) and (i.root not in checked_list):
            copy_target = i
            checked_list.append(copy_target.root)
            break

    for i in tree_list:
        if i.contains(copy_target.root) and (i.root != copy_target.root):

            print("Original Tree\n")
            copy_target.show()
            print("Modified Tree\n")
            i.show()
            original_parent = i.parent(copy_target.root).identifier
            i.remove_node(copy_target.root)
            i.paste(original_parent, copy_target)

bag_count = 0
for i in tree_list:
    if i.contains(target_bag) and (i.root != target_bag):
        bag_count += 1


# pprint.pprint("Modified Tree")
# for i in tree_list:
#     if i.contains(target_bag):
#         i.show()

pprint.pprint("Bag Count : {0}".format(bag_count))
