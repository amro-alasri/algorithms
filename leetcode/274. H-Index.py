class Solution(object):
    def hIndex(self, citations):
        citations = sorted(citations)  # Sort citations in ascending order.
        n = len(citations)
        
        for i in range(n - 1, -1, -1):
            if citations[i] >= n - i:
                return n - i  # Return the H-Index when the condition is met.
        
        return 0  # Return 0 if no suitable H-Index is found.

# Example usage:
solution = Solution()
print(solution.hIndex([3, 0, 6, 1, 5]))  # Output: 3
print(solution.hIndex([1, 3, 1]))         # Output: 1
