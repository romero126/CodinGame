import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class player():
    path = ["SOUTH", "EAST", "NORTH", "WEST"]
    path_pos = 0
    pathing = []
    path_inversed = False
    x, y = 0, 0
    moves = []
    breaker = False
    teleporter = False
    teleporters = []
    '''
        All moves will be in this format
        [x, y, direction, breaker_State]
    '''
    def init(this, grid):

        #Find myself
        for y in range(len(grid)):

            for x in range(len(grid[y])):
                if grid[y][x] == '@':
                    this.x, this.y = x, y
                    grid[y][x] = ' '
                if grid[y][x] == 'T':
                    this.teleporters.append([x, y])

    def testmv(this, grid, direction):
        nx, ny = this.x, this.y
        if this.path[direction] == 'SOUTH':
            ny += 1
        if this.path[direction] == 'EAST':
            nx += 1
        if this.path[direction] == 'NORTH':
            ny += -1
        if this.path[direction] == 'WEST':
            nx += -1

        return nx, ny, grid[ny][nx]

    def move(this, grid):
        #Looping Detection

        if this.teleporter == True:
            #find next teleporter
            for i in this.teleporters:
                v = [this.x, this.y]
                if i != v:
                    this.x, this.y = i[0], i[1]
                    break
            this.teleporter = False
        if this.path_inversed == True:
            cardinal = this.path[this.path_pos]

            p = []
            for i in reversed(this.path):
                p.append(i)
            this.path = p

            this.path_pos = this.path.index(cardinal)
            this.path_inversed = False


        nx, ny, gv = this.testmv(grid, this.path_pos)
        direction = this.path[this.path_pos]


        if gv == 'X' and this.breaker == True:
            #Break the wall!!
            grid[ny][nx] = ' '
            gv = ' '
            this.moves = []
        elif gv == '#' or gv == 'X':

            for i in range(len(this.path)):
                ax, ay, av = this.testmv(grid, i)
                if av != '#' and av != 'X':
                    this.path_pos = i
                    this.move(grid)
                    return

        elif gv == "$":
            global running
            running = False
        elif gv == 'S':
            this.path_pos = this.path.index('SOUTH')
        elif gv == 'E':
            this.path_pos = this.path.index('EAST')
        elif gv == 'N':
            this.path_pos = this.path.index('NORTH')
        elif gv == 'W':
            this.path_pos = this.path.index('WEST')
        elif gv == 'T':
            this.teleporter = True
        elif gv == 'B':
            this.breaker = not this.breaker
        elif gv == 'I':
            this.path_inversed = not this.path_inversed

        for i in this.moves:
            #Test x,y, direction
            v = [ nx, ny, this.path[this.path_pos], this.breaker]
            if v == i:
                this.pathing = []
                this.pathing.append("LOOP")

                global running
                running = False
                return


        this.pathing.append(direction)
        this.moves.append([nx, ny, direction, this.breaker])
        this.x, this.y = nx, ny





w, h = [int(i) for i in input().split()]

#Lets start by creating a map
grid = []
for i in range(w):
    row = input()
    gridx = []
    for i in range(len(row)):
        gridx.append( row[i] )
    grid.append(gridx)






def DrawMap(grid):
    for i in grid:
        print(i, file=sys.stderr)


DrawMap(grid)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
bender = player()
bender.init(grid)

running = True


r = []


while (running):
    r.append(bender.move(grid))


for i in bender.pathing:
    print(i)
