import numpy as np
import copy
from game_params import FIELD_ROW_DICT, FIELD_COL_DICT, COLOR_DICT


class Figure:
    def __init__(self, field, color):
        self.field_col = FIELD_COL_DICT[field[0]]
        self.field_row = FIELD_ROW_DICT[field[1]]
        self.color = color
        self.color_value = COLOR_DICT[color]
        self.value = 0
        self.legal_moves = set()
        self.legal_capture_moves = set()

    def move_to(self, board, new_pos, next_turn):
        """
        Checks if move legal and moves piece if so
        :param next_turn: side to move on the next turn -> "white" or "black"
        :param board: current board -> Instance of class Board
        :param new_pos: string with new position in modern notation, e. g. "e4"
        :return: True, if move was successfully executed, False if not
        """
        board.get_covered_squares(next_turn)
        self.get_legal_moves(board)
        legal_pos = {(self.field_row + move[0], self.field_col + move[1])
                     for move in self.legal_moves | self.legal_capture_moves}
        if (FIELD_ROW_DICT[new_pos[1]], FIELD_COL_DICT[new_pos[0]]) in legal_pos:
            for piece in board.figures:
                if (piece.field_row == FIELD_ROW_DICT[new_pos[1]]
                        and piece.field_col == FIELD_COL_DICT[new_pos[0]]):
                    piece.get_captured(board)
            old_pos_row = copy.deepcopy(self.field_row)
            old_pos_col = copy.deepcopy(self.field_col)
            self.field_row = FIELD_ROW_DICT[new_pos[1]]
            self.field_col = FIELD_COL_DICT[new_pos[0]]
            board.create_board()
            board.king_in_check(self.color)
            if board.in_check == self.color:
                self.field_row = old_pos_row
                self.field_col = old_pos_col
                board.create_board()
                return False, "illegal move: king in check"
            else:
                return True, "legal move carried out"
        else:
            return False, f"illegal move: {self.short_name} cannot move to {new_pos}"

    def get_captured(self, board):
        """
        resets the value of the figure to zero if it was captured
        :return:
        """
        self.value = 0
        board.figures.remove(self)

    def path_clear(self, board, move, target_row, target_col):
        """
        Checks, if the path of a figure to its target position is clear.
        :param board: current board as instance of class Board
        :param move: move to be carried in modern notation, e. g. "e4"
        :param target_row: integer numbering the rows from 0 to 7
        :param target_col: integer numbering the cols from 0 to 7
        :return: True, if path clear, False if not
        """
        if not (target_row > 7 or target_row < 0 or target_col > 7 or target_col < 0):
            row_step = np.sign(move[0])
            col_step = np.sign(move[1])
            sq_cov = not any(board.status[self.field_row + i * row_step,
                                          self.field_col + i * col_step]
                             for i in range(1, abs(move[0])))
            return sq_cov
        else:
            return False

    def get_legal_moves(self, board):
        """
        get all legal moves from potential moves considering the current board.
        General restrictions:
        - cannot capture-move to a square where a piece of the same color stands
        - cannot capture-move to an empty square
        - cannot move to a square where a piece stands
        Restrictions for all pieces except for Knights:
        - cannot capture-move nor move through a position where a piece stands
        :param board: current board
        :return:
        """
        moves = set()
        capture_moves = set()
        for move in self.pot_moves:
            target_row = self.field_row + move[0]
            target_col = self.field_col + move[1]
            if self.path_clear(board, move, target_row, target_col):
                if board.status[target_row, target_col] * self.color_value == 0:
                    moves.add(move)
                if board.status[target_row, target_col] * self.color_value < 0:
                    capture_moves.add(move)
        self.legal_moves = moves
        self.legal_capture_moves = capture_moves


