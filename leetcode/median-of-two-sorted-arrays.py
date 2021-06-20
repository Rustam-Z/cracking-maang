import numpy as np

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = sorted(nums1 + nums2)

        return np.median(np.array(nums3))



sol = Solution()
nums1 = [1,3]
nums2 = [2]
print(sol.findMedianSortedArrays(nums1, nums2))