class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] > 0:
                return 0
            else:
                return -1
            
        import heapq
        
        heap = []
        heapq.heapify(heap)
        
        for index in range(0, len(nums)):
            heapq.heappush(heap, (nums[index], {"index": index}))
        
        temp = heapq.nlargest(2, heap)
        if (temp[0][0] / 2) >= temp[1][0]:
            return temp[0][1]["index"]
        else:
            return -1
            
