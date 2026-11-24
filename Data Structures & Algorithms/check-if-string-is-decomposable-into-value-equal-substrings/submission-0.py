class Solution:
    def isDecomposable(self, s: str) -> bool:
        index = {}

        for c in s:
            index[c] = 1 + index.get(c, 0)
        
        two = False

        for key, value in index.items():
            if not two and value == 2:
                two = True
            elif value == 3:
                pass
            else:
                return False
        
        return two
