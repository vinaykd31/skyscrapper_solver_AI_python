

SIZE = 5
CELLSIZE = 100
cellSize = 100
gridPos = (cellSize,cellSize)
gridSize = CELLSIZE*SIZE
WIDTH = 280 + SIZE*CELLSIZE
HEIGHT = 450 + SIZE*CELLSIZE

# Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTBLUE = (125, 116, 127)
LOCKEDCELLCOLOUR = (189,189,189)
GREY = (77,64,78)
INCORRECTCELLCOLOUR = (195,121,121)

# Boards
s=set(range(1,SIZE+1))
emptySolution = [s for i in range(SIZE*SIZE)]
testSolution = [[s for x in range(5)] for x in range(5)]

rowConstraint1 = [[2,3],[2,2],[1,4],[4,2],[4,1]]
colConstraint1 = [[3,2],[2,3],[1,2],[2,2],[4,1]]
gameBoard1 = [rowConstraint1,colConstraint1]

rowConstraint2 = [[2,2],[1,5],[2,2],[4,1],[2,4]]
colConstraint2 = [[2,4],[3,1],[3,2],[1,3],[2,2]]
gameBoard2 = [rowConstraint2,colConstraint2]

row3=[[1,3],[2,2],[3,1],[2,2]]
col3=[[1,2],[2,2],[4,1],[3,2]]
gameBoard3= [row3,col3]


row4=[[3,2],[4,3],[2,3],[1,4],[2,4],[3,1]]
col4=[[4,3],[2,2],[4,2],[2,4],[1,5],[2,1]]
gameBoard4= [row4,col4]

# DisplayText
stepText = ['','Clue elimination is performed','Constraint Propagation is performed', 'Elimination Assignment is performed', 'Sequeunce elimination is performed']



# Positions and sizes


