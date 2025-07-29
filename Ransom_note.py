class Solution:
    @staticmethod
    def removefirstoccurence(original, old, new):
        index = original.find(old)
        if index != -1:
            return original[:index] + new + original[index+len(old):]
        else:
            return original
            
    def canConstruct(self, ransomNote, magazine):
        check = True
        if len(ransomNote) == 0:
            return True
        for i in ransomNote:
            if i in magazine:
                indexofcommonmagazine = magazine.find(i)
                indexofcommonransomenote = ransomNote.find(i)
                magazine = self.removefirstoccurence(magazine,magazine[indexofcommonmagazine],"")
                ransomNote = self.removefirstoccurence(ransomNote,ransomNote[indexofcommonransomenote],"")
                check = True
            else:
                check = False

        if len(ransomNote) != 0:
            check = False
            return check
        
        else:
            check = True
            return check
    
test = Solution()
print(test.canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))