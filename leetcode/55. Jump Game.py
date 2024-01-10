class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        last = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last:
                last = i

        return True if last == 0 else False


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2,3,1,0,4]))
    print(s.canJump([2,3,1,0, 0,4]))

                