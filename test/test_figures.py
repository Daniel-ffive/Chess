import numpy as np
import unittest
import copy
from src.figure import Pawn, Rook, Knight, Bishop, Queen, King
from src.board import Board
from game_params import FIELD_COL_DICT, FIELD_ROW_DICT
from game_setup import FIGURES


class TestFigures(unittest.TestCase):
    def setUp(self) -> None:
        self.initial_board = np.zeros((8, 8))
        for i in range(8):
            self.initial_board[1, i] = 1
            self.initial_board[6, i] = -1
        for i in [1, 6]:
            self.initial_board[0, i] = 2.5
            self.initial_board[7, i] = -2.5
        for i in [2, 5]:
            self.initial_board[0, i] = 3.5
            self.initial_board[7, i] = -3.5
        for i in [0, 7]:
            self.initial_board[0, i] = 5
            self.initial_board[7, i] = -5
        self.initial_board[0, 3] = 9
        self.initial_board[7, 3] = -9
        self.initial_board[0, 4] = 10
        self.initial_board[7, 4] = -10

    def test_create_board(self):
        expected_output = self.initial_board
        board = Board(FIGURES)
        board.create_board()
        output = board.status
        np.testing.assert_array_equal(expected_output, output)

    def test_move_to_1(self):
        board = Board(FIGURES)
        new_field = "e4"
        expected_output = (FIELD_ROW_DICT[new_field[1]], FIELD_COL_DICT[new_field[0]])
        wP5 = Pawn("e2", "white")
        wP5.move_to(board, new_field, "black")
        output = wP5.field_row, wP5.field_col
        self.assertEqual(expected_output, output)

    def test_move_to_2(self):
        board = Board(FIGURES)
        new_field = "e5"
        expected_output = (FIELD_ROW_DICT[new_field[1]], FIELD_COL_DICT[new_field[0]])
        bP5 = Pawn("e7", "black")
        bP5.move_to(board, new_field, "white")
        output = bP5.field_row, bP5.field_col
        self.assertEqual(expected_output, output)

    def test_move_to_3(self):
        board = Board(FIGURES)
        new_field = "e4"
        expected_output = (FIELD_ROW_DICT["7"], FIELD_COL_DICT["e"])
        bP5 = Pawn("e7", "black")
        bP5.move_to(board, new_field, "white")
        output = bP5.field_row, bP5.field_col
        self.assertEqual(expected_output, output)

    def test_get_captured(self):
        figures = copy.deepcopy(FIGURES)
        board = Board(figures)
        piece = figures[0]
        self.assertTrue(piece in board.figures)
        piece.get_captured(board)
        self.assertEqual(0, piece.value)
        self.assertTrue(piece not in board.figures)

    def test_display_board(self):
        board = Board(FIGURES)
        board.create_board()
        expected_output = " [bR]  [bN]  [bB]  [bQ]  [bK]  [bB]  [bN]  [bR] \n" \
                          " [bp]  [bp]  [bp]  [bp]  [bp]  [bp]  [bp]  [bp] \n" \
                          " [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ] \n" \
                          " [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ] \n" \
                          " [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ] \n" \
                          " [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ] \n" \
                          " [wp]  [wp]  [wp]  [wp]  [wp]  [wp]  [wp]  [wp] \n" \
                          " [wR]  [wN]  [wB]  [wQ]  [wK]  [wB]  [wN]  [wR] "
        output = board.display_board()
        self.assertEqual(expected_output, output)

    def test_get_covered_squares_1(self):
        board = Board([King("e4", "white"), King("e6", "black"), Bishop("a1", "black")])
        board.create_board()
        expected_output = {(6, 4), (6, 5), (5, 5), (4, 5),
                           (4, 4), (4, 3), (5, 3), (6, 3),
                           (1, 1), (2, 2), (3, 3), (4, 4),
                           (5, 5), (6, 6), (7, 7)}
        board.get_covered_squares("black")
        output = board.covered_squares
        self.assertEqual(expected_output, output)

    def test_get_covered_squares_2(self):
        board = Board(FIGURES)
        board.create_board()
        expected_output = {(5, 0), (5, 1), (5, 2), (5, 3),
                           (5, 4), (5, 5), (5, 6), (5, 7)}
        board.get_covered_squares("black")
        output = board.covered_squares
        self.assertEqual(expected_output, output)

    def test_get_covered_squares_3(self):
        board = Board([King("e4", "white"), King("e6", "black"), Bishop("a1", "black")])
        board.create_board()
        expected_output = {(6, 4), (6, 5), (5, 5), (4, 5),
                           (4, 4), (4, 3), (5, 3), (6, 3),
                           (1, 1), (2, 2), (3, 3), (4, 4),
                           (5, 5), (6, 6), (7, 7)}
        board.get_covered_squares("black")
        output = board.covered_squares
        self.assertEqual(expected_output, output)

    def test_king_in_check(self):
        king = King("d4", "white")
        board = Board([king, King("e6", "black"), Bishop("a1", "black")])
        board.create_board()
        board.king_in_check(king.color)
        expected_output = king.color
        output = board.in_check
        self.assertEqual(expected_output, output)

    def test_king_in_check_2(self):
        king = King("e4", "white")
        board = Board([king, King("e6", "black"), Bishop("a1", "black")])
        board.create_board()
        board.king_in_check(king.color)
        expected_output = "None"
        output = board.in_check
        self.assertEqual(expected_output, output)

    def test_king_capture_covered_piece(self):
        king = King("e4", "white")
        board = Board([king, Knight("e5", "black"), Bishop("a1", "black")])
        board.create_board()
        output = king.move_to(board, "e5", "black")
        expected_output = (False, "illegal move: king in check")
        self.assertEqual(expected_output, output)

    def test_king_capture_uncovered_piece(self):
        king = King("e4", "white")
        board = Board([king, Knight("e5", "black"), Bishop("a2", "black")])
        board.create_board()
        output = king.move_to(board, "e5", "black")
        expected_output = (True, "legal move carried out")
        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
