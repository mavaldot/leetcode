class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        row = [1,1]

        for i in range(2, rowIndex+1):
            newRow = [1] * (i + 1)
            for j in range(1, i):
                newRow[j] = row[j-1] + row[j]
            row = newRow
        
        return row