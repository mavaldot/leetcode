class Solution:
    def addMinimum(self, word: str) -> int:
        need = ['a', 'b', 'c']
        i = 0
        idx = 0
        additions = 0
        last = ''
        while i < len(word):
            last = word[i]
            if word[i] != need[idx]:
                additions += 1
            else:
                i += 1
            idx = (idx + 1) % 3
            
        if last == 'a': additions += 2
        if last == 'b': additions += 1
        return additions