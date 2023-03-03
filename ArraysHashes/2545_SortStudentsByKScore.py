class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        
        for i in range(0, len(score) - 1):
            for j in range(0, len(score) - 1 - i):
                print(f"{score[i][k]} vs {score[i+1][k]}")
                if (score[j][k] < score[j+1][k]):
                    print("yes")
                    temp = score[j]
                    score[j] = score[j+1]
                    score[j+1] = temp
        
        return score