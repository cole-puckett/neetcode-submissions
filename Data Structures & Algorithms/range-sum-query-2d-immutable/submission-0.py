class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.matrix_ = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if col != 0:
                    self.matrix_[row][col] = self.matrix_[row][col - 1] + matrix[row][col]
                else:
                    self.matrix_[row][col] = matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        sum = 0
        for row in range(row1, row2 + 1, 1):
            if col1 == 0:
                sum += self.matrix_[row][col2]
            else:
                sum += (self.matrix_[row][col2] - self.matrix_[row][col1 - 1])

        return sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)