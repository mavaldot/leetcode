class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        self.res = set()

        def addPart(newPart, oldPart, remaining, parts):
            if parts > 5: return
            if not newPart or (len(newPart) > 1 and newPart[0] == "0") or int(newPart) > 255:
                return
            if parts == 4 and remaining == "" and newPart:
                self.res.add(oldPart + newPart)
            for i in range(1, 4):
                addPart(remaining[:i], oldPart + f"{newPart}.", remaining[i:], parts + 1)
        
        for i in range(1, 4):
            addPart(s[:i], "", s[i:], 1)
        
        return list(self.res)