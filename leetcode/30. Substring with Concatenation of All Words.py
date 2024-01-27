class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []


        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_dict = Counter(words)
        result = []

        for i in range(word_len):
            left, right = i, i
            current_dict = Counter()

            while right + word_len <= len(s):
                current_word = s[right:right + word_len]
                right += word_len

                if current_word in word_dict:
                    current_dict[current_word] += 1

                    while current_dict[current_word] > word_dict[current_word]:
                        current_dict[s[left:left + word_len]] -= 1
                        left += word_len

                    if right - left == total_len:
                        result.append(left)

                else:
                    current_dict.clear()
                    left = right

            current_dict.clear()

        return result