class BinaryTree:
    
    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node
    
    # Helper Method    
    def size(self,root):
        if root == None:
            return 0
        else:
            return (self.size(root.left_child) + 1 + self.size(root.right_child)) 
        
    def find_kth_largest(self,root,k):
        # Return Element should be of type TreeNode
        if not root:
            return None
        else:
            right_size = self.size(root.right_child)
            if right_size + 1 == k:
                return root
            if k < right_size:
                return self.find_kth_largest(root.right_child, k)
            else:
                return self.find_kth_largest(root.left_child, k - right_size - 1)
        # need to work on this problem
