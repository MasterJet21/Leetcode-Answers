class Solution:
    def divideString(self, s, k, fill):
        i = 0
        ans = []
        while i < len(s):
            chunk = s[i:i+k]
            if len(chunk) < k:
                chunk += fill * (k-len(chunk))

            ans.append(chunk)

            i += k

        return ans
        

test = Solution()
test.divideString("ctoyjrwtngqwt",8,"n")