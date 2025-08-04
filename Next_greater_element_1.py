class Solution:
    def nextGreaterElement(self, nums1, nums2):
        if len(nums1) < len(nums2):
            for i in nums1:
                