class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        setofrows = set()
        setofcols = set()
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(0 , rows):
                for j in range(0,cols):
                   if matrix[i][j] == 0:
                        setofrows.add(i)
                        setofcols.add(j)
        for i in setofrows:
                for  j in range(0,cols):
                        matrix[i][j] = 0
        for j in setofcols:
                for i in  range(0,rows):
                        matrix[i][j] = 0
                        
                