class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        boats = 0
        while (i <= j):
            w = people[j]
            j -= 1
            if (w + people[i] <= limit):
                i += 1
            boats += 1
        return boats