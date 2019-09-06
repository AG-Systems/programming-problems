# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        import heapq
        heap = []
        heapq.heapify(heap)
        
        self.min_val_set = set()
        
        def helper(root):
            if root == None:
                return None
            self.min_val_set.add(root.val)
            helper(root.left)
            helper(root.right)
        
        helper(root)
        for val in self.min_val_set:
            heapq.heappush(heap, val)
        
        min_val_list = heapq.nsmallest(2, heap)
        if len(min_val_list) < 2:
            return -1
        else:
            return min_val_list[1]
        
