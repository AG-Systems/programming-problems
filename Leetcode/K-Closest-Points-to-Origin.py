class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if points == None or points == []:
            return []
        
        import heapq
        import math
        
        def get_distance(x,y):
            x = x ** 2
            y = y ** 2
            return math.sqrt(x + y)
        
        heap = []
        heapq.heapify(heap)
        
        for point in points:
            distance = get_distance(point[0], point[1])
            heapq.heappush(heap, (distance, [point[0], point[1]]))
        
        answer = []
        temp = heapq.nsmallest(K, heap)
        for val in temp:
            answer.append(val[1])
        return answer
