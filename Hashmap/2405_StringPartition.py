class Solution:
    def partitionString(self, s: str) -> int:
        letters = set()
        partitions = 1

        for c in s:
            if c in letters:
                letters = set()
                partitions += 1
            letters.add(c)
        
        return partitions
