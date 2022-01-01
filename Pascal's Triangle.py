class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2: 
            return [[1], [1,1]]
        else: 
            x = [0]*numRows
            x[0] = [1]
            x[1] = [1,1]
            for n in range(2, numRows): 
                x[n] = [0] * (n+1) 
                x[n][0] = 1
                x[n][-1] = 1
                for j in range(1,n):
                    x[n][j] = x[n-1][j-1] + x[n-1][j]
        return x
        