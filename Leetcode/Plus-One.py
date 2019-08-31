class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == None or len(digits) == 0:
            return None
        
        num_str = ''.join(str(e) for e in digits)
        num_str = int(num_str)
        num_str += 1
        num_str = str(num_str)
        
        answer = []
        for digit in num_str:
            answer.append(digit)
        return answer
        
                
