class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while heap:
            print(heap)
            s1 = -heapq.heappop(heap)
            if len(heap) == 0:
                return s1
            s2 = -heapq.heappop(heap)

            if s1 > s2:
                heapq.heappush(heap, -(s1 - s2))
            
        return 0