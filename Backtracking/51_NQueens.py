class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        col = set()
        row = set()
        diag = set()
        ndiag = set()
        sol = []

        def solve(r, arr):
            if r == n:
                sol.append(arr)
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
                    s = "." * i + "Q" + "." * max(0, n - 1 - i)
                    arr.append(s)
                    solve(r+1, arr[:])
                    arr.pop()
                    col.remove(i)
                    diag.remove(d)
                    ndiag.remove(nd)
            row.remove(r)
        solve(0, [])

        return sol