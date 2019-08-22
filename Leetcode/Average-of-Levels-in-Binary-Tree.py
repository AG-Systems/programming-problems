# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        def avg_value(level_list):
            return sum(level_list) / len(level_list)
        
        def dfs(root, level, level_table):
            if root:
                level += 1
                if level in level_table:
                    level_table[level].append(root.val)
                else:
                    level_table[level] = [root.val]
                dfs(root.left, level, level_table)
                dfs(root.right, level, level_table)
                return level_table
        
        
        level_table = dfs(root, 0, {})
        print(level_table)
        average_values = []
        for keys,val in level_table.items():
            average_values.append(avg_value(val))
        
        return average_values
