class Solution:
    b = False
    def isPalindrome(self, s: str) -> bool:
        string = s
        string = string.lower()
        l = []
        for j in string:
            l.append(j)
        i = 0
        while i >= 0 and i < len(l):
            if l[i].isalnum() == False or l[i] == " ":
                l.pop(i)
                i = i-2
            i = i + 1

        if l == []:
            b = True
            return b

        if l == "" or l == None:
            b = True
            return b

        len_of_list = len(l)
        for a in range(len_of_list):
            print(a)
            if l[a] == l[len_of_list-1-a]:
                b = True
            else:
                b = False
                return b
        if b == True:
            return b

test = Solution()
print(test.isPalindrome("\"Stop!\" nine myriad murmur. \"Put up rum, rum, dairymen, in pots.\""))