from src.figure import Board
from game_setup import FIGURES, FIGURES_DICT

if __name__ == '__main__':
    board = Board(FIGURES)
    turn = "white"
    board.create_board()
    board.display_board()
    while True:
        print("pieces: ", [name for name in FIGURES_DICT.keys()
                           if FIGURES_DICT[name].value != 0
                           and name.startswith(turn[0])])
        figure_to_move = input(f"{turn} to move, chose piece to move from list above: ")
        if not figure_to_move.startswith(turn[0]):
            print("It is %s's turn. Please chose a %s piece to move." % (turn, turn))
        else:
            if figure_to_move in FIGURES_DICT.keys():
                if turn == "white":
                    next_turn = "black"
                elif turn == "black":
                    next_turn = "white"
                figure_to_move = FIGURES_DICT[figure_to_move]
                new_pos = input("Move to: ")
                if figure_to_move.move_to(board, new_pos, turn):
                    print(board.covered_squares)
                    board.create_board()
                    board.display_board()
                    turn = next_turn
                else:
                    print("illegal move, chose another one.")
            else:
                print(f"{figure_to_move} not on Board")
