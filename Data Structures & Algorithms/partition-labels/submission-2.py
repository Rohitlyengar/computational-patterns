class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = {}
        res = []

        for i, c in enumerate(s):
            index[c] = i
        
        start = 0
        end = index[s[i]]
        for i in range(len(s)):
            if i == end:
                res.append(end - start)
                start = end
            

        return res        
