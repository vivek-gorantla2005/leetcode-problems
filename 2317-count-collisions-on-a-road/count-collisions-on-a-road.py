class Solution:
    def countCollisions(self, directions: str) -> int:
        s = []
        ans = 0
        
        for c in directions:
            # Process R, S directly
            if not s:
                s.append(c)
                continue

            # last element on stack
            t = s[-1]

            # Case 1: R meets L → 2 collisions + becomes S
            if t == 'R' and c == 'L':
                ans += 2
                s.pop()
                # After they both stop, this new car (S)
                # can be hit by previous Rs in stack
                while s and s[-1] == 'R':
                    ans += 1
                    s.pop()
                s.append('S')

            # Case 2: S meets L → 1 collision (L stops)
            elif t == 'S' and c == 'L':
                ans += 1
                s.append('S')

            # Case 3: previous Rs keep moving right,
            # new S stops them (each collision = 1)
            elif c == 'S' and t == 'R':
                while s and s[-1] == 'R':
                    ans += 1
                    s.pop()
                s.append('S')

            else:
                s.append(c)

        return ans
