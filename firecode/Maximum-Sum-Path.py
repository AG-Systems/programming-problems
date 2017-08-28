class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    # All the necessary collection moduled have been already imported.
    
    def helper(self, root, max_num):
        if root == None:
            return 0
        left_sum = self.helper(root.left_child, max_num)
        right_sum = self.helper(root.right_child, max_num)
        sum_val = max(root.data + left_sum, root.data + right_sum)
        max_num[0] = max(max_num[0], left_sum + root.data + right_sum)
        return sum_val
        
    def max_sum_path(self,root):
        max_num = [0]
        self.helper(root, max_num)
        return max_num[0]
