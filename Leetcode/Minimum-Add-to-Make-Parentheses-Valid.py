class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if S == "" or S == None:
            return 0
        
        stack = []
        steps = 0
        for char in S:
            if char == "(":
                stack.append(char)
            if char == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    steps += 1
        
        steps += len(stack)
        return steps
