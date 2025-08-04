# Last index must be an even number
# First index cannot be a zero (If there is even a zero in digits)

# This only gives you combinations like [1, 2, 3], but not permutations like [2, 1, 3], [3, 2, 1], etc.

# But the question expects all permutations of 3 digits with no repeats, no leading 0, and ending in an even digit.

# class Solution:
#     def findEvenNumbers(self, digits):
#         even_numbers = []
#         possibilities = []
#         for i in range(len(digits)):
#             for j in range(i + 1, len(digits)):
#                 for k in range(j + 1, len(digits)):
#                     if digits[k] % 2 == 0 and digits[i] != 0:
#                         even_numbers.append([digits[i], digits[j], digits[k]])

#         possibilities = [int(''.join(str(d) for d in u)) for u in even_numbers]
        
#         return possibilities

# This accounts for all permutations of 3 digits with no repeats, no leading 0, and ending in an even digit.

class Solution:
    def findEvenNumbers(self, digits):
        n = len(digits)
        possibilities = set()
        possibilities1 = []
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if digits[k] % 2 != 0:
                        continue
                    if j == k or i == k:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    possibilities.add(num)
        
        for l in possibilities:
            possibilities1.append(l)
        
        return sorted(possibilities1)

test = Solution()
print(test.findEvenNumbers([2,1,3,0]))

# | Optimization                                  | Impact                                   |
# | --------------------------------------------- | ---------------------------------------- |
# | `continue` early                              | Cuts unnecessary loops                   |
# | `set()` directly                              | No need for `append + set()` later       |
# | Integer construction (`a * 100 + b * 10 + c`) | Faster than `str()` + `join()` + `int()` |
# | Skips sorting until the end                   | Keeps main loop fast                     |
