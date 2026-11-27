class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def DFS(i: int, curr: str) -> None:
            if i >= len(digits):
                res.append(curr)
                return
            
            for c in digitToChar[digits[i]]:
                DFS(i + 1, curr + c)
        
        if digits:
            DFS(0, str())

        return res
