class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = []
        locked = list(range(1, len(rooms)))

        for key in rooms[0]:
            keys.append(key)

        while (True):
            if len(keys) == 0: break

            for key in keys:
                if key in locked:
                    for item in rooms[key]:
                        keys.append(item)
                    locked.remove(key) 
                keys.remove(key)

        print(f"{len(locked)}")

        return len(locked) == 0