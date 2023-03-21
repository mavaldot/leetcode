class WordDictionary:

    def __init__(self):
        self.words = {}

    def addWord(self, word: str) -> None:
        cur = self.words
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["*"] = {}

    def search(self, word: str) -> bool:
        def helper(w, dic):
            if w == "":
                return "*" in dic
            if w[0] == ".":
                for val in dic.values():
                    if (helper(w[1:], val)):
                        return True
            elif w[0] not in dic:
                return False
            else:
                return helper(w[1:], dic[w[0]])
            return False
        return helper(word, self.words)