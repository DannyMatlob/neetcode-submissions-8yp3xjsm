class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, dst, ti in times:
            adj[src].append((dst, ti))
        
        timeToReachNode = {k: 0}
        queue = deque([k])

        while queue:
            cur = queue.popleft()
            curTi = timeToReachNode[cur]
            for dst, ti in adj[cur]:
                newTime = curTi + ti
                if dst not in timeToReachNode or timeToReachNode[dst] > newTime:
                    timeToReachNode[dst] = newTime
                    queue.append(dst)  # enqueue on any improvement
        
        if len(timeToReachNode) == n:
            return max(timeToReachNode.values())
        return -1