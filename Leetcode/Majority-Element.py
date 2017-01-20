class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        max = 0
        characters = {}
        for z in nums:
            if z in characters:
                characters[z] +=1
            else:
                characters[z] = 1
        for x in range(0,len(characters.keys())):
            if characters.values()[x] > counter:
                max = characters.keys()[x]
                counter = characters.values()[x]
        return max
            
