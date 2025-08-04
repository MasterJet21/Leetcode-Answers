class Solution:
    def hIndex(self, citations):
        right = len(citations)-1
        h_index = 0
        citations = sorted(citations, reverse=False)
        check = True
        while check is True:
            if citations[right] >= len(citations[right:]) and right >= 0:
                h_index += 1
                right -= 1
            else:
                check = False
        return h_index

test = Solution()
print(test.hIndex([1]))