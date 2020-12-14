from src.board import Board
from game_setup import FIGURES, FIGURES_DICT

if __name__ == '__main__':
    board = Board(FIGURES)
    turn = "white"
    board.create_board()
    board.display_board()
    predef_moves = [("wP5", "e4"), ("bP4", "d5"),
                    ("wP5", "d5"), ("bQ", "d5"),
                    ("wN1", "c3"), ("bQ", "e6"),
                    ("wK", "e2"), ("wN2", "e2"), ("bN2", "f6")]
    for move in predef_moves:
        figure_to_move = move[0]
        if not figure_to_move.startswith(turn[0]):
            print("It is %s's turn. Please chose a %s piece to move." % (turn, turn))
        else:
            figure_to_move = FIGURES_DICT[figure_to_move]
            if figure_to_move in board.figures:
                if turn == "white":
                    next_turn = "black"
                else:
                    next_turn = "white"
                new_pos = move[1]
                move_done, reason = figure_to_move.move_to(board, new_pos, turn)
                if move_done:
                    board.create_board()
                    board.display_board()
                    turn = next_turn
                else:
                    board.create_board()
                    board.display_board()
                    print(move, ":", reason)
            else:
                print(f"{figure_to_move} not on Board")
