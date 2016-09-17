def postorder(tree):
	postorder(tree.getLeftChild())
	postOrder(tree.getRightChild())
	print tree.getRootVal()