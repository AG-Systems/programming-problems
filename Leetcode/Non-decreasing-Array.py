class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        counter = 0
        for x in range(0,len(nums)-1):
            if nums[x] > nums[x+1]:
                counter += 1
        if counter <= 1:
            if len(nums[0:(nums.index(min(nums)))]) > 1:
                return False
            else:
                return True
        else:
            return False
        """
        list1 = list(nums)
        list2 = list(nums)
        for x in range(0,len(nums)-1):
            if nums[x] > nums[x+1]:
                list1[x] = nums[x + 1]
                list2[x+1] = nums[x]
                break
        #print(list1,list2)
        if list1 == sorted(list1):
            return True
        elif list2 == sorted(list2):
            return True
        else:
            return False
