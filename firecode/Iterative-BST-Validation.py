# Collections module has already been imported.
class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    
    def validate_BST_Itr(self,root):
        # Return type should be Boolean
        
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            
            if node.left_child:
                if node.data < node.left_child.data:
                    return False
                queue.append(node.left_child)
            if node.right_child:
                if node.data > node.right_child.data:
                    return False
                queue.append(node.right_child)
        return True
