# Method using treelib library

# tree = Tree()
# tree.create_node(tag="bag", identifier="bag", parent=None)
# list_of_bag_colors = []
# list_of_sub_bag_colors = []

# for entry in processed_data:
#     bag_color = entry[0]
#     sub_bag_colors = list(map(lambda a:' '.join(a.split(' ')[1:]), entry[1:]))
#     sub_bag_count = list(map(lambda a:a.split(' ')[0], entry[1:]))
#     sub_bag_contents = list(zip(sub_bag_colors, sub_bag_count))
#     list_of_bag_colors.append(bag_color)
#     list_of_sub_bag_colors.append(sub_bag_colors)

#     # print(bag_color, sub_bag_contents)
#     # if len(sub_bag_contents) == 0:
#     #     tree.create_node(tag=bag_color, identifier=bag_color, parent="bag")
#     # else:
#     #     for content in sub_bag_contents:
#     #         tree.create_node(tag=content[0], identifier=content[0], parent=bag_color)

# set_of_bag_colors = set(list_of_bag_colors)
# set_of_sub_bag_colors = set(itertools.chain.from_iterable(list_of_sub_bag_colors))
# set_of_basic_colors=  set_of_bag_colors - set_of_sub_bag_colors
# list_of_basic_colors = list(set_of_basic_colors)

# for entry in zip(list_of_bag_colors, list_of_sub_bag_colors):
#     if entry[0] in list_of_basic_colors:
#         tree.create_node(tag=entry[0], identifier=entry[0], parent='bag')
#     if len(entry[1]) > 0:
#         for sub_color in entry[1]:
#             tree.create_node(tag=sub_color, identifier=sub_color, parent=entry[0])