class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []

        m = len(heights[0])
        n = len(heights)

        def searchOcean(i, j, oceans, visited, prevH):
            
            if (i,j) in visited: return
            if i < 0 or j < 0:
                oceans[0] = True
                return
            if j >= m or i >= n:
                oceans[1] = True
                return
            h = heights[i][j]
            if h > prevH:
                return
            visited.add((i,j))
            searchOcean(i+1, j, oceans, visited, h)
            searchOcean(i, j+1, oceans, visited, h)
            searchOcean(i-1, j, oceans, visited, h)
            searchOcean(i, j-1, oceans, visited, h)
        
        for i in range(0, n):
            for j in range(0, m):
                reached = [False, False]
                visit = set()
                searchOcean(i, j, reached, visit, float("inf"))
                if reached[0] and reached[1]:
                    res.append([i,j])

        return res