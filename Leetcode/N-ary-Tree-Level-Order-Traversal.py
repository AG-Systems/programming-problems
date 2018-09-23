"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        container = []
        queue = [root]
        while queue:
            temp = []
            tempq = []
            for node in queue:
                temp.append(node.val)
                if node.children:
                    for child in node.children:
                        tempq.append(child)
            container.append(temp)
            queue = tempq
        return container
