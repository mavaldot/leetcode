class Solution:
    def addDigits(self, num: int) -> int:

        sm = 0
        while num > 0:
            sm += (num % 10)
            num //= 10
            if num == 0 and sm >= 10:
                num = sm
                sm = 0
            # print(num)
            # print(sm)
            # print("####")

        return sm