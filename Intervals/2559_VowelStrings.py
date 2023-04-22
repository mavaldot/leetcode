class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        goodCount = [0] * len(words)
        vowels = "aeiou"
        goodCount[0] += words[0][0] in vowels and words[0][~0] in vowels
        for i in range(1, len(words)):
            goodCount[i] = goodCount[i-1] + (words[i][0] in vowels and words[i][~0] in vowels)
        
        res = []

        for a, b in queries:
            if a == 0:
                res.append(goodCount[b])
            else:
                res.append(goodCount[b] - goodCount[a-1])

        return res