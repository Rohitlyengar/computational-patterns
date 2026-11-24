class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        
        res = 1
        for _ in range(abs(n)):
            res = res * x
        
        if n > 0:
            return res
        else:
            return 1 / res
