class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache = {}
        def fib_helper(N, cache):
            if N in cache:
                return cache[N]
            
            result = None
            if N < 2:
                result = N
            else:
                result = fib_helper(N - 2, cache) + fib_helper(N - 1, cache)
            
            cache[N] = result
            return result
        
        return fib_helper(N, cache)
