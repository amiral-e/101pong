##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## test_errors.py
##

import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from src.errors_man import *

class TestErrors(TestCase):
    def test_usage_one(self):
        with patch("sys.stdout", new = StringIO()) as mock_stdout:
            usage(1)
            self.assertEqual(mock_stdout.getvalue(), "Usage: ./101pong x0 y0 z0 x1 y1 z1 n\n")

    def test_usage_other(self):
        expected = "USAGE\n    ./101pong x0 y0 z0 x1 y1 z1 n\n"
        expected += "\nDESCRIPTION\n"
        expected += "    x0  ball abscissa at time t -1\n"
        expected += "    y0  ball ordinate at time t -1\n"
        expected += "    z0  ball altitude at time t -1\n"
        expected += "    x1  ball abscissa at time t\n"
        expected += "    y1  ball ordinate at time t\n"
        expected += "    z1  ball altitude at time t\n"
        expected += "    n   time shift (greater than or equal to zero, integer)\n"

        with patch("sys.stdout", new = StringIO()) as mock_stdout:
            usage(0)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_errors(self):
        argv = ["./101pong"]
        self.assertEqual(errors(1, len(argv)), 84)
        argv = ["./101pong", "-h"]
        self.assertEqual(errors(1, len(argv)), 0)
        argv = ["./101pong", "1", "2", "3", "4", "5", "6", "7"]
        self.assertEqual(errors(2, len(argv)), 84)
        self.assertEqual(errors(3, len(argv)), 84)
        self.assertEqual(errors(4, len(argv)), 84)