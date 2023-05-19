class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        setA = set()
        setB = set()
        
        pca = [0] * len(A) 
        common = 0
        
        for i in range(len(A)):
            if A[i] in setB and A[i] not in setA:
                common += 1
            setA.add(A[i])
            if B[i] in setA and B[i] not in setB:
                common += 1
            setB.add(B[i])
            
            pca[i] = common
        
        return pca