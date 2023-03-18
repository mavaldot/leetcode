class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftArr = [0] * (k + 1)
        rightArr = [0] * (k + 1)
        leftSum = 0
        rightSum = 0
        maxPoints = 0
        for i in range(k):
            leftSum += cardPoints[i]
            rightSum += cardPoints[~i]
            leftArr[i+1] = leftSum
            rightArr[i+1] = rightSum
        print(leftArr)
        print(rightArr)

        for i in range(k+1):
            currentPoints = leftArr[i] + rightArr[~i]
            maxPoints = max(currentPoints, maxPoints)

        return maxPoints 