class Pawn(Figure):
    def __init__(self, field, color):
        """
        Class with methods and properties of pawns
        :param field: Field of the pawn
        :param color: Color (black or white) of the pawn
        """
        Figure.__init__(self, field, color)
        self.pot_capture_moves = {(1 * self.color_value, 1),
                                  (1 * self.color_value, -1)}
        self.pot_moves = {(1 * self.color_value, 0),
                          (2 * self.color_value, 0)}
        self.value = 1 * self.color_value
        self.short_name = self.color[0] + "p"

    def get_legal_moves(self, board):
        """
        get all legal moves from potential moves considering the current board.
        General restrictions:
        - cannot capture-move to a square where a piece of the same color stands
        - cannot capture-move to an empty square
        - cannot move to a square where a piece stands
        Restrictions for all pieces except for Knights:
        - cannot capture-move or move through a position where a piece stands
        Restrictions for pawns:
        - white pawns can only move two squares, when they stand on the second row
        - black pawns can only move two squares, when they stand on the seventh row
        - pawns can only move forward
        :param board: current board
        :return:
        """
        moves = set()
        capture_moves = set()
        if not (self.field_row*self.color_value == 1 or self.field_row*self.color_value == -6):
            self.pot_moves = {(1*self.color_value, 0)}

        for move in self.pot_moves:
            target_row = self.field_row + move[0]
            target_col = self.field_col + move[1]
            if self.path_clear(board, move, target_row, target_col):
                if board.status[target_row, target_col] * self.color_value == 0:
                    moves.add(move)

        for move in self.pot_capture_moves:
            target_row = self.field_row + move[0]
            target_col = self.field_col + move[1]
            if self.path_clear(board, move, target_row, target_col):
                if board.status[target_row, target_col] * self.color_value < 0:
                    capture_moves.add(move)
        self.legal_moves = moves
        self.legal_capture_moves = capture_moves


class Knight(Figure):
    def __init__(self, field, color):
        """
        Class with methods and properties of knights
        :param field: Field of the knight
        :param color: Color (black or white) of the knight
        """
        Figure.__init__(self, field, color)
        self.pot_moves = {(2, 1), (1, 2), (-1, 2), (-2, 1),
                          (-2, -1), (-1, -2), (1, -2), (2, -1)}
        self.value = 2.5 * self.color_value
        self.short_name = self.color[0] + "N"

    def get_legal_moves(self, board):
        """
        get all legal moves from potential moves considering the current board.
        General restrictions:
        - cannot capture-move to a square where a piece of the same color stands
        - cannot capture-move to an empty square
        - cannot move to a square where a piece stands
        :param board: current board
        :return:
        """
        moves = set()
        capture_moves = set()
        for move in self.pot_moves:
            target_row = self.field_row + move[0]
            target_col = self.field_col + move[1]
            if not (target_row > 7 or target_row < 0 or target_col > 7 or target_col < 0):
                if board.status[target_row, target_col] == 0:
                    moves.add(move)
                if board.status[target_row, target_col] * self.color_value < 0:
                    capture_moves.add(move)
        self.legal_moves = moves
        self.legal_capture_moves = capture_moves


class Bishop(Figure):
    def __init__(self, field, color):
        """
        Class with methods and properties of bishops
        :param field: Field of the bishop
        :param color: Color (black or white) of the bishop
        """
        Figure.__init__(self, field, color)
        self.pot_moves = {(i, -i) for i in range(-7, 0)} \
                             | {(i, -i) for i in range(1, 8)} \
                             | {(i, i) for i in range(-7, 0)} \
                             | {(i, i) for i in range(1, 8)}
        self.value = 3.5 * self.color_value
        self.short_name = self.color[0] + "B"


class Rook(Figure):
    def __init__(self, field, color):
        """
        Class with methods and properties of rooks
        :param field: Field of the rook
        :param color: Color (black or white) of the rook
        """
        Figure.__init__(self, field, color)
        self.pot_moves = {(i, 0) for i in range(-7, 0)} \
                         | {(i, 0) for i in range(1, 8)} \
                         | {(0, i) for i in range(-7, 0)} \
                         | {(0, i) for i in range(1, 8)}
        self.value = 5 * self.color_value
        self.short_name = self.color[0] + "R"


class Queen(Figure):
    def __init__(self, field, color):
        """
        Class with methods and properties of Queens
        :param field: Field of the queen
        :param color: Color (black or white) of the queen
        """
        Figure.__init__(self, field, color)
        self.pot_moves = {(i, 0) for i in range(-7, 0)} \
                         | {(i, 0) for i in range(1, 8)} \
                         | {(0, i) for i in range(-7, 0)} \
                         | {(0, i) for i in range(1, 8)} \
                         | {(i, -i) for i in range(-7, 0)} \
                         | {(i, -i) for i in range(1, 8)} \
                         | {(i, i) for i in range(-7, 0)} \
                         | {(i, i) for i in range(1, 8)}
        self.value = 9 * self.color_value
        self.short_name = self.color[0] + "Q"


class King(Figure):
    def __init__(self, field, color):
        """
        Class with methods and properties of kings
        :param field: Field of the king
        :param color: Color (black or white) of the king
        """
        Figure.__init__(self, field, color)
        self.pot_moves = {(1, 0), (1, 1), (0, 1), (-1, 1),
                          (-1, 0), (-1, -1), (0, -1), (1, -1)}
        self.value = 10 * self.color_value
        self.short_name = self.color[0] + "K"
