class Solution(object):
    def hIndex(self, citations):
        citations = sorted(citations,reverse=True)

        n = len(citations) 
        for i in range(n):
            if citations[i] < i + 1:
                return i 

        return n

