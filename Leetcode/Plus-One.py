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
        
                
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits) - 1] += 1

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] > 9:
                digits[i] %= 10
                if (i - 1 < 0):
                    digits.insert(0, 1)
                else:
                    digits[i - 1] += 1

        return digits
"""
