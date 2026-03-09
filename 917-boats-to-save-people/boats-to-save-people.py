class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        if people[0] > limit:
            return -1
        
        n = len(people)
        st = 0
        end = n-1
        boats = 0
        while st <= end:
            if people[st] + people[end] <= limit:
                st+=1
                end-=1
            elif people[end] <= limit:
                end-=1
            boats+=1
        return boats
            