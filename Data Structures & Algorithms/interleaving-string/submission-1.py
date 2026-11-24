class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        def DFS(i: int, j: int) -> bool:
            if i + j == len(s3):
                return True
            
            if i < len(s1) and s1[i] == s3[i + j] and DFS(i + 1, j):
                return True
            
            if j < len(s2) and s2[j] == s3[i + j] and DFS(i, j + 1):
                return True
            
            return False
        
        return DFS(0, 0)
        