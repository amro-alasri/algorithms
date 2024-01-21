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