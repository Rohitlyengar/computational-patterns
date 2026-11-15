class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        index = {}

        for i in range(len(nums)):
            index[nums[i]] = 1 + index.get(nums[i], 0)

        heap = []
        for key, value in index.items():
            heapq.heappush_max(heap, (value, key))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop_max(heap)[1])
        
        return res
