import numpy as np
import unittest
from src.figure import Board
from src.figure import FIELD_COL_DICT, FIELD_ROW_DICT
from game_setup import FIGURES, FIGURES_DICT

if __name__ == '__main__':
    board = Board(FIGURES)
    turn = "white"
    board.create_board()
    board.display_board()
    while True:
        figure_to_move = input(f"{turn} to move, chose piece to move: ")
        if not figure_to_move.startswith(turn[0]):
            print("It is %s's turn. Please chose a %s piece to move." % (turn, turn))
        else:
            figure_to_move = FIGURES_DICT[figure_to_move]
            new_pos = input("Move to: ")
            figure_to_move.move_to(new_pos)
            if turn == "white":
                turn = "black"
            elif turn == "black":
                turn = "white"
            board.create_board()
            board.display_board()
