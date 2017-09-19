class BinaryTree:
    
    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node
    
    def insert(self,root,data):
        # Return the new root
        l = [root]
        while l:
            node = l.pop(0)
            if node.left_child and node.right_child:
                if data < node:
                    l.append(node.left_child)
                elif data > node:
                    l.append(node.right_child)
            else:
                if node.left_child:
                    if data < node:
                        node.left_child.left_child = data
                    if data > node:
                        node.left_child.right_child = data
                if node.right_child:
                    if data < node:
                        node.right_child.left_child = data
                    if data > node:
                        node.right_child.right_child = data
