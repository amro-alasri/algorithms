class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result, cur, num_of_letters = [], [], 0
    
        for word in words:
            if num_of_letters + len(word) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                
                result.append(''.join(cur))
                cur, num_of_letters = [], 0

            cur += [word]
            num_of_letters += len(word)

        result.append(' '.join(cur).ljust(maxWidth))
        return result


# Example usage:
s = Solution()
words1 = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth1 = 16
output1 = s.fullJustify(words1, maxWidth1)
print(output1)

words2 = ["What","must","be","acknowledgment","shall","be"]
maxWidth2 = 16
output2 = s.fullJustify(words2, maxWidth2)
print(output2)

words3 = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth3 = 20
output3 = s.fullJustify(words3, maxWidth3)
print(output3)