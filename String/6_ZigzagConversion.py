class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        row = 0
        res = ""
        step = -1
        i = 0
        j = 0
        while (row <= numRows):
            if j == row:
                res += s[i]
            i += 1
            if j == 0 or j == numRows - 1:
                step *= -1
            j += step
            if i >= len(s):
                i = 0
                j = 0
                row += 1
                step = -1
        return res