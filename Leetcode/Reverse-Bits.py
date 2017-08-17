class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        counter = 0
        mask = 1
        for x in xrange(32):
            if n & mask:
                counter += 1
            if x != 31:
                counter <<= 1
            mask <<= 1
        return counter
