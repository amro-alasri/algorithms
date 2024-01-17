class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        n = len(ratings)
        candies = [1] * n
        
        # Iterate from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Iterate from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Sum up the candies array
        total_candies = sum(candies)
        
        return total_candies


# Example 1
ratings1 = [1, 0, 2]
output1 = min_candies(ratings1)
print("Example 1 Output:", output1)

# Example 2
ratings2 = [1, 2, 2]
output2 = min_candies(ratings2)
print("Example 2 Output:", output2)
