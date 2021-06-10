import string
import time 



#Bruteforce
class bruteforce:
    def verticalDown(self,grid, col, row, hasilGrid):
        concateGrid = grid[col][row]
        hasilGrid["arrayHasil"].append(concateGrid)
        hasilGrid["posisi"].append(f"{col},{row}")
        hasilGrid["jenis"].append("Vertical Down")
        col += 1
        while col <= (len(grid[0])-1):
            concateGrid = concateGrid + grid[col][row]
            hasilGrid["arrayHasil"].append(concateGrid)
            hasilGrid["posisi"].append(f"{col},{row}")
            hasilGrid["jenis"].append("Vertical Down")
            col += 1
        return hasilGrid
    
    def verticalUp(self,grid, col, row, hasilGrid):
        concateGrid = grid[col][row]
        hasilGrid["arrayHasil"].append(concateGrid)
        hasilGrid["posisi"].append(f"{(len(grid[0])-1)-col},{row}")
        hasilGrid["jenis"].append("Vertical Up")
        col -= 1
        while col >= 0:
            concateGrid = concateGrid + grid[col][row]
            hasilGrid["arrayHasil"].append(concateGrid)
            hasilGrid["posisi"].append(f"{(len(grid[0])-1)-col},{row}")
            hasilGrid["jenis"].append("Vertical Up")
            col -= 1
        return hasilGrid

    def horizontalRight(self, grid, col, row, hasilGrid):
        concateGrid = grid[col][row]
        hasilGrid["arrayHasil"].append(concateGrid)
        hasilGrid["posisi"].append(f"{col},{row}")
        hasilGrid["jenis"].append("Horizontal Right")
        row += 1
        while row <= (len(grid)-1):
            concateGrid = concateGrid + grid[col][row]
            hasilGrid["arrayHasil"].append(concateGrid)
            hasilGrid["posisi"].append(f"{col},{row}")
            hasilGrid["jenis"].append("Horizontal Right")
            row += 1
        return hasilGrid

    def horizontalLeft(self, grid, col, row, hasilGrid):
        concateGrid = grid[col][row]
        hasilGrid["arrayHasil"].append(concateGrid)
        hasilGrid["posisi"].append(f"{col},{(len(grid)-1)-row}")
        hasilGrid["jenis"].append("Horizontal Left")
        row -= 1
        while row >= 0:
            concateGrid = concateGrid + grid[col][row]
            hasilGrid["arrayHasil"].append(concateGrid)
            hasilGrid["posisi"].append(f"{col},{(len(grid)-1)-row}")
            hasilGrid["jenis"].append("Horizontal Left")
            row -= 1
        return hasilGrid

    def diagonalRightDown(self, grid, col, row, hasilGrid):
        concateGrid = grid[col][row]
        hasilGrid["arrayHasil"].append(concateGrid)
        hasilGrid["posisi"].append(f"{col},{row}")
        hasilGrid["jenis"].append("Diagonal Right Down")
        row += 1
        col += 1
        while row <= (len(grid)-1) and col <= (len(grid[0])-1):
            concateGrid = concateGrid + grid[col][row]
            hasilGrid["arrayHasil"].append(concateGrid)
            hasilGrid["posisi"].append(f"{col},{row}")
            hasilGrid["jenis"].append("Diagonal Right Down")
            row += 1
            col += 1
        return hasilGrid
    
    def diagonalRightUp(self, grid, col, row, hasilGrid):
        concateGrid = grid[col][row]
        hasilGrid["arrayHasil"].append(concateGrid)
        hasilGrid["posisi"].append(f"{(len(grid[0])-1)-col},{row}")
        hasilGrid["jenis"].append("Diagonal Right Up")
        row += 1
        col -= 1
        while row <= (len(grid)-1) and col >= 0:
            concateGrid = concateGrid + grid[col][row]
            hasilGrid["arrayHasil"].append(concateGrid)
            hasilGrid["posisi"].append(f"{(len(grid[0])-1)-col},{row}")
            hasilGrid["jenis"].append("Diagonal Right Up")
            row += 1
            col -= 1
        return hasilGrid

    def diagonalLeftDown(self, grid, col, row, hasilGrid):
        concateGrid = grid[col][row]
        hasilGrid["arrayHasil"].append(concateGrid)
        hasilGrid["posisi"].append(f"{col},{(len(grid)-1)-row}")
        hasilGrid["jenis"].append("Diagonal Left Down")
        row -= 1
        col += 1
        while row >= 0 and col <= (len(grid[0])-1):
            concateGrid = concateGrid + grid[col][row]
            hasilGrid["arrayHasil"].append(concateGrid)
            hasilGrid["posisi"].append(f"{col},{(len(grid)-1)-row}")
            hasilGrid["jenis"].append("Diagonal Left Down")
            row -= 1
            col += 1
        return hasilGrid

    def diagonalLeftUp(self, grid, col, row, hasilGrid):
        concateGrid = grid[col][row]
        hasilGrid["arrayHasil"].append(concateGrid)
        hasilGrid["posisi"].append(f"{(len(grid[0])-1)-col},{(len(grid)-1)-row}")
        hasilGrid["jenis"].append("Diagonal Left Up")
        row -= 1
        col -= 1
        while row >= 0 and col >= 0:
            concateGrid = concateGrid + grid[col][row]
            hasilGrid["arrayHasil"].append(concateGrid)
            hasilGrid["posisi"].append(
                f"{(len(grid[0])-1)-col},{(len(grid)-1)-row}")
            hasilGrid["jenis"].append("Diagonal Left Up")
            row -= 1
            col -= 1
        return hasilGrid

    def initArray(self, grid):
        hasilGrid = {"posisi" : [], "arrayHasil" : [], "jenis" : []}
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                self.horizontalRight(grid, col, row, hasilGrid)
                self.horizontalLeft(grid, col, row, hasilGrid)
                self.verticalDown(grid, col, row, hasilGrid)
                self.verticalUp(grid, col, row, hasilGrid)
                self.diagonalRightDown(grid, col, row, hasilGrid)
                self.diagonalLeftDown(grid, col, row, hasilGrid)
                self.diagonalRightUp(grid, col, row, hasilGrid)
                self.diagonalLeftUp(grid, col, row, hasilGrid)
        return hasilGrid

