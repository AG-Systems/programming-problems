"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        container = []
        def dfs(root):
            if root == None:
                return None
            for child in root.children:
                dfs(child)
            container.append(root.val)
        dfs(root)
        return container
        
