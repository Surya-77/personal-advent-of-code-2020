import re
import itertools
import pprint
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

bags_to_check = ['shiny gold']
bags_to_check_2 = ['shiny gold']

bag_rec_list = []

# Range was selected based on trial and error for probable maximum depth.
for iter_i in range(6): 
    for i in pd:
        sub_bags = [' '.join(k.split(' ')[1:]) for k in i[1:]]
        for target_bag in bags_to_check:
            if i[0] not in bags_to_check and target_bag in sub_bags:
                bags_to_check.append(i[0])

# pprint.pprint(bags_to_check)

# Excluding initial entry 'shiny gold' from the bag list.
print("Total Bags : {0} \n".format(len((bags_to_check[1:]))))

# for iter_i in range(6):
#     for i in pd:
#         if i[0] in bags_to_check_2:
#             sub_bags = [' '.join(k.split(' ')[1:]) for k in i[1:]]
#             for sub_bag in sub_bags:
#                 if sub_bag not in bags_to_check_2:
#                     bags_to_check_2.append(sub_bag)

for iter_i in range(6):
    for i in pd:
        if i[0] in bags_to_check_2:
            sub_bags = [' '.join(k.split(' ')[1:]) for k in i[1:]]
            sub_bags_count = [int(k.split(' ')[0]) for k in i[1:]]
            for sub_bag in sub_bags:
                if sub_bag not in bags_to_check_2:
                    bags_to_check_2.append(sub_bag)
            bag_rec_list.append([i[0], sub_bags, sub_bags_count, 1])


bag_rec_list_names = [bag[0] for bag in bag_rec_list]
bag_rec_unique = []

for bag in bag_rec_list:
    if bag[0] not in [i[0] for i in bag_rec_unique]:
        bag_rec_unique.append(bag)

# bag_rec_unique_original = deepcopy(bag_rec_unique)
# bag_t1 = None
# for iter_i in range(5):
#     for bag_1 in list(bag_rec_unique):
#         if len(bag_1[1]) == iter_i:
#             bag_t1 = bag_1[0]
#             removal_index_1 = [i[0] for i in bag_rec_unique].index(bag_t1)
#             former_value = bag_rec_unique[removal_index_1][3]
#             for index_2, bag_2 in enumerate(list(bag_rec_unique)):
#                 if bag_t1 in bag_2[1]:
#                     removal_index_2 = bag_rec_unique[index_2][1].index(bag_t1)
#                     value = bag_rec_unique[index_2][2][removal_index_2]
#                     bag_rec_unique[index_2][3] += value * former_value
#                     del(bag_rec_unique[index_2][1][removal_index_2])
#                     del(bag_rec_unique[index_2][2][removal_index_2])
#             print(bag_rec_unique[removal_index_1], removal_index_1)
#             del(bag_rec_unique[removal_index_1])


bag_rec_unique_original = deepcopy(bag_rec_unique)
bag_t1 = None
exit_loop = False

for iter_i in range(7):

    # if exit_loop is True:
    #     break

    for bag_1 in list(bag_rec_unique):
        
        # removal_index_main = [i[0] for i in bag_rec_unique].index('shiny gold')
        # print("{0}".format(bag_rec_unique[removal_index_main]))
        # if len(bag_rec_unique[removal_index_main][1]) <= 1:
        #     exit_loop =  True
        #     break

        if len(bag_1[1]) == 0:
            bag_t1 = bag_1[0]
            removal_index_1 = [i[0] for i in bag_rec_unique].index(bag_t1)
            former_value = bag_rec_unique[removal_index_1][3]
            for bag_2 in list(bag_rec_unique):
                if bag_t1 in bag_2[1]:
                    removal_index_2 = [i[0] for i in bag_rec_unique].index(bag_2[0])
                    removal_index_3 = bag_2[1].index(bag_t1)
                    value = bag_2[2][removal_index_3]
                    bag_rec_unique[removal_index_2][3] += (value * former_value)
                    del(bag_rec_unique[removal_index_2][1][removal_index_3])
                    del(bag_rec_unique[removal_index_2][2][removal_index_3])
            # print(bag_rec_unique[removal_index_1], removal_index_1)
            del(bag_rec_unique[removal_index_1])
    
    # print(list(set([i[0] for i in bag_rec_unique_original]) - set([i[0] for i in bag_rec_unique])))

    print("After Iteration\t{0}\n".format(iter_i))
    for j in range(len(bag_rec_unique)):
        print(bag_rec_unique[j],"\n")
    print("\n\n")
    


# for bag in (bag_rec_unique):
#     print("Main Bag : {0} \nSub Bags : {1}\nBag Count: {2}\nTotal Count: {3}\n".format(bag[0], bag[1], bag[2], bag[3]))


# Excluding initial entry 'shiny gold' from the bag list.
print("Total Bags 2 : {0} \n".format(len((bags_to_check_2[1:]))))
