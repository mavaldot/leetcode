class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRow = set()
        zeroCol = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroRow.add(i)
                    zeroCol.add(j)
                    print(zeroCol)
            
        for i in range(len(matrix)):
            if i in zeroRow:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

        for j in range(len(matrix[0])):
            if j in zeroCol:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        
        print(zeroRow)