class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        container = {}
        l = []
        for x in list1:
            container[x] = 1
        for x in list2:
            if x in container:
                container[x] = 0
        for key,val in container.items():
            if val == 0:
                l.append(key)
        if len(l) == 1:
            return l
        else:
            container = {}
            for x in l:
                index1 = list1.index(x)
                index2 = list2.index(x)
                container[x] = index1 + index2
            index = []
            for key,val in container.items():
                if val not in index:
                    index.append(val)
            if len(index) == 1:
                return l
            min_val = float('inf')
            common = ""
            for key,val in container.items():
                if min_val > val:
                    min_val = val
                    common = key
            return [common]
            
                
