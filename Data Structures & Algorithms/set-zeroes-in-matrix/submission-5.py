class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # Step 1: Determine which rows/cols need to be zeroed
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # Mark column
                    if r > 0:
                        matrix[r][0] = 0 # Mark row
                    else:
                        rowZero = True

        # Step 2: Use markers to fill the inner part of the matrix
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Step 3: Zero out the first column if the origin marker is 0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # Step 4: Zero out the first row if rowZero is True
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0