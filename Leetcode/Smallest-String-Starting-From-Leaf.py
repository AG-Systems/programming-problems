# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if root == None:
            return ""
        
        self.smallest_string = "~"
        
        def dfs(root, new_str):
            if root:
                new_str.append(chr(root.val + ord('a')))
                
                if root.left == None and root.right == None:
                    self.smallest_string = min(self.smallest_string, "".join(new_str[::-1]))
                dfs(root.left, new_str)
                dfs(root.right, new_str)
                new_str.pop()
        
        dfs(root, [])
        return self.smallest_string
