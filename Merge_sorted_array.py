class Solution:
    def merge(self, nums1, m, nums2, n):
        # """
        # Do not return anything, modify nums1 in-place instead.
        # """
        midx = m -1
        nidx = n -1
        right = m+n-1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1

            right -= 1
        return nums1

test = Solution()
print(test.merge([-1,0,0,3,3,3,0,0,0],6,[1,2,2],3))