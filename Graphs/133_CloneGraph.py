# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:

    def __init__(self):
        self.firstIndex = -1

    def cloneGraph(self, node: 'Node') -> 'Node':
        seen = {}
        neighbors = defaultdict(list)

        if node is None: return None

        def explore(nd):
            if nd.val in seen: return

            copyNode = Node(nd.val)
            if self.firstIndex == -1:
                self.firstIndex = nd.val
            seen[nd.val] = copyNode

            print(copyNode.val)

            for neighbor in nd.neighbors:
                neighbors[nd.val].append(neighbor.val)
                explore(neighbor)

        explore(node)

        for key, l in neighbors.items():
            print(f"list: {l}")
            for val in l:
                seen[key].neighbors.append(seen[val])
                print(f"val:{val}")
        
        return seen[self.firstIndex]
