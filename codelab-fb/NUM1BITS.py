class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        if int(A):
            binary = str('{0:b}'.format(int(A)))
            return int(binary.count('1'))
        else:
            return 0 #error

      
 # Other solution: 
"""
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        ret = 0
        while A != 0:
            if A&1:
                ret += 1
            A = A >> 1
        return ret

"""
