# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def treenodes(self, root, leafs):
        if root:
            if root.left == None and root.right == None:
                leafs.append(root.val)
                return leafs
            else:
                self.treenodes(root.left, leafs)
                self.treenodes(root.right, leafs) 
                return leafs
        else:
            return leafs
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        seq1 = self.treenodes(root1, [])
        seq2 = self.treenodes(root2, [])
        if seq1 == seq2:
            return True
        else:
            return False

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, container):
        if root == None:
            return container
        if root.left == None and root.right == None:
            container.append(root.val)
            return container
        self.helper(root.left, container)
        self.helper(root.right, container)
        return container
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        seq1 = self.helper(root1, [])
        seq2 = self.helper(root2, [])
        
        return seq1 == seq2
'''
