class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, dst, ti in times:
            adj[src].append((dst, ti))
        
        timeToReachNode = {}
        heap = [(0, k)]  # (time, node)

        while heap:
            curTi, cur = heapq.heappop(heap)
            if cur in timeToReachNode:  # already settled, skip
                continue
            timeToReachNode[cur] = curTi
            for dst, ti in adj[cur]:
                if dst not in timeToReachNode:
                    heapq.heappush(heap, (curTi + ti, dst))
        
        if len(timeToReachNode) == n:
            return max(timeToReachNode.values())
        return -1