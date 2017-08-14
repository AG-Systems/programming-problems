class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        container = {}
        counter = 0
        for x in A:
            for z in B:
                answer = z + x
                if answer in container:
                    container[answer] += 1
                else:
                    container[answer] = 1
        for x in C:
            for z in D:
                answer = -(x + z)
                if answer in container:
                    counter += container[answer]
        return counter
                    
                    
        """
        def fourSumCount(self, A, B, C, D):
            AB = collections.Counter(a+b for a in A for b in B)
            return sum(AB[-c-d] for c in C for d in D)
        
        Super clever solution
        """
        
        
