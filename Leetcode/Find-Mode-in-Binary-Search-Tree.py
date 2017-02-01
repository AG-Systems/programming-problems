# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mode(self,root,container):
        if root:
            if root.val in container:
                container[root.val] += 1
            else:
                container[root.val] = 1
        else:
            return container
        return self.mode(root.left, container) and self.mode(root.right, container)
        
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r = []
        if not root:
            return r
        container = {}
        x = self.mode(root,container)
        max_key = max(x, key=lambda k: x[k])
        for key,val in x.items():
            if val >= x[max_key]:
                r.append(key)
        return r 
