class Solution(object):
    def calc(self, container, z):
        if container[z] != -1:
            return container[z]
        if z <= 2:
            container[z] = z
            return container[z]
        container[z] = self.calc(container,z-1) + self.calc(container,z-2)
        return container[z]
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        container = [-1]
        for x in range(0,n):
            container.append(-1)
        return self.calc(container, n)

        
