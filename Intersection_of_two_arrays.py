class Solution:
    def intersection(self, nums1, nums2):
        leng1 = len(nums1)
        leng2 = len(nums2)
        a = 0
        ls = []
        if leng1 < leng2:
            for i in range(0, leng2):
                if nums2[i] == nums2[a]:
                    ls.append(nums2[a])
                    a += 1
            if ls == nums2:
                for j in range(0, len(ls)-2):
                    if ls[j] == ls[j+1]:
                        ls1.append()            