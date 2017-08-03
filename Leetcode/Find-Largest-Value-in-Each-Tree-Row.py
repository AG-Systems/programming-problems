# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def largeval(self, root, depth, results):
        if not root: #if node does not exist
            return
        if depth == len(results): #so if the level matches up with the length of the values
            results.append(root.val)
        else:
            results[depth] = max(results[depth], root.val)
        print results
        self.largeval(root.left, depth+1, results)
        self.largeval(root.right, depth+1, results)
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        container = []
        self.largeval(root, 0, container)
        return container
                
