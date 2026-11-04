class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        people.sort()
        l,r = 0,len(people)-1
        while l <= r:
            remain = limit - people[r]
            boat += 1
            r -= 1
            if remain >= people[l]:
                l += 1
        return boat
