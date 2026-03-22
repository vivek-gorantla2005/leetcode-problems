class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate():
            n = len(mat)
            for i in range(n):
                for j in range(i,n):
                    mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
            
            for i in range(n):
                mat[i] = mat[i][::-1]
            return mat
        
        for i in range(4):
            if rotate() == target:
                return True
        
        return False
        