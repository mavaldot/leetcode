class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = ""
        size = len(words[0])
        start = 0
        for i in range(1, len(words)):
            if size + len(words[i]) + 1 > maxWidth:
                numWords = (i - start) - 1
                spaces = maxWidth - size + numWords
                print(spaces)
                for j in range(start, i):
                    space = math.ceil(spaces/max(1,numWords))
                    line += words[j] + " " * space
                    spaces -= space
                    numWords -= 1
                res.append(line)
                line = ""
                start = i
                size = len(words[i])
            else:
                size += len(words[i]) + 1
                print(words[i])
                print(f"size: {size}")

        numWords = (len(words) - start) - 1
        spaces = maxWidth - size + numWords

        print(start)
        print(len(words))
        for j in range(start, len(words)):
            space = math.ceil(spaces/max(1,numWords))
            line += words[j]
            if j < len(words) - 1: line += " "
            spaces -= space
            numWords -= 1
        line += " " * (maxWidth - len(line))
        res.append(line)

        return res