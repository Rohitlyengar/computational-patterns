class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0

        def DFS(i: int, curr: int) -> None:
            nonlocal res
            if curr == amount:
                res += 1
                return

            if i >= len(coins) or curr > amount:
                return

            DFS(i, coins[i] + curr)

            DFS(i + 1, curr)
        
        DFS(0, 0)
        return res
        