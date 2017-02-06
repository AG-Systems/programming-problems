class Solution(object):
    def helper(self,prices,container, index):
        if index == len(prices)-1:
            return container
        container.append(0)
        highest = min(prices)
        for x in range(index+1,len(prices)):
            result = prices[index] - prices[x]
            if result < highest:
                container[index] = result
                highest = result
        return self.helper(prices,container,index+1)
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        if len(prices) == 0:
            return 0
        container = []
        counter = 0
        r = self.helper(prices,container,counter)
        print(r)
        for c in r:
            if c < 0:
                z = abs(min(r))
                return z
        return 0
