class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            # Calculate the width of the container
            width = right - left

            # Calculate the height of the container
            h = min(height[left], height[right])

            # Update the maximum area if a larger one is found
            max_area = max(max_area, width * h)

            # Move the pointers towards each other
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area