"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        container = []
        def dfs(root):
            if root == None:
                return None
            container.append(root.val)
            for child in root.children:
                dfs(child)
        dfs(root)
        return container
