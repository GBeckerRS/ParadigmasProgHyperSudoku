import random
import pdb
import sys # Handling exceptions

class SudokuGrid:
    def __init__(self):
        """ Construtor do objeto """
        self.grid = []
        temp = []
        self.qtEmptyCells = 0
        for x in range(9):
            temp.append(None)
        for y in range(9):
            self.grid.append(temp[:])

    def getNum(self, row, column):
        """ Retorna um numero de uma posicao especifica """
        return self.grid[row][column]

    def setNum(self, row, column, number):
        """ Insere um numero em uma posicao especifica """
        self.grid[row][column] = number
        self.qtEmptyCells = self.qtEmptyCells - 1

    def checkRow(self, row, number):
        """ Verifica o numero eh repetido na linha """
        for x in range(9):
            if self.getNum(row, x) == number:
                return True
        return False

    def checkColumn(self, column, number):
        """ Verifica o numero eh repetido na coluna """
        for y in range(9):
            if self.getNum(y, column) == number:
                return True
        return False

    def checkSquare(self, row, column, number):
        """ Verifica o numero eh repetido na quadrado """
        if row in (0, 1, 2): rowrange = (0, 1, 2)
        if row in (3, 4, 5): rowrange = (3, 4, 5)
        if row in (6, 7, 8): rowrange = (6, 7, 8)
        if column in (0, 1, 2): colrange = (0, 1, 2)
        if column in (3, 4, 5): colrange = (3, 4, 5)
        if column in (6, 7, 8): colrange = (6, 7, 8)

        for y in rowrange:
            for x in colrange:
                if self.getNum(y, x) == number:
                    return True
        return False
    
    def checkAll(self, row, column, number):
        """ Executa todas as validacoes """
        if self.checkRow(row, number):
            return True
        elif self.checkColumn(column, number):
            return True
        elif self.checkSquare(row, column, number):
            return True
        else:
            return False

    def checkFull (self):
        """ Verifica se o tabuleiro foi totalmente preenchido """
        if self.qtEmptyCells == 0:
            return True
        return False

    def printGrid(self):
        """ Debug do tabuleiro """
        print
        for y in range(9):
            for x in range(9):
                if x in (3, 6):
                    print "|",
                temp = self.getNum(y, x)
                if temp == None:
                    print " ",
                else:
                    print temp,
            if y in (2, 5):
                print
                print "-" * 22
            else:
                print
        print

    def createGrid(self, genAmount=81, theSeed=None,isSolution=False):
        """ Cria um tabuleiro """
        random.seed(theSeed)

        avail = []
        for num in range(0, 81):
            avail.append((num % 9) + 1)

        # Dificuldade do jogo pode ser alterada aqui pela quantidade
        # de numeros gerados no tabuleiro
        difficulty = 40
        if isSolution:
            difficulty = 0

        while len(avail) > difficulty:
            location = int(random.random() * len(avail))
            numToPlace = avail[location]
            row = int(random.random() * 9)
            col = int(random.random() * 9)

            if self.getNum(row, col) == None:
                if not self.checkAll(row, col, numToPlace):
                    self.setNum(row, col, numToPlace)
                    del avail[location]
        self.qtEmptyCells = len (avail) + 1

    def createGrid_1 (self, genAmount=81, theSeed=None,isSolution=False):
        """ Cria um tabuleiro """
        random.seed(theSeed)

        avail = []
        for num in range(0, genAmount):
            avail.append((num % 9) + 1)
        pdb.set_trace ()

        posit = []
        for num in range(0, 81):
            posit.append(num)
        pdb.set_trace ()

        cPosit = 0
        cout = 0
        p = 0
        #while len(avail) >= 0:
        while len(posit) >= 0:
            location = int(random.random() * len(avail))
            numToPlace = avail[location]

            p = int(random.random() * len(posit))
            row = int(random.random() * 9)
            col = int(random.random() * 9)
            try:
                pos = posit.index (p)
            except: # Handling all exception
                pos = -1
                count =+ 1
            pdb.set_trace ()
            if pos >= 0:
                del posit[pos]

        print "Vezes erradas = "
        pdb.set_trace ()


    def checkSolution(self, solution):
        """ Verifica o tabuleiro preenchido contra a solucao encotrada """
        fWrong = True
        for row in range(9):
            for col in range(9):
                if not solution.getNum(row, col) == self.getNum(row, col):
                    fWrong = False
                    # If a wrong number, empty the cell
                    self.setNum (row, col, "")
        return fWrong


if __name__ == "__main__":
    print "Testing SudokuGrid functionality."
    print "Create an empty grid..."
    sampleGrid = SudokuGrid()
    sampleGrid.printGrid()

    # print
    # print "Compare an empty grid to another empty grid..."
    # emptyGrid = SudokuGrid()
    # print sampleGrid.checkSolution(emptyGrid)

    # print
    # print "Set three numbers in an empty grid..."
    # sampleGrid.setNum(0, 0, 1)
    # sampleGrid.setNum(0, 1, 2)
    # sampleGrid.setNum(0, 2, 3)
    # sampleGrid.setNum(0, 3, 1)
    # sampleGrid.printGrid()
    # print "Check row for ones...",
    # print sampleGrid.checkRow(0, 1)
    # print "Check row for nines...",
    # print sampleGrid.checkRow(0, 4)
    # sampleGrid.setNum(1, 0, 4)
    # sampleGrid.setNum(2, 0, 5)
    # sampleGrid.setNum(3, 0, 6)
    # sampleGrid.printGrid()
    # print "Check column for ones...",
    # print sampleGrid.checkColumn(0, 1)
    # print "Check column for nines...",
    # print sampleGrid.checkColumn(0, 9)
    # sampleGrid.setNum(2, 2, 1)
    # sampleGrid.printGrid()
    # print "Check square for ones...",
    # print sampleGrid.checkSquare(0, 0, 1)
    # print "Check square for nines...",
    # print sampleGrid.checkSquare(0, 0, 9)
    
    print
    print "Attempting to create a full solution..."
    sampleGrid.createGrid_1(81,None,True)
    print
    print
    print "DONE!"
    sampleGrid.printGrid()
    
    # print
    # sampleGrid2 = SudokuGrid()
    # sampleGrid2.createGrid(81, 10)
    # sampleGrid2.printGrid()
