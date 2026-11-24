class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            heapq.heappush_max(stones, abs(heapq.heappop(stones) - heapq.heappop(stones)))
        return stones[0]
        