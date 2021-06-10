import time
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
    #test1
    print("---------------------------------------------")
    start_time = time.time()
    grid1 = ["OKO",
             "WEK",
             "CAC"]
    searching().pattern(grid1, 'CEO')
    print("Running Time grid1           : %s seconds" %
          (time.time() - start_time))
    print("---------------------------------------------")

    #test2
    print("---------------------------------------------")
    start_time = time.time()
    grid2 = ["OKOD",
             "WEQK",
             "CACD",
             "SPSA"]
    searching().pattern(grid2, 'CEO')
    print("Running Time grid2           : %s seconds" %
          (time.time() - start_time))
    print("---------------------------------------------")

    #test3
    print("---------------------------------------------")
    start_time = time.time()
    grid3 = ["OKODS",
             "WEQSK",
             "CACDD",
             "ODSWE",
             "SPSAJ"]
    searching().pattern(grid3, 'CEO')
    print("Running Time grid3           : %s seconds" %
          (time.time() - start_time))
    print("---------------------------------------------")

    #test4
    start_time = time.time()
    grid4 = ["OKODSWEQSK",
             "WEQSKCACDD",
             "CACDDOKODS",
             "OKODSWEQSK",
             "WEQSKCACDD",
             "SPSAJODSWE",
             "DSWEQQSKCA",
             "DDOKOOKODS",
             "ODSWEQSKCA",
             "OKODSWEQSK"]
    searching().pattern(grid4, 'CEO')
    print("Running Time grid4           : %s seconds" %
          (time.time() - start_time))
    print("---------------------------------------------")

    print("---------------------------------------------")
    #test5
    start_time = time.time()
    grid5 = ["ODOEQS",
             "WEQSAC",
             "CDDODS",
             "OKEQSK",
             "WEQCAC",
             "ODSQSK",
             ]
    searching().pattern(grid5, 'CEO')
    print("Running Time grid5           : %s seconds" %
          (time.time() - start_time))
    print("---------------------------------------------")



