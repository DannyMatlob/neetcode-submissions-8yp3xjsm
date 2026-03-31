class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.res = True
        preMap = defaultdict(list)
        for a, b in prerequisites:
            preMap[b].append(a)
        
        def dfs(key, visited):
            print("searching", key)
            print("visited: ", visited)
            if (key in visited):
                print("setting res to false")
                self.res = False
                return

            visited.append(key)
            for adj in preMap[key]:
                dfs(adj, visited)
            visited.pop()
            
        for key in list(preMap.keys()):
            dfs(key, [])

        return self.res