# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        container = []
        sum = 0
        container.append(root)
        while container:
            for x in range(0, len(container)):
                node = container.pop(0)
                if node.left:
                    container.append(node.left)
                    if node.left.left == None:
                        if node.left.right == None:
                            sum += node.left.val
                if node.right:
                    container.append(node.right)
        return sum
            
