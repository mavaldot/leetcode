class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        d = ""
        i = 0
        n = len(path)
        while i < n:
            while (i < n and path[i] == "/"):
                i += 1
            j = i
            while (j < n and path[j] != "/"):
                j += 1
            
            d = path[i:j]
            print(d)
            if d == ".." and len(res) >= 1:
                res.pop(-1)
            elif d != "." and d != "..":
                res.append(d)
            i = j
            print(res)
        
        p = "/" + "/".join(res)
        if len(p) > 1 and p[-1] == "/":
            p = p[:len(p)-1]
        print(p)
        return p