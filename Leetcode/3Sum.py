class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from random import shuffle
        container = list(itertools.combinations(nums,3))
        sum_container = []
        #print list(itertools.combinations(nums,3))
        for x in container:
            str(x).strip('()')
            if sum(x) == 0:
                temp = list(x)
                temp.sort()
                if temp not in sum_container:
                    sum_container.append(list(temp))
        #sum_container = [list(x) for x in {(tuple(e)) for e in sum_container}]
        return sum_container
