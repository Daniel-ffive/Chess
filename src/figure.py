import numpy as np

FIELD_ROW_DICT = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7}
FIELD_COL_DICT = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
COLOR_DICT = {"white": 1, "black": -1}


class Figure:
    def __init__(self, field, color):
        self.field_col = FIELD_COL_DICT[field[0]]
        self.field_row = FIELD_ROW_DICT[field[1]]
        self.color = color
        self.color_value = COLOR_DICT[color]
        self.value = 0
        self.legal_moves = {}

    def move_to(self, new_pos):
        self.field_col = FIELD_COL_DICT[new_pos[0]]
        self.field_row = FIELD_ROW_DICT[new_pos[1]]

    def get_captured(self):
        self.value = 0

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
            if not (target_row > 7 or target_row < 0 or target_col > 7 or target_col < 0):
                row_step = np.sign(move[0])
                col_step = np.sign(move[1])
                sq_cov = sum(board[self.field_row + i * row_step, self.field_col + i * col_step]
                             for i in range(1, abs(move[0])))
                if sq_cov == 0:
                    if board[target_row, target_col] * self.color_value == 0:
                        moves.add(move)
                    if board[target_row, target_col] * self.color_value < 0:
                        capture_moves.add(move)
        self.legal_moves = moves | capture_moves


class Pawn(Figure):
    def __init__(self, field, color):
        """
        Class with methods and properties of pawns
        :param field: Initial field of the pawn
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
        capture_moves = self.pot_capture_moves
        moves = self.pot_moves
        if not (self.field_row * self.color_value == 1 or
                self.field_row * self.color_value == -6):
            moves.remove((2 * self.color_value, 0))
        if not board[self.field_row + 1 * self.color_value,
                     self.field_col + 1] * self.color_value < 0:
            capture_moves.remove((1 * self.color_value, 1))
        if not board[self.field_row + 1 * self.color_value,
                     self.field_col - 1] * self.color_value < 0:
            capture_moves.remove((1 * self.color_value, -1))
        self.legal_moves = moves | capture_moves


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
                if board[target_row, target_col] == 0:
                    moves.add(move)
                if board[target_row, target_col] * self.color_value < 0:
                    capture_moves.add(move)
        self.legal_moves = moves | capture_moves


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


class Board:
    def __init__(self, figures):
        self.figures = figures
        self.status = np.zeros((8, 8))
        self.covered_squares = set()

    def create_board(self):
        self.status = np.zeros((8, 8))
        for figure in self.figures:
            self.status[figure.field_row, figure.field_col] = figure.value

    def display_board(self):
        display = ""
        for row in range(8):
            for col in range(8):
                display += " [  ] "
        for figure in self.figures:
            display = display[:6 * (8 * (7 - figure.field_row) + figure.field_col) + 2] \
                      + figure.short_name \
                      + display[6 * (8 * (7 - figure.field_row) + figure.field_col) + 4:]
        for i in range(7, 0, -1):
            display = display[:i * 6 * 8] + "\n" + display[i * 6 * 8:]
        return display

    def get_covered_squares(self, color):
        for figure in self.figures:
            if figure.color == color:
                figure.get_legal_moves(self.status)
                for move in figure.legal_moves:
                    self.covered_squares.add((figure.field_row + move[0],
                                              figure.field_col + move[1]))
