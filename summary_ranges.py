class Solution:
    def summaryRanges(self, nums):
      res = []
      if not nums:
         return res
      
      start = nums[0]
      end = nums[0]
      
      for i in nums[1:]:
         if i == end + 1:
            end = i
         else:
            if start == end:
               res.append(str(start))
            else:
               res.append(str(start)+"->"+str(end))
            start = i
            end = i

      if start == end:
         res.append(str(start))

      else:
         res.append(str(start)+"->"+str(end))

      return res

test = Solution()
# test.summaryRanges([0,1,2,4,5,7])
test.summaryRanges([0,2,3,4,6,8,9])
# Output ["0->2","4->5","7"]