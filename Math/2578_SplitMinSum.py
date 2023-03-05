class Solution:
    def splitNum(self, num: int) -> int:
        digits = []
        minSum = 0
        num1 = 0
        num2 = 0
        
        while (num):
            digits.append(num % 10)
            num = num // 10
            
        digits.sort()
        
        i = 0
        
        while i < len(digits):
            num1 *= 10
            num1 += digits[i]
            i+=1
            
            if i >= len(digits): break
                
            num2 *= 10
            num2 += digits[i]
            i+=1
        
        return num1 + num2