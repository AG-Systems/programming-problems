class BinaryTree:
    
    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node
    
    def find_min(self,root):
        # Return element should be of type TreeNode
        if not root:
            return None
        else:
            if not root.left_child:
                return root
            else:
                return self.find_min(root.left_child)
                
