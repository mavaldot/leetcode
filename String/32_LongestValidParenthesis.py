class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        if "(" not in s or ")" not in s: return 0

        longest = 0

        for i in range(len(s)):
            if s[i] == ")": continue
            left = 1
            right = 0
            for j in range(i+1, len(s)):
                if s[j] == ")":
                    right += 1
                else:
                    left += 1
                if right > left: break
                if left == right:
                    longest = max(longest, left*2)
            
        return longest