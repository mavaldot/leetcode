class Solution:
    def reverse(self, x: int) -> int:
        i = 0
        vals = []
        neg = False
        if x < 0:
            neg = True
            x *= -1
        while (x // 10) > 0:
            r = x % 10
            vals.append(r)
            x = x // 10
            i += 1
        vals.append(x)
        print(vals)

        res = 0

        while (i >= 0):
            a = vals.pop(0)
            a *= pow(10, i)
            res += a
            i -= 1

        if res > pow(2, 31):
            res = 0

        if neg:
            res *= -1

        return res