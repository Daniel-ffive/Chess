import unittest
from src.figure import Pawn, Rook, Knight, Bishop, Queen, King
from src.figure import Board
from game_setup import FIGURES


class TestLegalMoves(unittest.TestCase):
    def setUp(self):
        self.board = Board(FIGURES)
        self.board.create_board()

    def test_pawn_white_second_row(self):
        """
        Testcase: no capture moves, white pawn on second row
        """
        pawn = Pawn("a2", "white")
        expected_output = {(1, 0), (2, 0)}
        pawn.get_legal_moves(self.board)
        output = pawn.legal_moves
        self.assertEqual(expected_output, output)
        expected_output = set()
        output = pawn.legal_capture_moves
        self.assertEqual(expected_output, output)

    def test_pawn_black_seventh_row(self):
        """
        Testcase: no capture moves, black pawn on seventh row
        """
        pawn = Pawn("a7", "black")
        expected_output = {(-1, 0), (-2, 0)}
        pawn.get_legal_moves(self.board)
        output = pawn.legal_moves
        self.assertEqual(expected_output, output)
        expected_output = set()
        output = pawn.legal_capture_moves
        self.assertEqual(expected_output, output)

    def test_pawn_white_capture(self):
        """
        Testcase: capture move and one step move, white pawn on e6
        """
        pawn = Pawn("e6", "white")
        expected_output = set()
        pawn.get_legal_moves(self.board)
        output = pawn.legal_moves
        self.assertEqual(expected_output, output)
        expected_output = {(1, -1), (1, 1)}
        output = pawn.legal_capture_moves
        self.assertEqual(expected_output, output)

    def test_pawn_black_capture(self):
        """
        Testcase: capture move and one step move, black pawn on b5, white piece on a4
        """
        pawn = Pawn("b3", "black")
        expected_output = set()
        pawn.get_legal_moves(self.board)
        output = pawn.legal_moves
        self.assertEqual(expected_output, output)
        expected_output = {(-1, -1), (-1, 1)}
        output = pawn.legal_capture_moves
        self.assertEqual(expected_output, output)

    def test_knight_white(self):
        """
        Testcase: Additional white Knight on e4, rest of pieces on initial squares
        """
        piece = Knight("e4", "white")
        expected_output = {(2, 1), (1, 2), (-1, 2),
                           (-1, -2), (1, -2), (2, -1)}
        piece.get_legal_moves(self.board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)
        expected_output = set()
        output = piece.legal_capture_moves
        self.assertEqual(expected_output, output)

    def test_knight_black(self):
        """
        Testcase: Additional black Knight on e4, rest of pieces on initial squares
        """
        piece = Knight("e4", "black")
        expected_output = {(2, 1), (1, 2), (-1, 2),
                           (-1, -2), (1, -2), (2, -1)}
        piece.get_legal_moves(self.board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)
        expected_output = {(-2, 1), (-2, -1)}
        output = piece.legal_capture_moves
        self.assertEqual(expected_output, output)

    def test_bishop_white(self):
        """
        Testcase: Additional white Bishop on e4, rest of pieces on initial squares
        """
        piece = Bishop("e4", "white")
        expected_output = {(1, 1), (2, 2), (-1, 1),
                           (-1, -1), (1, -1), (2, -2)}
        piece.get_legal_moves(self.board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)
        expected_output = {(3, 3), (3, -3)}
        output = piece.legal_capture_moves
        self.assertEqual(expected_output, output)

    def test_bishop_black(self):
        """
        Testcase 1: Additional black Bishop on e4, rest of pieces on initial squares
        """
        piece = Bishop("e4", "black")
        expected_output = {(2, 2), (2, -2), (1, -1),
                           (1, 1), (-1, -1), (-1, 1)}
        piece.get_legal_moves(self.board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)
        expected_output = {(-2, 2), (-2, -2)}
        output = piece.legal_capture_moves
        self.assertEqual(expected_output, output)

    def test_rook_white(self):
        """
        Testcase: Additional white Rook on e4, rest of pieces on initial squares
        """
        piece = Rook("e4", "white")
        expected_output = {(1, 0), (2, 0),
                           (0, 1), (0, 2), (0, 3),
                           (0, -1), (0, -2), (0, -3), (0, -4),
                           (-1, 0)}
        piece.get_legal_moves(self.board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)
        expected_output = {(3, 0)}
        output = piece.legal_capture_moves
        self.assertEqual(expected_output, output)

    def test_rook_black(self):
        """
        Testcase: Additional black Rook on e4, rest of pieces on initial squares
        """
        piece = Rook("e4", "black")
        expected_output = {(1, 0), (2, 0),
                           (0, 1), (0, 2), (0, 3),
                           (0, -1), (0, -2), (0, -3), (0, -4),
                           (-1, 0)}
        piece.get_legal_moves(self.board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)
        expected_output = {(-2, 0)}
        output = piece.legal_capture_moves
        self.assertEqual(expected_output, output)

    def test_queen_white(self):
        """
        Testcase: Additional white Queen on e4, rest of pieces on initial squares
        """
        piece = Queen("e4", "white")
        expected_output = {(1, 0), (2, 0),
                           (0, 1), (0, 2), (0, 3),
                           (0, -1), (0, -2), (0, -3), (0, -4),
                           (-1, 0),
                           (1, 1), (2, 2), (-1, 1),
                           (-1, -1), (1, -1), (2, -2)}
        piece.get_legal_moves(self.board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)
        expected_output = {(3, 0), (3, 3), (3, -3)}
        output = piece.legal_capture_moves
        self.assertEqual(expected_output, output)

    def test_queen_black(self):
        """
        Testcase: Additional black Queen on e4, rest of pieces on initial squares
        """
        piece = Queen("e4", "black")
        expected_output = {(1, 0), (2, 0),
                           (0, 1), (0, 2), (0, 3),
                           (0, -1), (0, -2), (0, -3), (0, -4),
                           (-1, 0), (2, 2), (2, -2), (1, -1), (1, 1),
                           (-1, -1), (-1, 1)}
        piece.get_legal_moves(self.board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)
        expected_output = {(-2, 0), (-2, 2), (-2, -2)}
        output = piece.legal_capture_moves
        self.assertEqual(expected_output, output)

    def test_king_white(self):
        """
        Testcase: Additional white King on e4, rest of pieces on initial squares
        """
        self.board.get_covered_squares("black")
        piece = King("e4", "white")
        expected_output = {(1, 0), (1, 1), (0, 1), (-1, 1),
                           (-1, 0), (-1, -1), (0, -1), (1, -1)}
        piece.get_legal_moves(self.board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)
        expected_output = set()
        output = piece.legal_capture_moves
        self.assertEqual(expected_output, output)

    def test_king_black(self):
        """
        Testcase: Additional black King on e4, rest of pieces on initial squares
        """
        self.board.get_covered_squares("white")
        piece = King("e4", "black")
        expected_output = {(1, 0), (1, 1), (0, 1),
                           (0, -1), (1, -1)}
        piece.get_legal_moves(self.board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)
        expected_output = set()
        output = piece.legal_capture_moves
        self.assertEqual(expected_output, output)

    def test_king_white_2(self):
        """
        Testcase: white King on e1, black Queen on e6
        """
        board = Board([Queen("e6", "black"), King("e1", "white")])
        board.create_board()
        board.get_covered_squares("black")
        piece = King("e1", "white")
        expected_output = {(1, 1), (0, 1), (0, -1), (1, -1)}
        piece.get_legal_moves(board)
        output = piece.legal_moves
        self.assertEqual(expected_output, output)
        expected_output = set()
        output = piece.legal_capture_moves
        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
