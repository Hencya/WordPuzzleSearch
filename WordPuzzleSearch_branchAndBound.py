class searching:
    def __init__(self):
        self.R = None
        self.C = None
        self.dir = [[-1, 0], [1, 0], [1, 1],
                    [1, -1], [-1, -1], [-1, 1],
                    [0, 1], [0, -1]]

    def searchingWord(self, grid, row, col, word):
        if grid[row][col] != word[0]:
            return False
        print("------------\n"+"huruf",
              word[0], "ketemu di posisi :", row, col)

        for x, y in self.dir:
            rd, cd = row + x, col + y
            flag = True
            for k in range(1, len(word)):
                if (0 <= rd < self.R and
                    0 <= cd < self.C and
                        word[k] == grid[rd][cd]):
                    print("huruf", word[k], "ketemu di posisi :", rd, cd)
                    rd += x
                    cd += y
                else:
                    flag = False
                    break
            if flag:
                return True
        return False

    def pattern(self, grid, word):
        self.R = len(grid)
        self.C = len(grid[0])
        for row in range(self.R):
            for col in range(self.C):
                if self.searchingWord(grid, row, col, word):
                    print("Kata ketemu pada posisi " +
                          str(row) + ', ' + str(col))

# Driver Code
if __name__ == '__main__':
    grid = ["KDSZWKGZWKD",
            "ADIFLDOWIDK",
            "FAIZADAWOAK",
            "FWAOADAWODF"]
    searching().pattern(grid, 'FAIZ')
