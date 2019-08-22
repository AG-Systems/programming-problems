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
        
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.postorder_list = []
        
        def order(root):
            if root:
                for index in range(0,len(root.children)):
                    order(root.children[index])
                self.postorder_list.append(root.val)
        
        order(root)
        return self.postorder_list
"""
