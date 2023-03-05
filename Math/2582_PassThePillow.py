class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 0
        step = 1
        time += 1
        while time:
            if i == n: step = -1
            if i == 1: step = 1
            i += step
            time -= 1
        return i