
class Solution:
    
    def isPalindrome(self, s: str):
        for i in range(0, len(s)//2):
            if s[~i] != s[i]:
                return False
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        pal = defaultdict(list)

        for i in range(0, len(s)):
            for j in range(i+2, len(s) + 1):
                if self.isPalindrome(s[i:j]):
                    print(f"Palindrome: {s[i:j]}")
                    pal[i].append(j)


        def getPartition(i, arr):
            if i == len(s):
                res.append(arr[:])
                return
            
            if i in pal:
                for point in pal[i]:
                    arr.append(s[i:point])
                    getPartition(point, arr[:])
                    arr.pop()

            arr.append(s[i])
            getPartition(i+1, arr[:]) 
        
        getPartition(0, [])

        return res