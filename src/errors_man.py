##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## errors_man.py
##

import os
from sys import argv
import math
import random
from src.constants import *

def usage(c):
    if (c == 1):
        print("Usage: ./101pong x0 y0 z0 x1 y1 z1 n")
    else:
        print("USAGE\n    ./101pong x0 y0 z0 x1 y1 z1 n\n")
        print("DESCRIPTION")
        print("    x0  ball abscissa at time t -1")
        print("    y0  ball ordinate at time t -1")
        print("    z0  ball altitude at time t -1")
        print("    x1  ball abscissa at time t")
        print("    y1  ball ordinate at time t")
        print("    z1  ball altitude at time t")
        print("    n   time shift (greater than or equal to zero, integer)")

def errors(c, num_arg):
    if (c == 1):
        if (num_arg == 1):
            usage(1)
        elif (num_arg == 2):
            usage(2)
            return (0)
    elif (c == 2):
        print(INVALID_NB_ARGS)
    elif (c == 3):
        print(INVALID_ARG)
    elif (c == 4):
        print(N_NEG)
    return (84)
