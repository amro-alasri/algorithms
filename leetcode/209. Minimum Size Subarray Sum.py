class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        min_length = float('inf')
        current_sum = 0

        while right < len(nums):
            current_sum += nums[right]
            right += 1

            while current_sum >= target:
                min_length = min(min_length, right - left)
                current_sum -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length

# add the use cases:
target1, nums1 = 7, [2, 3, 1, 2, 4, 3]
s = Solution()
result1 = s.minSubArrayLen(target1, nums1)
print(result1)  # Output: 2

target2, nums2 = 4, [1, 4, 4]
result2 = s.minSubArrayLen(target2, nums2)
print(result2)  # Output: 1

target3, nums3 = 11, [1, 1, 1, 1, 1, 1, 1, 1]
result3 = s.minSubArrayLen(target3, nums3)
print(result3)  # Output: 0        