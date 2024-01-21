class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
          return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

            return -1

s = Solution()
haystack1 = "sadbutsad"
needle1 = "sad"
output1 = s.strStr(haystack1, needle1)
print(output1)

haystack2 = "leetcode"
needle2 = "leeto"
output2 = s.strStr(haystack2, needle2)
print(output2)        