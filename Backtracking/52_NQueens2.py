class Solution:
    def totalNQueens(self, n: int) -> int:
        solutions = 0

        col = set()
        row = set()
        diag = set()
        ndiag = set()
        sol = []

        def solve(r):
            nonlocal solutions
            if r == n:
                solutions += 1
                return
            if r in row:
                return
            row.add(r)
            for i in range(n):
                d = r - i
                nd = (n - 1 - r) - i
                if (i not in col) and (d not in diag) and (nd not in ndiag):
                    col.add(i)
                    diag.add(d)
                    ndiag.add(nd)
                    solve(r+1)
                    col.remove(i)
                    diag.remove(d)
                    ndiag.remove(nd)
            row.remove(r)
        
        solve(0)

        return solutions