class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap=[]
        for p in points:
            x=p[0]
            y=p[1]
            dist=x*x+y*y
            heapq.heappush(heap,(-dist,p))
            if len(heap)>k:
                heapq.heappop(heap)
        return [p[1] for p in heap]
