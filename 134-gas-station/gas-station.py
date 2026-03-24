class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        currgas = 0
        startidx = 0
        for i in range(len(gas)):
            currgas+=(gas[i] - cost[i])
            if currgas < 0:
                currgas = 0
                startidx = i+1
        
        return startidx
        
        