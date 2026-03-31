class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list[int])
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = [0] * n
        visited[0] = 1
        queue = deque()
        queue.append([0,-1])

        while queue:
            for i in range(len(queue)):
                node, parent = queue.popleft()
                print(node, parent)
                print(visited)
                for neighbor in adj[node]:
                    if neighbor is not parent:
                        visited[neighbor] += 1
                        if visited[neighbor] > 1: return False
                        queue.append([neighbor, node])
        
        for i in visited:
            if i != 1: return False
        return True


