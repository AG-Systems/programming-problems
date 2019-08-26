# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        container = [root]
        r = []
        counter = 0
        if not root:
            return r
        else:
            r.append([])
        while container:
            node = container.pop(0)
            if node.right or node.left:
                counter += 1
                if counter == 1:
                    r[counter-1].append(node.val)
                r.append([])
            if node.left:
                container.append(node.left)
                r[counter].append(node.left.val)
            if node.right:
                container.append(node.right)
                r[counter].append(node.right.val)
        return r
        
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        level_order_list = []
        
        def dfs(root,lvl):
            if root:
                if len(level_order_list) <= lvl:
                    level_order_list.append([])
                level_order_list[lvl].append(root.val)
                lvl += 1
                dfs(root.left, lvl)
                dfs(root.right, lvl)
        
        dfs(root, 0)
        return level_order_list
"""
