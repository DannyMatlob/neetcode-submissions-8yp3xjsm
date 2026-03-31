class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(p1):
            if p1 != par[p1]:
                par[p1] = find(par[p1])
            return par[p1]

        def union(p1, p2):
            root1 = find(p1)
            root2 = find(p2)
            if root1 == root2:
                return False
            
            if rank[root1] > rank[root2]:
                par[root2] = root1
                rank[root1] += rank[root2]
            else:
                par[root1] = root2
                rank[root2] += rank[root1]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return [0, 0]
