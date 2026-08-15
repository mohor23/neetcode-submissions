class MedianFinder:
    import heapq
    def __init__(self):
        self.left=[]
        self.right=[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left,-num)
        if self.left and self.right and -self.left[0]>self.right[0]:
            n=-heapq.heappop(self.left)
            heapq.heappush(self.right,n)
        if len(self.left)>len(self.right)+1:
            n=-heapq.heappop(self.left)
            heapq.heappush(self.right,n)
        if len(self.right)>len(self.left)+1:
            n=heapq.heappop(self.right)
            heapq.heappush(self.left,-n)

    def findMedian(self) -> float:
        if len(self.left)>len(self.right):
            return -self.left[0]
        elif len(self.right)>len(self.left):
            return self.right[0]
        else:
            return (-self.left[0]+self.right[0])/2
        
        