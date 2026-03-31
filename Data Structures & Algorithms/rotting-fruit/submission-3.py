class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh+=1
    
        def checkNode(i, j) -> int:
            if (i < 0 or 
            i >= len(grid) or 
            j < 0 or 
            j >= len(grid[0]) or 
            grid[i][j] == 0):
                return 0
            
            if grid[i][j] == 1:
                grid[i][j] = 2
                return 1
            return 0
        
        minutes = -1
        while queue:
            for n in range(len(queue)):
                i, j = queue.popleft()

                up = checkNode(i-1, j)
                down = checkNode(i+1, j)
                right = checkNode(i, j+1)
                left = checkNode(i, j-1)

                if up == 1:
                    queue.append((i-1, j))
                if down == 1:
                    queue.append((i+1, j))
                if right == 1:
                    queue.append((i, j+1))
                if left == 1:
                    queue.append((i, j-1))
                
                fresh-= (up + down + left + right)

            minutes+=1

        if fresh == 0:
            return max(minutes, 0)
        return -1
                
