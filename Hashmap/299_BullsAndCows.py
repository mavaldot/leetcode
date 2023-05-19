class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        n = len(secret)

        letters = defaultdict(int)
        pos = defaultdict(set)

        for i in range(n):
            letters[secret[i]] += 1
            pos[secret[i]].add(i)

        for i in range(n):
            if letters[guess[i]] > 0:
                if i in pos[guess[i]]:
                    letters[guess[i]] -= 1
                    bulls += 1 
        
        for i in range(n):
            if letters[guess[i]] > 0:
                if i not in pos[guess[i]]:
                    letters[guess[i]] -= 1
                    cows += 1 


        return f"{bulls}A{cows}B"