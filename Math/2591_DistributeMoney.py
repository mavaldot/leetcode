class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        if money < 0:
            return -1
        child = 0
        remaining = children
        while (money >= 7):

            money -= 7
            child += 1
            remaining -= 1
            if (remaining == 1):
                if money > 7:
                    return child
                if money == 3:
                    return max(0, child - 1)
        
        return child