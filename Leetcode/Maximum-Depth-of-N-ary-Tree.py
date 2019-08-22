"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        
        def dfs(root, level):
            level += 1
            if root and root.children:
                return max([dfs(child, level) for child in root.children])
            else:
                return level
                
        return dfs(root, 0)
