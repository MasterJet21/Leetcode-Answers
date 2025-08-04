class Solution:
    def canCompleteCircuit(self, gas, cost):
        current_tank = 0
        total_gain = 0
        start_index = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total_gain += gain
            current_tank += gain
        
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
            
        return start_index if total_gain >= 0 else -1

test = Solution()
test.canCompleteCircuit([5,1,2,3,4],[4,4,1,5,1])