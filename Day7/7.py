import re
import itertools
import pprint
from treelib import Tree, Node

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

tree_list = []
for i in range(len(pd)):
    tree_list.append(Tree())
    tree_list[i].create_node(pd[i][0], pd[i][0])
    for j in range(1, len(pd[i])):
        bag_name = ' '.join(pd[i][j].split(' ')[1:])
        bag_count = int(pd[i][j].split(' ')[0])
        
