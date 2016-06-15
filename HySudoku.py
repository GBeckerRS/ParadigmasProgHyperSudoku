import sys, os, random, pygame, pdb
sys.path.append(os.path.join("objects"))
import SudokuSquare
import SudokuGrid
from GameResources import *

def getSudoku(puzzleNumber=None):
    """ Inicializacao """
    initial = SudokuGrid.SudokuGrid()
    current = SudokuGrid.SudokuGrid()
    solution = SudokuGrid.SudokuGrid()

    #initial.createGrid(27, puzzleNumber)
    #current.createGrid(27, puzzleNumber)
    #solution.createGrid(81, puzzleNumber)

    strSolution = load_Solution ()
    count = 0
    current.qtEmptyCells = 0
    cntEmpty = 0
    for l in range (0,9):
        for c in range (0,9):
            solution.setNum (l,c,strSolution [count])
            if int ((random.random ()) * 10) >= 5:
                initial.setNum (l,c,strSolution [count])
            else:
                initial.setNum (l,c,None)
                cntEmpty += 1
            count += 1

    current = initial
    current.qtEmptyCells = cntEmpty
    pdb.set_trace ()
    return initial, current, solution

def main():
    """ Inicializa a Pygame """
    pygame.init()

    """ Cria a Janela """
    size = width, height = 400, 500
    screen = pygame.display.set_mode(size)

    """ Imagem de fundo do tabuleiro """
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    board, boardRect = load_image("SudokuBg.png")
    boardRect = boardRect.move(10, 80)

    clock = pygame.time.Clock()

    """ Semente para gerar o tabuleiro """
    puzzleNumber = int(random.random() * 20000) + 1
    pygame.display.set_caption("PySudoku  -  Puzzle " + str(puzzleNumber))    
    inital, current, solution = getSudoku(puzzleNumber)

    theSquares = []
    initXLoc = 10
    initYLoc = 80
    startX, startY, editable, number = 0, 0, "N", 0
    for y in range(9):
        for x in range(9):
            if x in (0, 1, 2):  startX = (x * 41) + (initXLoc + 2)
            if x in (3, 4, 5):  startX = (x * 41) + (initXLoc + 6)
            if x in (6, 7, 8):  startX = (x * 41) + (initXLoc + 10)
            if y in (0, 1, 2):  startY = (y * 41) + (initYLoc + 2)
            if y in (3, 4, 5):  startY = (y * 41) + (initYLoc + 6)
            if y in (6, 7, 8):  startY = (y * 41) + (initYLoc + 10)
            number = inital.getNum(y, x)
            if number != None:
                editable = "N"
            else:
                editable = "Y"
            theSquares.append(SudokuSquare.SudokuSquare(number, 
                                                        startX, 
                                                        startY, 
                                                        editable, 
                                                        x, 
                                                        y))

    currentHighlight = theSquares[0]
    currentHighlight.highlight()

    """ Desenha a tela """
    screen.blit(background, (0, 0))
    screen.blit(board, boardRect)
    pygame.display.flip()

    """ Musica """
    load_music("PySudokuTheme1.ogg")

    """ Teclas aceitas """
    theNumbers = { pygame.K_1 : "1", pygame.K_2 : "2", 
                 pygame.K_3 : "3", pygame.K_4 : "4", pygame.K_5 : "5", 
                 pygame.K_6 : "6", pygame.K_7 : "7", pygame.K_8 : "8", 
                 pygame.K_9 : "9", pygame.K_SPACE : "", pygame.K_BACKSPACE : "",
                 pygame.K_DELETE : "" }

    # Gameloop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                for x in theSquares:
                    if x.checkCollide(mousepos):
                        currentHighlight.unhighlight()
                        currentHighlight = x
                        currentHighlight.highlight()
            if event.type == pygame.KEYDOWN and event.key in theNumbers:
                currentHighlight.change(theNumbers[event.key])
                xLoc, yLoc = currentHighlight.currentLoc()
                current.setNum(yLoc, xLoc, theNumbers[event.key])

                # Verifica Fim de jogo
                if current.checkFull ():
                    pdb.set_trace ()
                    print "Game end!"
                    current.checkSolution (solution)

        # Atualiza a tela
        for num in theSquares:
            num.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    """ Define metodo principal do script """
    main()
    sys.exit()
