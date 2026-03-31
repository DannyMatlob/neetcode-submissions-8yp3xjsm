class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            # Base case: Out of bounds or not an 'O'
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            
            # Mark as safe
            board[r][c] = "T"
            
            # Explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Start DFS from "O"s on the border
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS-1] or c in [0, COLS-1]) and board[r][c] == "O":
                    dfs(r, c)

        # 2. Re-traverse and flip
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X" # Captured
                elif board[r][c] == "T":
                    board[r][c] = "O" # Rescued