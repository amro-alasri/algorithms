class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the string into words
        words = s.split()

        # Reverse the order of words
        reversed_words = words[::-1]

        # Join the reversed words into a string with a single space between them
        result = ' '.join(reversed_words)

        return result
        