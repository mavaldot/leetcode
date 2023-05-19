class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = set(i for i in range(n))

        for a, b in edges:
            if b in nodes: nodes.remove(b)

        return list(nodes)