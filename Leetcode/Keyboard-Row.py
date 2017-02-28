class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = ["q","w","e","r","t","y","u","i","o","p","Q","W","E","R","T","Y","U","I","O","P"]
        row2 = ["a","s","d","f","g","h","j","k","l","A","S","D","F","G","H","J","K","L"]
        row3 = ["z","x","c","v","b","n","m","Z","X","C","V","B","N","M"]
        container = []
        for x in words:
            s = list(x)
            counter = 0
            if s[0] in row1:
                select_id = row1
            if s[0] in row2:
                select_id = row2
            if s[0] in row3:
                select_id = row3
            for x in s:
                if x in select_id:
                    counter += 1
            s = ''.join(s)
            if counter == len(s):
                container.append(s)
        return container
                
                    
                
        
