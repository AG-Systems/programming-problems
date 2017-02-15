class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        counter = 0
        while counter < len(nums):
            temp = list(nums)
            del temp[counter]
            x = str(temp)
            mul_nums = x.replace(',','*')
            product = eval(mul_nums)
            product = str(product).replace("[","")
            product = str(product).replace("]","")
            output.append(int(product))
            counter += 1
        return output
             
