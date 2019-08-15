class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jeweltable = {}
        for jewel in J:
            jeweltable[jewel] = True
        
        ownership_jewels = 0
        
        for stone in S:
            if stone in jeweltable:
                ownership_jewels += 1
        return ownership_jewels
