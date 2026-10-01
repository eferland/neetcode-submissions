class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.size = k
        for num in nums:
            heapq.heappush(self.minheap, num)
            if len(self.minheap)==self.size+1:
                heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap)==self.size+1:
                heapq.heappop(self.minheap)
        return self.minheap[0]
