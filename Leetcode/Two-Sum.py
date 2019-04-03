class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        container = {}
        indices = []
        for x in nums:
            if x in container:
                container[x] = target-x
            else:
                container[x] = target-x
        for key,val in container.items():
            if val in nums:
                indices.append(nums.index(key))
                if key != val:
                    indices.append(nums.index(val))
                else:
                    nums[nums.index(key)] = -99
                    indices.append(nums.index(val))
                break
        return indices

    
"""
# BETTER SOLUTION
class Solution(object):
    def twoSum(self, nums, target):        
        container = {}
        
        counter = 0
        
        for num in nums:
            if num in container:
                container[num]["index"].append(counter)
            else:
                diff = target - num
                container[num] = { 
                    "diff": diff,
                    "index": [counter]
                }
            counter += 1
        
        for key,val in container.items():
            data = val
            if data["diff"] in container and data["diff"] + key == target:
                if data["diff"] != key:
                    index1 = data["index"][0]
                    index2 = container[data["diff"]]["index"][0]
                    return [index1, index2]
                else:
                    index1 = data["index"][0]
                    index2 = data["index"][1]
                    return [index1, index2]
"""
