class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def DFS(i: int, buying: bool) -> int:
            if i >= len(prices):
                return 0
            
            if buying:
                buy = DFS(i + 1, False) - prices[i]
                cooldown = DFS(i + 1, True)
                return max(buy, cooldown)
            else:
                sell = DFS(i + 2, True) + prices[i]
                cooldown = DFS(i + 1, True)
                return max(sell, cooldown)
        return DFS(0, True)
