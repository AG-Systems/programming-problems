# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        depth = 0
        container = []
        container.append(root)
        while container:
            depth += 1
            for x in range(0, len(container)):
                node = container.pop(0)
                if node.left:
                    container.append(node.left)
                if node.right:
                    container.append(node.right)
        return depth
                    
        
