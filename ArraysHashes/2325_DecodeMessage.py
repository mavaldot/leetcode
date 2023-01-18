class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cipher = {}
        print(chr(97))
        count = 0
        for letter in key:
            if letter == " ": continue
            if letter not in cipher:
                cipher[letter] = chr(97 + count)
                count += 1
        res = ""
        for i in range(0, len(message)):
            if message[i] == " ":
                res += " "
            else:
                res += cipher[message[i]]

        return res