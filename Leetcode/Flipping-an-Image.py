class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for x in range(len(A)):
            A[x] = A[x][::-1]
            for z in range(len(A)):
                if A[x][z] == 1:
                    A[x][z] = 0
                else:
                    A[x][z] = 1
        return A
