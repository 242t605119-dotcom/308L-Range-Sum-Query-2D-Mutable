class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]

        for i in range(self.m):
            for j in range(self.n):
                self._update(i + 1, j + 1, matrix[i][j])

    def _update(self, row, col, value):
        i = row

        while i <= self.m:
            j = col
            while j <= self.n:
                self.tree[i][j] += value
                j += j & -j
            i += i & -i

    def update(self, row, col, val):
        difference = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self._update(row + 1, col + 1, difference)

    def _sum(self, row, col):
        total = 0
        i = row

        while i > 0:
            j = col
            while j > 0:
                total += self.tree[i][j]
                j -= j & -j
            i -= i & -i

        return total

    def sumRegion(self, row1, col1, row2, col2):
        return (
            self._sum(row2 + 1, col2 + 1)
            - self._sum(row1, col2 + 1)
            - self._sum(row2 + 1, col1)
            + self._sum(row1, col1)
        )
