class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp = {}

        def match(i, j):
            #print(f"{i}, {j}")
            if i == len(s):
                #print(f"Arrived: {i}, {j}")
                for x in range(j, len(p)):
                    if p[x] != '*':
                        print("Failed")
                        return False
                return True
            if i >= len(s) or j >= len(p):
                return False
            if (i,j) in dp:
                return dp[(i,j)]
            if p[j] == '?' or s[i] == p[j]:
                res = match(i+1, j+1)
                dp[(i,j)] = res
                return res
            if p[j] == '*':
                res1 = match(i+1, j+1)
                res2 = match(i+1, j)
                res3 = match(i, j+1)
                dp[(i,j)] = res1 or res2 or res3
                return res1 or res2 or res3
            return False
        
        return match(0, 0)