class Solution:
    def wordPattern(self, pattern, s):
        s_list = s.split()
        diction = {}
        pattern_list = []

        for l in pattern:
            pattern_list.append(l)

        if len(pattern_list) != len(s_list):
            return False

        for j in range(0, len(pattern)):
            if pattern[j] not in diction and s_list[j] not in diction.values():
                diction.update({pattern[j]:s_list[j]})

        print(diction)

        for i in s_list:
            if i not in diction.values():
                return False

        for k in range(0, len(pattern)):
            if pattern[k] in diction:
                key = pattern[k]
                if s_list[k] != diction[key]:
                    return False
            else:
                return False

        return True

test = Solution()
print(test.wordPattern("abba", "dog dog dog dog"))
print(test.wordPattern("abba", "dog cat cat dog"))
print(test.wordPattern("abba", "dog cat cat fish"))
print(test.wordPattern("aba", "dog cat cat"))
"dog cat cat"
# s_list contains ALL the elements in s
# dictionary.value() gives the VALUES related to all the UNIQUE keys