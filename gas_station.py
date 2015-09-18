#gas stations are on a circle
#gas = amount of gas supplied by each station i 
#cost = amount of gas will be costed by driving from station i to (i+1)
#return -1 if can't finish a cycle, otherwise return the start station index
class gas_station_Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # calculate cumulative sum of (gas-cost) at each point
        # if the total sum of (gas-cost) < 0 -> can't finish this journey
        # otherwise, start with the minimum point
        min_ = 0
        min_index = 0
        cur = 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if cur < min_:
                min_ = cur
                min_index = i+1
        
        if cur < 0 :
            return -1
        else:
            return min_index
