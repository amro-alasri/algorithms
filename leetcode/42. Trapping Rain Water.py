class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 2:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        water_trapped = 0
        for i in range(1, n - 1):
            min_height = min(left_max[i], right_max[i])
            water_trapped += max(0, min_height - height[i])

        return water_trapped

# Example usage:
solution = Solution()
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(solution.trap(height1))  # Output: 6

height2 = [4, 2, 0, 3, 2, 5]
print(solution.trap(height2)) # Output: 9
