class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        import itertools
        container = []
        l = [A,B,C,D]
        l = list(itertools.product(*l))
        #print l
        for x in l:
            if len(x) == 4 and sum(x) == 0:
                container.append(x)
        return len(container)
