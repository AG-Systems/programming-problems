# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head = TreeNode(None)
        self.current = head
        
        def inorder(root):
            if root:
                inorder(root.left)
                root.left = None
                self.current.right = root
                self.current = root
                inorder(root.right)
        
        inorder(root)
        return head.right
                
