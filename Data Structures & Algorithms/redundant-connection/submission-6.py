class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(p1):
            if p1 != par[p1]:
                par[p1] = find(par[p1])
            return par[p1]

        def union(p1, p2):
            if find(p1) == find(p2):
                return False
            par[find(p2)] = find(p1)
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return [0, 0]
