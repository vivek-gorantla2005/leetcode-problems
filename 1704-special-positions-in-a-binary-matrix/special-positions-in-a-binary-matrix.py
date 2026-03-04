class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ones = {}  # store positions of 1s
        
        rows = len(mat)
        cols = len(mat[0])
        
        # track 1's
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    ones[(i, j)] = True
        
        ans = 0
        
        for i, j in ones.keys():
            flag = False
            
            # check row
            for col in range(cols):
                if col != j and mat[i][col] == 1:
                    flag = True
                    break
            
            # check column
            if not flag:
                for row in range(rows):
                    if row != i and mat[row][j] == 1:
                        flag = True
                        break
            
            if not flag:   # special position
                ans += 1
        
        return ans