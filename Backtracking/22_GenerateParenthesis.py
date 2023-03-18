class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def helper(s, left, right):
            if left == 0 and right == 0:
                res.append(s)
            if left < 0 or right < 0:
                return
            helper(s + "(", left - 1, right + 1)
            helper(s + ")", left, right - 1)
        
        helper("(", n - 1, 1)
        
        return res