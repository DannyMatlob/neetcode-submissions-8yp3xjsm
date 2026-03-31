class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        reqToCourses = defaultdict(list)
        ingressMap = defaultdict(int)
        for a, b in prerequisites:
            reqToCourses[b].append(a)
            ingressMap[a] += 1 
        
        queue = deque()
        for i in range(numCourses):
            if ingressMap[i] == 0:
                res.append(i)
                queue.append(i)
    
        print(queue)
        while queue:
            for i in range(len(queue)):
                req = queue.popleft()
                for course in reqToCourses[req]:
                    ingressMap[course] -= 1
                    if ingressMap[course] <= 0:
                        res.append(course)
                        queue.append(course)

        for course in ingressMap:
            if ingressMap[course] > 0: return []
        
        return res

