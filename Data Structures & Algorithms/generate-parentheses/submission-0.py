class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        subset = []
        res = []

        def DFS(openN: int, closedN: int) -> None:
            if openN == closedN == n:
                res.append("".join(subset))
                return
            
            if openN < n:
                subset.append('(')
                DFS(openN + 1, closedN)
                subset.pop()
            
            if closedN < openN:
                subset.append(')')
                DFS(openN, closedN + 1)
                subset.pop()
            
        DFS(0, 0)
        return res
