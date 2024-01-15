class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = r = 0
        res = 0
        while r < len(nums):
            fathers = 0 
            for i in range(l,r + 1):   ## r + 1 -> to include r in the loop
                fathers = i+nums[i] if i + nums[i] > fathers else fathers
            l = r + 1
            r = fathers
            res += 1
        return res





