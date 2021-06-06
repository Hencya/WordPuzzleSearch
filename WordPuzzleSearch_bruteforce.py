import string

#Bruteforce
class bruteforce:
    def vertical(self,grid, col, row, hasilGrid):
        concategrid = grid[col][row]
        hasilGrid.append(concategrid)
        col += 1
        while col <= (len(grid)-1):
            concategrid = concategrid + grid[col][row]
            hasilGrid.append(concategrid)
            col += 1
        return hasilGrid

    def horizontal(self, grid, col, row, hasilGrid):
        concategrid = grid[col][row]
        hasilGrid.append(concategrid)
        row += 1
        while row <= (len(grid)-1):
            concategrid = concategrid + grid[col][row]
            hasilGrid.append(concategrid)
            row += 1
        return hasilGrid

    def diagonal(self, grid, col, row, hasilGrid):
        concategrid = grid[col][row]
        hasilGrid.append(concategrid)
        row += 1
        col += 1
        while row <= (len(grid)-1) and col <= (len(grid)-1):
            concategrid = concategrid + grid[col][row]
            hasilGrid.append(concategrid)
            row += 1
            col += 1
        return hasilGrid

    def initArray(self, grid):
        hasilGrid = []
        for col in range(len(grid)-1):
            for row in range(len(grid)-1):
                self.horizontal(grid, col, row, hasilGrid)
                self.vertical(grid, col, row, hasilGrid)
                self.diagonal(grid, col, row, hasilGrid)
        return hasilGrid

def searchingWord(hasilGrid):
    found = False
    cari = input("Masukan kata yang ingin dicari :")
    for i in range(len(hasilGrid)):
        if cari.upper() == hasilGrid[i]:
            found = True
            break
    
    if found:
        print("KATA YANG ANDA CARI ADA")
    else:
        print("KATA TIDAK ADA")


if __name__ == '__main__':
    #list 4 x 4
    grid1 = [["K", "F", "N", "K"],
            ["D", "A", "I", "K"],
            ["A", "I", "I", "W"],
            ["D", "Z", "I", "Z"]
            ]
    array1 = bruteforce().initArray(grid1)
    searchingWord(array1)



    

