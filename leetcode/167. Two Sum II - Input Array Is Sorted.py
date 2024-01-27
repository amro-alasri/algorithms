class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]  # Indices are 1-based, so add 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

# add the use cases
numbers1 = [2, 7, 11, 15]
target1 = 9
s = Solution()
result1 = s.twoSum(numbers1, target1)
print(result1)  # Output: [1, 2]

numbers2 = [2, 3, 4]
target2 = 6
result2 = s.twoSum(numbers2, target2)
print(result2)  # Output: [1, 3]

numbers3 = [-1, 0]
target3 = -1
result3 = s.twoSum(numbers3, target3)
print(result3)  # Output: [1, 2]                