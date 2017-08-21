class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    def number_of_leaves(self,root, leaves=0):
        left = 0
        right = 0
        if root:
            if not root.left_child and not root.right_child:
                return 1
            else:
                if root.left_child:
                    left = self.number_of_leaves(root.left_child, leaves)
                if root.right_child:
                    right =  self.number_of_leaves(root.right_child, leaves)
        return sum([left,right,leaves])
