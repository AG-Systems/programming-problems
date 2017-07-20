class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1) + len(nums2) ) % 2 == 0:
            #even
            print "even"
            nums1.extend(nums2)
            nums1.sort()
            print nums1
            return  (nums1[len(nums1)/2 - 1] + nums1[len(nums1)/2]) / 2.0
            pass
        else:
            #odd
            print "odd"
            nums1.extend(nums2)
            nums1.sort()
            print nums1
            return nums1[len(nums1)/2]
            
            pass
