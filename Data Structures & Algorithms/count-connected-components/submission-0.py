class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list[int])
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        def bfs(n):
            q = deque()
            q.append(n)
            while q:
                node = q.popleft()
                visited[node] = 1

                for neighbor in adj[node]:
                    if visited[neighbor] != 1:
                        q.append(neighbor)

        visited = [0] * n
        res = 0
        for i in range(n):
            if visited[i] == 0:
                res+=1
                bfs(i)
        return res