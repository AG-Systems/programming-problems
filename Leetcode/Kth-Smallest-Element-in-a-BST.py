# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root == None:
            return 0
        
        self.kth_smallest = None
        self.k_val = k
        
        def search(root):
            if root:
                search(root.left)
                if self.k_val > 1:
                    self.k_val -= 1
                else:
                    if self.k_val != -1:
                        self.kth_smallest = root.val
                        self.k_val = -1
                search(root.right)
                
        search(root)
        return self.kth_smallest
