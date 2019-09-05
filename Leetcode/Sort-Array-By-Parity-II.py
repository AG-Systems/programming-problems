class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        pointer = 1
        for x in range(0, len(A), 2):
            if A[x] % 2:
                while A[pointer] % 2:
                    pointer += 2
                A[x], A[pointer] = A[pointer], A[x]
        
        return A
