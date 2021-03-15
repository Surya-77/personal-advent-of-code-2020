import re
import itertools
import pprint


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
            bag_rec_list.append([i[0], zip(sub_bags, sub_bags_count)])
            # bags_to_check_2_count.append(sub_bags_count)


for count in len(bag_rec_list):
    pprint.pprint("Main Bag : {0}\n Sub Bags : {1}\n".format(count[0], list(count[1])))

# pprint.pprint(bags_to_check_2)
# pprint.pprint(list(zip(bags_to_check_2, bags_to_check_2_count)))

# Excluding initial entry 'shiny gold' from the bag list.
print("Total Bags 2 : {0} \n".format(len((bags_to_check_2[1:]))))
