class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visit = set()
        directions = [[0,1], [1, 0], [0, -1], [-1, 0]]
        index = 0
        x, y = 0, 0
        m = len(matrix)
        n = len(matrix[0])
        squares = m * n
        res = []
        res.append(matrix[0][0])
        visit.add((0,0))
        while (len(visit) < squares):
            x1 = x + directions[index][0]
            y1 = y + directions[index][1]
            if (x1, y1) in visit or (x1 < 0) or (x1 >= m) or (y1 < 0) or (y1 >= n):
                index = (index + 1) % 4
                x1 = x + directions[index][0]
                y1 = y + directions[index][1]
            res.append(matrix[x1][y1])
            print(res)
            visit.add((x1, y1))
            x, y = x1, y1
        return res