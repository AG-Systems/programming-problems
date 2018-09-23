class BinaryTree:
    
    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node
    
    def find_max(self,root):
        # Return element should be of type TreeNode
        
        while root:
            if root.right_child:
                root = root.right_child
            else:
                return root