def searchingWord(hasilGrid):
    hasilSearching = {"posisi": [], "arrayHasil": [], "jenis": []}
    found = False
    print()
    cari = input("Masukan kata yang ingin dicari :")
    for i in range(len(hasilGrid["arrayHasil"])):
        if cari.upper() == hasilGrid["arrayHasil"][i]:
            found = True
            hasilSearching["posisi"].append(hasilGrid["posisi"][i])
            hasilSearching["jenis"].append(hasilGrid["jenis"][i])
    
    if found:
        print("-----------------------")
        print("KATA YANG ANDA CARI ADA")
        print("-----------------------")
        print(f'Kata yang anda cari adalah   : {cari.upper()}')
        print(f'Ketemu di posisi             : {hasilSearching["posisi"]}')
        print(f'Dengan arah ketemunya adalah : {hasilSearching["jenis"]}')
    else:
        print("--------------")
        print("KATA TIDAK ADA")
        print("--------------")


if __name__ == '__main__':
    #test 1
    start_time = time.time()
    grid1 = ["OKO",
            "WEK",
            "CAC"]
    array1 = bruteforce().initArray(grid1)
    searchingWord(array1)
    print("Running Time grid1           : %s seconds" % (time.time() - start_time))

    #test 2
    start_time = time.time()
    grid2 = ["OKOD",
             "WEQK",
             "CACD",
             "SPSA"]
    array1 = bruteforce().initArray(grid2)
    searchingWord(array1)
    print("Running Time grid2           : %s seconds" %
          (time.time() - start_time))

    #test3
    start_time = time.time()
    grid3 = ["OKODS",
            "WEQSK",
            "CACDD",
            "ODSWE",
            "SPSAJ"]
    array1 = bruteforce().initArray(grid3)
    searchingWord(array1)
    print("Running Time grid3           : %s seconds" %
          (time.time() - start_time))  

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
    array1 = bruteforce().initArray(grid4)
    searchingWord(array1)
    print("Running Time grid4           : %s seconds" %
          (time.time() - start_time))

    #test5
    start_time = time.time()
    grid5 = ["ODOEQS",
             "WEQSAC",
             "CDDODS",
             "OKEQSK",
             "WEQCAC",
             "ODSQSK",
             ]
    array1 = bruteforce().initArray(grid5)
    searchingWord(array1)
    print("Running Time grid5           : %s seconds" %
          (time.time() - start_time))



    

