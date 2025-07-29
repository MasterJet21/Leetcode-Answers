class Solution:
    def findRelativeRanks(self, score):
        sorted_ls = []
        d = {}
        a = 1
        for i in score:
            sorted_ls.append(i)
        sorted_ls = sorted(sorted_ls, reverse=True)

        for j in score:
            d.update({a: j})
            a += 1

        if len(score) <= 1:
            score[0] = "Gold Medal"
            return score
        
        if len(score) == 2:
            for l in range(len(score)):
                if score[l] > score[l+1]:
                    score[l] = "Gold Medal"
                    score[l+1] = "Silver Medal"
                else:
                    score[l+1] = "Gold Medal"
                    score[l] = "Silver Medal"
                return score

        for k in d.values():
            if k == sorted_ls[0]:
                score[score.index(k)] = "Gold Medal"

            if k == sorted_ls[1]:
                score[score.index(k)] = "Silver Medal"

            if k == sorted_ls[2]:
                score[score.index(k)] = "Bronze Medal"

        b = 4
        if len(score) > 3:
            for u in sorted_ls[3:]:
                score[score.index(u)] = str(b)
                b += 1

        return(score)

test = Solution()
test.findRelativeRanks([5,7,3,2,1])