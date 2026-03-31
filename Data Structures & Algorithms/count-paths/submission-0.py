class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # grid[0][0], only one way (where you started)
        # to get to grid[0][x] there is only one way (moving right)
        # tp get tp grid[x][0] there is only one way (moving down)


        # m = rows, n = cols

        numWays = [[0] * n] * m
        print(numWays)

        for i in range(n):
            numWays[0][i] = 1
        for i in range(m):
            numWays[i][0] = 1

        for row in range(1, m):
            for col in range(1, n):
                numWays[row][col] = numWays[row-1][col] + numWays[row][col-1]
        
        return numWays[m-1][n-1]

           