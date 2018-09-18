class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        if int(A):
            binary = str('{0:b}'.format(int(A)))
            return int(binary.count('1'))
        else:
            return 0 #error
