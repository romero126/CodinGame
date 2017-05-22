import sys
import math

def Debug(*args):
    r = ""
    for i in args:
        if r == "":
            r = str(i)
        else:
            r = r + "   " + str(i)
    print(r, file=sys.stderr)


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]




# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).

    Debug(x, y, v_speed, fuel, rotate, power)

    gravity = 3.771
    landy = 114
    thrust = 1
    #Distance to Ground
    DistanceToGround = y - landy


    EndRound_v_Speed = (v_speed - gravity + thrust )
    #Thrust
    #r = DistanceToGround + v_speed
    if v_speed > -10:
        thrust = 1
    if v_speed > -20:
        thrust = 2
    if v_speed > 30:
        thrust = 3
    if v_speed < -39:
        thrust = 4
    r = v_speed + 40
    #thrust = abs(thrust)

    #* v_speed
    Debug(r)



    #power = thrust

    #t = gravity *
    #t = v *
    #Landing Paramters

    #y = 114



    #if y < 1803:
    #    thrust = 4

    #Define Thrust
    print("0 " + str(thrust))
