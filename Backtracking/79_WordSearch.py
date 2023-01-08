class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        letters = set(word)
        seen = False
        for letter in letters:
            for row in board:
                if letter in row:
                    seen = True
            if seen == False: return False
            seen = False
        

        def searchCell(i, j, index, visited):

            if (i, j) in visited:
                return False
            if (i < 0 or i >= len(board)
            or j < 0 or j >= len(board[0])):
                return False
            if index == len(word) - 1:
                return board[i][j] == word[index]
            
            if board[i][j] != word[index]: return False

            visited.append((i,j))

            return (searchCell(i, j-1, index+1, visited[:]) or 
            searchCell(i, j+1, index+1, visited[:])
            or searchCell(i+1, j, index+1, visited[:]) or searchCell(i-1, j, index+1, visited[:]))

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if searchCell(i, j, 0, []):
                    return True
        return False