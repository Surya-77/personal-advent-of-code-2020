from treelib import Tree, Node

tree = Tree()
tree.create_node("Harry", "harry")  # root node
tree.create_node("Jane", "jane", parent="harry")
tree.create_node("Bill", "bill", parent="harry")
tree.create_node("Diane", "diane", parent="jane")
tree.create_node("Mary", "mary", parent="diane")
tree.create_node("Mark", "mark", parent="jane")
tree.show()

new_tree = Tree()
new_tree.create_node("n1", 1)  # root node
new_tree.create_node("n2", 2, parent=1)
new_tree.create_node("n3", 3, parent=1)

new_tree.show()
tree.paste('bill', new_tree)
tree.show()