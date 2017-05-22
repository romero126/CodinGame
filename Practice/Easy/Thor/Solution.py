import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

def Debug(obj):
    r = ""
    for i in obj:
        if r == "":
            r = str(i)
        else:
            r = r + ",  "+ str(i)
    print(r, file=sys.stderr)

class C_Player:
    def SetPos(self, x, y):
        self.x = x
        self.y = y
        Debug(["Setting POS", self.x, self.y])
    def GetPos(self):

        Debug(["YourPos is ", self.x, self.y])
        return self.x, self.y
    def Move(self, id):
        if id == "NW":
            self.y += -1
            self.x += -1
        if id == "N":
            self.y += -1
        if id == "NE":
            self.y += -1
            self.x += 1
        if id == "W":
            self.x += -1
        if id == "E":
            self.x += 1
        if id == "SW":
            self.y += 1
            self.x -= 1
        if id == "S":
            self.y += 1
        if id == "SE":
            self.y += 1
            self.x += 1

        print(id)

Player = C_Player()
Player.SetPos(initial_tx, initial_ty)
Player.GetPos()
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # A single line providing the move to be made: N NE E SE S SW W or NW


    #Thor position = (31,17). Light position = (31,4). Energy = 13

    x, y = Player.GetPos()
    #Start the Smarts


    # NW    N    NE
    # W   U   D   E
    # SW    S    SE
#    if (x == light_x) and (y > light_y):
#        Player.Move("NW")
    if (x > light_x) and (y > light_y):
        Player.Move("NW")
    if (x == light_x) and (y > light_y):
        Player.Move("N")
    if (x < light_x) and (y > light_y):
        Player.Move("NE")

    if (x > light_x) and (y == light_y):
        Player.Move("W")

    if (x < light_x) and (y == light_y):
        Player.Move("E")

    if (x > light_x) and (y < light_y):
        Player.Move("SW")
    if (x == light_x) and (y < light_y):
        Player.Move("S")
    if (x < light_x) and (y < light_y):
        Player.Move("SE")


    
