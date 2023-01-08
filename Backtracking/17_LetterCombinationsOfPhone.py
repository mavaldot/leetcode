class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) < 1: return []

        comb = []
        
        letters = []
        letters.append([])
        letters.append([])
        letters.append(['a', 'b', 'c'])
        letters.append(['d', 'e', 'f'])
        letters.append(['g', 'h', 'i'])
        letters.append(['j', 'k', 'l'])
        letters.append(['m', 'n', 'o'])
        letters.append(['p', 'q', 'r', 's'])
        letters.append(['t', 'u', 'v'])
        letters.append(['w', 'x', 'y', 'z'])

        def addLetter(i, s):
            if i == len(digits):
                comb.append(s)
                return
            print(i)
            digit = int(digits[i])
            for item in letters[digit]:
                addLetter(i+1, s + item)

        addLetter(0, "")

        return comb