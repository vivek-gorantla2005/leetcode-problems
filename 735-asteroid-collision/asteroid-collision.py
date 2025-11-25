class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for i in asteroids:
            while s and i < 0 and s[-1] > 0:
                diff = i + s[-1]
                #curr ele destroys top
                if diff < 0:
                    s.pop()
                elif diff > 0:
                    #top is greater than curr so curr gets destroyed
                    i = 0
                else:
                    i = 0
                    s.pop()
            if i != 0:
                s.append(i)
        return s
                

                
        return s
        