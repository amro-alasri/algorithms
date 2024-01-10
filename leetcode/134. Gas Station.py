# 134. Gas Station

# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_gas = 0
        current_gas = 0
        start_index = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                current_gas = 0
                start_index = i + 1

        
        return start_index if total_gas >= 0 else -1


solution_instance = Solution()
gas_stations = [1, 2, 3, 4, 5]
travel_cost = [3, 4, 5, 1, 2]
result = solution_instance.canCompleteCircuit(gas_stations, travel_cost)

print("Starting gas station index:", result) 

# print(np.concatenate((np.array([2,35]),np.array([2,35]))))