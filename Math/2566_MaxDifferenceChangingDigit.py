class Solution:
    def minMaxDifference(self, num: int) -> int:
        maxStr = list(str(num))
        minStr = list(str(num))
        
        maxDigit = maxStr[0]
        maxDigit = '9'
        x = 0
        while (x < len(maxStr)):
            if maxStr[x] != '9':
                maxDigit = maxStr[x]
                break
            x += 1
        if maxDigit == '9': maxDigit = '0'
        
        minDigit = maxStr[0]