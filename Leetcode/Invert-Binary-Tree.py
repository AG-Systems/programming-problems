# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        container  = [root]
        while container:
            node = container.pop(0)
            temp = node.right
            node.right = node.left
            node.left = temp
            if node.left:
                container.append(node.left)
            if node.right:
                container.append(node.right)
        return root
                
