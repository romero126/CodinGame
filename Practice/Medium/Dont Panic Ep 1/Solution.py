import sys
import math


class clones_class():
    floor = 0
    pos = 0
    direction = 0

    def update(this, clone_floor, clone_pos, direction):
        this.floor = clone_floor
        this.pos = clone_pos
        this.direction = direction

    def move(this):
        dst = this.pos
        if clone.floor == exit_floor:
            dst = exit_pos
        for i in elevators:
            if clone_floor == i[0]:
                dst = i[1]
        if this.pos > dst and this.direction == "RIGHT":
            print("BLOCK")
        elif this.pos < dst and this.direction == "LEFT":
            print("BLOCK")
        else:
            print("WAIT")

clone = clones_class()

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]

#Create Elevators Array
elevators = []
for i in range(nb_elevators):
    floor,pos = [int(j) for j in input().split()]
    elevators.append([floor,pos])

while True:
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    clone.update(clone_floor, clone_pos, direction)
    clone.move()
