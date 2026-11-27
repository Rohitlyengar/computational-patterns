class Solution:
    def isPali(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def DFS(i: int) -> None:
            if i >= len(s):
                res.append(subset[:])
                return
            
            for j in range(i, len(s), 1):
                if self.isPali(s, i, j):
                    subset.append(s[i : j + 1])
                    DFS(j + 1)
                    subset.pop()
        
        DFS(0)
        return res
    