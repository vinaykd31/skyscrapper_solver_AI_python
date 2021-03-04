import pygame, sys, requests
import pygame, sys
import requests
from bs4 import BeautifulSoup
from settings import *
from buttonClass import *
from algorithmClass import *
class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = gameBoard2
        self.N = SIZE
        self.state = "playing"
        self.font = pygame.font.SysFont("comicsansms", cellSize//2)
        self.solutiongrid =emptySolution
        self.optionButton= []
        self.loadButton()
        self.algorithm=algorithm(self.grid,SIZE)
        self.solvedstate=-1

### function that run everything in a loop
    def run(self):
        while self.running:
            if self.state == "playing":
                self.playing_draw()
                self.playing_events()
                self.playing_update()
        pygame.quit()
        sys.exit()

    def playing_draw(self):

        self.window.fill(WHITE)
        self.drawGrid(self.window)
        self.drawNumbers(self.window)
        self.drawEntry(self.window)
        self.textToScreenHint( self.window, stepText[self.solvedstate+1], [2 * CELLSIZE, 7 * CELLSIZE + 10] )
        for button in self.optionButton:
            button.draw(self.window)

        pygame.display.update()
    def textToScreenHint(self,window,text,pos):
        fontObj = pygame.font.SysFont( "comicsansms", 20 )
        font = fontObj.render( text, False, BLACK )

        window.blit( font, pos )

    def solver(self):
        print("hi i am solver")
        self.solutiongrid=self.algorithm.run(self.solvedstate+1)

        self.solvedstate+=1
        if self.solvedstate>3:
            self.solvedstate =3

    def reset(self):
        print( "hi i am reset" )
        del self.algorithm
        self.solvedstate=-1
        self.algorithm=algorithm(self.grid,SIZE)
        self.solutiongrid = emptySolution


###### PLAYING STATE FUNCTIONS #####
    def loadButton(self):
        self.optionButton.append( Button( cellSize +50 , gridPos[0] + CELLSIZE +50 + gridSize, WIDTH // 7, 40,
                                          colour = (117, 172, 112),
                                            function = self.solver,
                                            text= "Run" ) )
        self.optionButton.append( Button( cellSize + 150 + WIDTH // 7, gridPos[0] + CELLSIZE +50 + gridSize, WIDTH // 7, 40,
                                            colour=(27, 142, 207 ),
                                            function=self.reset,
                                            text= "Reset" ) )


    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.optionButton:
                    if button.highlighted:
                        button.click()



    def playing_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.optionButton:
            button.update( self.mousePos )

    def drawEntry(self, window):
        for i in range(len(self.solutiongrid)):
            text= str(self.solutiongrid[i])
            pos = [ ((i%self.N)*cellSize)+gridPos[1],((i//self.N)*cellSize)+gridPos[0]]
            self.fillSet(window, text , pos)


    def fillSet(self, window, text, pos):
        fontObj = pygame.font.SysFont( "comicsansms", 18)
        font = fontObj.render(text[1:-1], False, BLACK)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        pos[0] += (cellSize-fontWidth)//2
        pos[1] += (cellSize-fontHeight)//2
        window.blit(font, pos)

    def drawNumbers(self, window):


        for row in range(len(self.grid[0])):
            for side in range(len(self.grid[0][row])):
                l = self.grid[0][row][side]
                if l != 0:
                    pos = [side*(gridSize+CELLSIZE) +gridPos[0] - CELLSIZE , (row*cellSize)+gridPos[1]]
                    s=str(l)

                    self.drawSelection(window,pos)
                    self.textToScreen(window, s, pos)

        for row in range(len(self.grid[1])):
            for side in range(len(self.grid[1][row])):
                l = self.grid[1][row][side]
                if l != 0:
                    pos = [gridPos[0] +(row*cellSize), side*(gridSize+ CELLSIZE)+gridPos[1] -cellSize]
                    s=str(l)
                    self.drawSelection(window,pos)
                    self.textToScreen(window, s, pos)



    def drawSelection(self, window, pos):

        pygame.draw.rect(window, LIGHTBLUE, (pos[0]+10 , pos[1]+ 10, cellSize-10, cellSize-10))

    def drawGrid(self, window):
        pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], gridSize, gridSize), 2)
        for x in range(SIZE):
            pygame.draw.line(window, BLACK, (gridPos[0]+(x*cellSize), gridPos[1]), (gridPos[0]+(x*cellSize), gridPos[1]+gridSize), 2 )
            pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1]+(x*cellSize)), (gridPos[0]+gridSize, gridPos[1] + (x*cellSize)), 2 )


    def textToScreen(self, window, text, pos):
        font = self.font.render(text, False, BLACK)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        pos[0] += (cellSize-fontWidth)//2
        pos[1] += (cellSize-fontHeight)//2
        window.blit(font, pos)



