class Solution(object):
    def dfs(self, results, gen, left, right):
        if left > right:
            return
        
        if left == 0 and right == 0:
            results.append(gen)
            return 
        
        if left > 0:
            self.dfs(results, gen + "(", left - 1, right)
        if right > 0:
            self.dfs(results, gen + ")", left, right - 1)
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        self.dfs(results, "", n, n)
        return results
