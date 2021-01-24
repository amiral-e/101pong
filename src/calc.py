##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## calc.py
##

from math import sqrt, pow, acos, degrees
from src.vector import vector

def diff_vector(vector_0: vector, vector_1: vector):
    diff_vector = vector(0, 0, 0)
    diff_vector.x = vector_1.x - vector_0.x
    diff_vector.y = vector_1.y - vector_0.y
    diff_vector.z = vector_1.z - vector_0.z
    return (diff_vector)

def ball_coordinates(vector_0: vector, diff_vector: vector, n: int):
    ball_coordinates = vector(0, 0, 0)
    ball_coordinates.x = diff_vector.x * (n + 1) + vector_0.x
    ball_coordinates.y = diff_vector.y * (n + 1) + vector_0.y
    ball_coordinates.z = diff_vector.z * (n + 1) + vector_0.z
    return (ball_coordinates)

def vector_norm(vector: vector):
    return float(sqrt(pow(vector.x, 2) + pow(vector.y, 2) + pow(vector.z, 2)))

def incidence_angle(diff_vector: vector):
    paddle_vector = vector(diff_vector.x, diff_vector.y, 0)
    vector_norm0 = vector_norm(diff_vector)
    vector_norm1 = vector_norm(paddle_vector)
    if (vector_norm0 == 0):
        return (0.0)
    res = vector_norm1 / vector_norm0
    return (degrees(acos(res)))

def ball_reach_paddle(z0: float, z1: float):
    if (z0 == 0):
        return (False)
    elif ((z0 > 0.0 and z1 > 0.0) or (z0 < 0.0 and z1 < 0.0)):
        if (abs(z0) > abs(z1)):
            return (True)
        else:
            return (False)
    else:
        return (True)