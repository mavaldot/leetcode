class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['*'] = {}

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                return False
        return '*' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c in cur:
                cur = cur[c]
            else:
                return False
        return True