ascii_dict = dict()
ascii_in_number = range(0,256)
# for i in ascii_in_number:
#     ascii_dict[str(i)] = chr(i)

class Solution:
    def scoreOfString(self, s):
        sum_of_numbers = 0
        for j in range(len(s)-1):
            # print(s[j])
            # print(s[j+1])
            # print(ord(s[j]))
            # print(ord(s[j+1]))
            new_number = ord(s[j]) - ord(s[j+1])
            if new_number < 0:
                new_number += ((-2) * (ord(s[j]) - ord(s[j+1])))
            # print("Total number is " + str(new_number))
            sum_of_numbers += new_number
        return sum_of_numbers
    
test = Solution()
print(test.scoreOfString(""))