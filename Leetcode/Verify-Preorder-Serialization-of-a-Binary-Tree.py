class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        container = []
        num = 0
        counter = 0
        s = preorder.split(",")
        while num < len(s)-2:
            if s[num] != "#" and s[num+1] == "#" and s[num+2] == "#":
                del s[num], s[num+1]
                num = -1
            num += 1
        print(s)
        if len(s) == 1:
            if s[0] == "#":
                return True
            else:
                return False
        else:
            return False
                
                
                
            
                
                
                
                
        
            
