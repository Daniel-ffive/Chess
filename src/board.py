import numpy as np
from src.figure import King, Pawn


class Board:
    def __init__(self, figures):
        self.figures = figures
        self.status = np.zeros((8, 8))
        self.covered_squares = set()
        self.in_check = "None"

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
        print("-------------------------------\n")
        print(display)
        return display

    def get_covered_squares(self, color):
        for figure in self.figures:
            if figure.color == color:
                if not isinstance(figure, Pawn):
                    figure.get_legal_moves(self)
                    for move in figure.legal_moves | figure.legal_capture_moves:
                        self.covered_squares.add((figure.field_row + move[0],
                                                  figure.field_col + move[1]))
                else:
                    for move in figure.pot_capture_moves:
                        target_row = figure.field_row + move[0]
                        target_col = figure.field_col + move[1]
                        if not (target_row > 7 or target_row < 0
                                or target_col > 7 or target_col < 0):
                            self.covered_squares.add((target_row, target_col))

    def king_in_check(self, color):
        if color == "white":
            op_color = "black"
        else:
            op_color = "white"
        self.get_covered_squares(op_color)
        for figure in self.figures:
            if figure.color != op_color and isinstance(figure, King):
                if (figure.field_row, figure.field_col) in self.covered_squares:
                    self.in_check = color
                else:
                    self.in_check = "None"
