#!/usr/bin/python3

##
## EPITECH PROJECT, 2020
## 101pong
## File description:
## 101poppers main file
##

import os
import math
import random
from sys import argv
from src.errors_man import errors
from src.constants import NB_ARGS
from src.vector import vector
from src.calc import *
from src.print import *

num_arg = len(argv)
if (num_arg == 1 or (num_arg == 2 and argv[1] == "-h")):
    exit(errors(1, num_arg))
elif (num_arg != NB_ARGS): exit(errors(2, num_arg))
try:
    x0 = float(argv[1])
    y0 = float(argv[2])
    z0 = float(argv[3])
    x1 = float(argv[4])
    y1 = float(argv[5])
    z1 = float(argv[6])
    n = int(argv[7])
except ValueError:
    exit(errors(3, num_arg))
if (n < 0.0):
    exit(errors(4, num_arg))

vector_0 = vector(x0, y0, z0)
vector_1 = vector(x1, y1, z1)
diff_vector = diff_vector(vector_0, vector_1)
ball_coordinates = ball_coordinates(vector_0, diff_vector, n)
incidence_angle = incidence_angle(diff_vector)
ball_reach_paddle = ball_reach_paddle(vector_1.z, vector_1.z + diff_vector.z)

print_diff_vector(diff_vector)
print_ball_coordinates(ball_coordinates, n)
print_incidence_angle(ball_reach_paddle, incidence_angle)