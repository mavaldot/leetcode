class Solution:
    @cache
    def countAndSay(self, n: int) -> str:
        if (n == 1): return "1"
        num = self.countAndSay(n-1)
        res = ""
        repeat = 0
        prev = ""
        for i in range(len(num)+1):
            if i == len(num):
                res += str(repeat)
                res += prev
                break
            if num[i] != prev:
                if repeat != 0:
                    res += str(repeat)
                    res += prev
                repeat = 1
                prev = num[i]
            else:
                repeat += 1
        return res