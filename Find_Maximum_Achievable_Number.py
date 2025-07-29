class Solution:
    def theMaximumAchievableX(self, num, t):
        self.num = num
        self.t = t
        t = t * 2
        x = 0
        x = x + (num + t)
        return x