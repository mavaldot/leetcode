class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:

        points = {i:0 for i in student_id}
        pos = set(positive_feedback)
        neg = set(negative_feedback)

        for i in range(len(report)):
            for word in report[i].split(" "):
                if word in pos:
                    points[student_id[i]] += 3
                if word in neg:
                    points[student_id[i]] -= 1
        
        hp = []
        for key in points:
            heapq.heappush(hp, (-points[key], key))

        res = []

        for i in range(k):
            val, key = heapq.heappop(hp)
            res.append(key)

        return res