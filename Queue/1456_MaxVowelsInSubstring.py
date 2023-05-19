class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        dq = deque()
        vowels = "aeiou"
        maxVowels = 0
        curVowels = 0
        
        for c in s:
            dq.append(c)
            if c in vowels:
                curVowels += 1
            if len(dq) > k:
                x = dq.popleft()
                if x in vowels:
                    curVowels -= 1
            maxVowels = max(maxVowels, curVowels)
        
        return maxVowels