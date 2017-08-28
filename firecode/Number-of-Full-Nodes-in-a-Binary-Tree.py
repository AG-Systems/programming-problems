class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node
    
    # Required collection modules have already been imported. 
    def number_of_full_nodes(self,root):
        counter = 0
        que = [root]
        while que:
            node = que.pop(0)
            if node:
                if node.left_child and node.right_child:
                    counter += 1
                    que.append(node.left_child)
                    que.append(node.right_child)
        return counter
