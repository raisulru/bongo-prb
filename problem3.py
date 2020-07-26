class Node: 
	
	def __init__(self, value): 
		self.value = value 
		self.parent = None

def find_lca(node1, node2): 
	
	if node1.parent is None: 
		return node1.value
	
	if node2.parent is None: 
		return node2.value
	
	if node1.parent == node2.parent:
	    return node1.parent.value

	if node1.parent.value == node2.value:
		return node2.value
	
	if node2.parent.value == node1.value:
		return node1.value
	
	return find_lca(node1.parent, node2.parent)


root = Node(1)
node2 = Node(2)
node2.parent = root
node3 = Node(3)
node3.parent = root
node4 = Node(4)
node4.parent = node2
node5 = Node(5)
node5.parent = node2
node8 = Node(8)
node8.parent = node4
node9 = Node(9)
node9.parent = node4
node6 = Node(6)
node6.parent = node3
node7 = Node(7)
node7.parent = node3

print(find_lca(node9, node5))
