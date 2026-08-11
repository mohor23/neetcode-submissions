class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        heap=[]
        seen=Counter(nums)
        for item, val in seen.items():
            heapq.heappush(heap,(val,item))
            if len(heap)>k:
                heapq.heappop(heap)
        return [item for value,item in heap]
