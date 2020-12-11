import numpy as np
import unittest
from src.figure import Pawn, Rook, Knight, Bishop, Queen, King
from src.figure import Board
from src.figure import FIELD_COL_DICT, FIELD_ROW_DICT
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

    def test_move_to(self):
        new_field = "e4"
        expected_output = (FIELD_ROW_DICT[new_field[1]], FIELD_COL_DICT[new_field[0]])
        wP5 = Pawn("e2", "white")
        wP5.move_to(new_field)
        output = wP5.field_row, wP5.field_col
        self.assertEqual(expected_output, output)
        new_field = "e5"
        expected_output = (FIELD_ROW_DICT[new_field[1]], FIELD_COL_DICT[new_field[0]])
        bP5 = Pawn("e7", "black")
        bP5.move_to(new_field)
        output = bP5.field_row, bP5.field_col
        self.assertEqual(expected_output, output)

    def test_get_captured(self):
        wP1 = Pawn("a2", "white")
        wP1.get_captured()
        self.assertEqual(0, wP1.value)

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

    def test_list_of_legal_pawn_moves_1(self):
        """
        Testcase 1: no capture moves, white pawn on second row
        """
        board = self.initial_board
        board[1, 4] = 0
        board[3, 4] = 1
        board[6, 3] = 0
        board[4, 3] = 1
        pawn = Pawn("a2", "white")
        expected_output = {(1, 0), (2, 0)}
        pawn.get_legal_moves(board)
        output = pawn.legal_moves
        self.assertEqual(expected_output, output)

    def test_list_of_legal_pawn_moves_2(self):
        """
        Testcase 2: no capture moves, white pawn on seventh row
        """
        board = self.initial_board
        board[1, 4] = 0
        board[3, 4] = 1
        board[6, 3] = 0
        board[4, 3] = 1
        pawn = Pawn("a7", "black")
        expected_output = {(-1, 0), (-2, 0)}
        pawn.get_legal_moves(board)
        output = pawn.legal_moves
        self.assertEqual(expected_output, output)

    def test_list_of_legal_pawn_moves_3(self):
        """
        Testcase 3: capture move and one step move, white pawn on e4, black piece on d5
        """
        board = self.initial_board
        board[1, 4] = 0
        board[3, 4] = 1
        board[6, 3] = 0
        board[4, 3] = -1
        pawn = Pawn("e4", "white")
        expected_output = {(1, 0), (1, -1)}
        pawn.get_legal_moves(board)
        output = pawn.legal_moves
        self.assertEqual(expected_output, output)

    def test_list_of_legal_pawn_moves_4(self):
        """
        Testcase 4: capture move and one step move, black pawn on d5, white piece on e4
        """
        board = self.initial_board
        board[1, 4] = 0
        board[3, 4] = 1
        board[6, 3] = 0
        board[4, 3] = 1
        pawn = Pawn("d5", "black")
        expected_output = {(-1, 0), (-1, 1)}
        pawn.get_legal_moves(board)
        output = pawn.legal_moves
        self.assertEqual(expected_output, output)

    def test_list_of_legal_knight_moves_1(self):
        """
        Testcase 1: Additional white Knight on e4, rest of pieces on initial squares
        """
        piece = Knight("e4", "white")
        board = self.initial_board
        board[3, 4] = 2.5
        expected_output = {(2, 1), (1, 2), (-1, 2),
                           (-1, -2), (1, -2), (2, -1)}
        piece.get_legal_moves(board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)

    def test_list_of_legal_knight_moves_2(self):
        """
        Testcase 1: Additional black Knight on e4, rest of pieces on initial squares
        """
        piece = Knight("e4", "black")
        board = self.initial_board
        board[3, 4] = -2.5
        expected_output = {(2, 1), (1, 2), (-1, 2),
                           (-1, -2), (1, -2), (2, -1),
                           (-2, 1), (-2, -1)}
        piece.get_legal_moves(board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)

    def test_list_of_legal_bishop_moves_1(self):
        """
        Testcase 1: Additional white Bishop on e4, rest of pieces on initial squares
        """
        piece = Bishop("e4", "white")
        board = self.initial_board
        board[3, 4] = 3.5
        expected_output = {(1, 1), (2, 2), (-1, 1),
                           (-1, -1), (1, -1), (2, -2),
                           (3, 3), (3, -3)}
        piece.get_legal_moves(board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)

    def test_list_of_legal_bishop_moves_2(self):
        """
        Testcase 1: Additional black Bishop on e4, rest of pieces on initial squares
        """
        piece = Bishop("e4", "black")
        board = self.initial_board
        board[3, 4] = 3.5
        expected_output = {(2, 2), (2, -2), (-2, 2),
                           (-2, -2), (1, -1), (1, 1),
                           (-1, -1), (-1, 1)}
        piece.get_legal_moves(board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)

    def test_list_of_legal_rook_moves_1(self):
        """
        Testcase 1: Additional white Rook on e4, rest of pieces on initial squares
        """
        piece = Rook("e4", "white")
        board = self.initial_board
        board[3, 4] = 5
        expected_output = {(1, 0), (2, 0), (3,0),
                           (0, 1), (0, 2), (0, 3),
                           (0, -1), (0, -2), (0, -3), (0, -4),
                           (-1, 0)}
        piece.get_legal_moves(board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)

    def test_list_of_legal_rook_moves_2(self):
        """
        Testcase 1: Additional black Rook on e4, rest of pieces on initial squares
        """
        piece = Rook("e4", "black")
        board = self.initial_board
        board[3, 4] = 5
        expected_output = {(1, 0), (2, 0),
                           (0, 1), (0, 2), (0, 3),
                           (0, -1), (0, -2), (0, -3), (0, -4),
                           (-1, 0), (-2, 0)}
        piece.get_legal_moves(board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)

    def test_list_of_legal_queen_moves_1(self):
        """
        Testcase 1: Additional white Queen on e4, rest of pieces on initial squares
        """
        piece = Queen("e4", "white")
        board = self.initial_board
        board[3, 4] = 9
        expected_output = {(1, 0), (2, 0), (3,0),
                           (0, 1), (0, 2), (0, 3),
                           (0, -1), (0, -2), (0, -3), (0, -4),
                           (-1, 0),
                           (1, 1), (2, 2), (-1, 1),
                           (-1, -1), (1, -1), (2, -2),
                           (3, 3), (3, -3)}
        piece.get_legal_moves(board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)

    def test_list_of_legal_queen_moves_2(self):
        """
        Testcase 1: Additional black Queen on e4, rest of pieces on initial squares
        """
        piece = Queen("e4", "black")
        board = self.initial_board
        board[3, 4] = 9
        expected_output = {(1, 0), (2, 0),
                           (0, 1), (0, 2), (0, 3),
                           (0, -1), (0, -2), (0, -3), (0, -4),
                           (-1, 0), (-2, 0),
                           (2, 2), (2, -2), (-2, 2),
                           (-2, -2), (1, -1), (1, 1),
                           (-1, -1), (-1, 1)}
        piece.get_legal_moves(board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)

    def test_list_of_legal_king_moves_1(self):
        """
        Testcase 1: Additional white Queen on e4, rest of pieces on initial squares
        """
        piece = King("e4", "white")
        board = self.initial_board
        board[3, 4] = 10
        expected_output = {(1, 0), (1, 1), (0, 1), (-1, 1),
                           (-1, 0), (-1, -1), (0, -1), (1, -1)}
        piece.get_legal_moves(board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)

    def test_list_of_legal_king_moves_2(self):
        """
        Testcase 1: Additional black Queen on e4, rest of pieces on initial squares
        """
        piece = King("e4", "black")
        board = self.initial_board
        board[3, 4] = 9
        expected_output = {(1, 0), (1, 1), (0, 1),
                           (0, -1), (1, -1)}
        piece.get_legal_moves(board)
        output = piece.legal_moves
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


if __name__ == '__main__':
    unittest.main()
