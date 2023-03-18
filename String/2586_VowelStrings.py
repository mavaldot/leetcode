class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        cnt = 0
        for i in range(left, right+1):
            word = words[i]
            if word[0] in "aeiou" and word[~0] in "aeiou":
                cnt += 1
        return cnt