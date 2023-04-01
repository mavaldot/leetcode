class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if prev == 0:
                    if i < len(flowerbed) - 1:
                        if flowerbed[i+1] == 0:
                            flowerbed[i] = 1
                            n -= 1
                    else:
                        flowerbed[i] = 1
                        n -= 1 
            if n <= 0: return True
            prev = flowerbed[i]
        return False