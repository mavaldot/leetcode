class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        row = 0
        while row < n:
            for i in range(row, n):
                matrix[row][i], matrix[i][row] = matrix[i][row], matrix[row][i] 
            row += 1

        for r in matrix:
            r.reverse()

        print(matrix)