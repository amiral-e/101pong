##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## print.py
##

from src.vector import vector

def print_diff_vector(vector:vector):
    print("The velocity vector of the ball is:")
    print("(%.2f," % vector.x, "%.2f," % vector.y, "%.2f)" % vector.z)

def print_ball_coordinates(ball_coordinates: vector, n: int):
    print("At time t + " + str(n) + ", ball coordinates will be:")
    print("(%.2f," % ball_coordinates.x, "%.2f," % ball_coordinates.y,
        "%.2f)" % ball_coordinates.z)

def print_incidence_angle(ball_reach: bool, incidence_angle: float):
    if (ball_reach and incidence_angle != 0):
        print("The incidence angle is:")
        print("%.2f" % incidence_angle, "degrees")
    else:
        print("The ball won't reach the paddle.")
