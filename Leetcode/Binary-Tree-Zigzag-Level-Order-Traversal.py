# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        from collections import defaultdict
        
        zigzag = []
        queue = [root]        
        node_to_level = { root: 0 } # node to level
        level_map = defaultdict(list)
        level_map[0].append(root) # level to nodes
        
        
        while queue:
            node = queue.pop()
            if node.left:
                node_to_level[node.left] = node_to_level[node] + 1
                level_map[node_to_level[node] + 1].append(node.left)
                queue.append(node.left)
            if node.right:
                node_to_level[node.right] = node_to_level[node] + 1
                level_map[node_to_level[node] + 1].append(node.right)
                queue.append(node.right)
        
        left_to_right = True
        for key,val in level_map.items():
            temp = []
            for node in val:
                temp.append(node.val)
            if left_to_right:
                temp = temp[::-1]
                left_to_right = not left_to_right
            else:
                left_to_right = not left_to_right
            zigzag.append(temp)
        return zigzag
