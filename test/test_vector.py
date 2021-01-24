##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## test_vector.py
##

import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from src.vector import vector
from src.calc import *

class TestVector(TestCase):
    def test_vector(self):
        test_vector = vector(4, 2, 7)

        self.assertEqual(test_vector.x, 4)
        self.assertEqual(test_vector.y, 2)
        self.assertEqual(test_vector.z, 7)

class TestDiffVector(TestCase):
    def test_diff_vector(self):
        test_vector0 = vector(2, 1, 5)
        test_vector1 = vector(4, 2, 7)
        test_diff_vector = diff_vector(test_vector0, test_vector1)

        self.assertEqual(test_diff_vector.x, 2)
        self.assertEqual(test_diff_vector.y, 1)
        self.assertEqual(test_diff_vector.z, 2)

class TestBallCoordinatesVector(TestCase):
    def test_ball_coordinates(self):
        test_vector0 = vector(2, 1, 5)
        test_vector1 = vector(4, 2, 7)
        test_diff_vector = diff_vector(test_vector0, test_vector1)
        test_ball_coordinates = ball_coordinates(test_vector0, test_diff_vector, 3)

        self.assertEqual(test_ball_coordinates.x, 10)
        self.assertEqual(test_ball_coordinates.y, 5)
        self.assertEqual(test_ball_coordinates.z, 13)

class TestVectorNorm(TestCase):
    def test_vector_norm(self):
        test_vector0 = vector(2, 3, 4)
        test_vector_norm = vector_norm(test_vector0)
        test_res = float(sqrt(pow(2, 2) + pow(3, 2) + pow(4, 2)))

        self.assertEqual(test_vector_norm, test_res)

class TestIncidenceAngle(TestCase):
    def test_incidence_angle(self):
        test_vector0 = vector(2, 1, 5)
        test_vector1 = vector(4, 2, 7)
        test_diff_vector = diff_vector(test_vector0, test_vector1)
        test_incidence_angle = incidence_angle(test_diff_vector)
        test_incidence_angle = round(test_incidence_angle, 2)

        self.assertEqual(test_incidence_angle, 41.81)

class TestBallReachPaddleZero(TestCase):
    def test_incidence_angle(self):
        test_vector0 = vector(2, 1, 0)
        test_vector1 = vector(4, 2, 7)
        test_ball_reach_paddle = ball_reach_paddle(test_vector0.z, test_vector1.z)

        self.assertEqual(test_ball_reach_paddle, False)

class TestBallReachPaddleZ0Bigger(TestCase):
    def test_incidence_angle(self):
        test_vector0 = vector(2, 1, 7)
        test_vector1 = vector(4, 2, 5)
        test_ball_reach_paddle = ball_reach_paddle(test_vector0.z, test_vector1.z)

        self.assertEqual(test_ball_reach_paddle, True)

class TestBallReachPaddleZ1Bigger(TestCase):
    def test_incidence_angle(self):
        test_vector0 = vector(2, 1, 5)
        test_vector1 = vector(4, 2, 7)
        test_ball_reach_paddle = ball_reach_paddle(test_vector0.z, test_vector1.z)

        self.assertEqual(test_ball_reach_paddle, False)

class TestBallReachPaddleFalseNeg(TestCase):
    def test_incidence_angle(self):
        test_vector0 = vector(-2, -1, -5)
        test_vector1 = vector(4, 2, 7)
        test_ball_reach_paddle = ball_reach_paddle(test_vector0.z, test_vector1.z)

        self.assertEqual(test_ball_reach_paddle, True)

class TestBallReachPaddleTrue(TestCase):
    def test_incidence_angle(self):
        test_vector0 = vector(4, 2, 7)
        test_vector1 = vector(2, 1, 5)
        test_ball_reach_paddle = ball_reach_paddle(test_vector0.z, test_vector1.z)

        self.assertEqual(test_ball_reach_paddle, True)