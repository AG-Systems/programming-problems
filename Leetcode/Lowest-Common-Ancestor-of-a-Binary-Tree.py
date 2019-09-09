# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        if p.val == q.val:
            return p.val
        
        def dfs(root, val):
            if root == None:
                return None
            if root.val == val:
                return [root]
            left_path = dfs(root.left, val)
            if left_path:
                left_path.append(root)
                return left_path
            right_path = dfs(root.right, val)
            if right_path:
                right_path.append(root)
                return right_path
            return None
        
        p_path = dfs(root, p.val)
        q_path = dfs(root, q.val)
        LCA = None
        while p_path and q_path:
            p_node = p_path.pop()
            q_node = q_path.pop()
            if p_node.val == q_node.val:
                LCA = p_node
            else:
                break
        
        return LCA
                
