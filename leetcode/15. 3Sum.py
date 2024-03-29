class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # Skip duplicates to avoid duplicate triplets
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                
                if total_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left-1]:
                        left += 1  # Skip duplicates
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1  # Skip duplicates
                
                elif total_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result


# add the use cases 

nums1 = [-1, 0, 1, 2, -1, -4]
s = Solution()
print(s.threeSum(nums1))  # Output: [[-1, -1, 2], [-1, 0, 1]]

nums2 = [0, 1, 1]
print(s.threeSum(nums2))  # Output: []

nums3 = [0, 0, 0]
print(s.threeSum(nums3))  # Output: [[0, 0, 0]]        