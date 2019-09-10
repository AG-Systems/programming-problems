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
        if p.val < root.val and q.val > root.val:
            return root
        elif p.val > root.val and q.val < root.val:
            return root
        
        def search(root, val, path):
            if root == None:
                return None
            if root.val == val:
                path.append(root)
                return path
            path.append(root)
            if root.val > val:  
                return search(root.left, val, path)
            elif root.val < val:
                return search(root.right, val, path)
            
        p_path = search(root, p.val, [])
        q_path = search(root, q.val, [])
        lca = None
        while p_path and q_path:
            p_node = p_path.pop(0)
            q_node = q_path.pop(0)
            if q_node.val == p_node.val:
                lca = q_node
            else:
                break
        return lca
        
                
