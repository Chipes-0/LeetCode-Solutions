class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        out = 0
        count = 0
        boat = 0
        while people:
            if count + people[0] > limit or boat > 2:
                out += 1
                count = 0
                boat = 0
            count += people.pop(0)
            boat += 1
        if count: 
            out += 1
        return out