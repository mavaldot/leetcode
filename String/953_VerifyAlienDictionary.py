class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {}
        mp[0] = -inf
        for i in range(len(order)):
            mp[order[i]] = i
        
        def compare(w1, w2):
            for i in range(len(w1)):
                c1 = w1[i]
                c2 = w2[i] if i < len(w2) else 0
                if mp[c1] < mp[c2]: return True
                elif c1 == c2: continue
                else: return False
            return True
        
        for i in range(len(words) - 1):
            if not compare(words[i], words[i+1]):
                return False
        return True