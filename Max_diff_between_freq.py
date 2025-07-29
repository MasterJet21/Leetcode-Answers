class Solution:
    def maxDifference(self, s):
        d = {}
        a = 1
        for i in s:
            if i not in d:
                d.update({i: a})
            else:
                d.update({i: d[i]+1})

        print(d)
        even_ls = []
        odd_ls = []

        for j in d.values():
            if j % 2 == 0:
                even_ls.append(j)
            else:
                odd_ls.append(j)
        
        odd_ls = sorted(odd_ls, reverse= True)
        even_ls = sorted(even_ls, reverse= False)
        print(odd_ls)
        print(even_ls)
        return (odd_ls[0]-even_ls[0])

test = Solution()
test.maxDifference("mmsmsym")