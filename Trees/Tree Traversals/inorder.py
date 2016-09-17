def inorder(tree):
	inorder(tree.getLeftChild())
	print tree.getRootVal()
	inorder(tree.getRightChild())