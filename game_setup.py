from src.figure import Pawn, Rook, Knight, Bishop, Queen, King
# Initial setup:
# white
wP1 = Pawn("a2", "white")
wP2 = Pawn("b2", "white")
wP3 = Pawn("c2", "white")
wP4 = Pawn("d2", "white")
wP5 = Pawn("e2", "white")
wP6 = Pawn("f2", "white")
wP7 = Pawn("g2", "white")
wP8 = Pawn("h2", "white")
wR1 = Rook("a1", "white")
wR2 = Rook("h1", "white")
wN1 = Knight("b1", "white")
wN2 = Knight("g1", "white")
wB1 = Bishop("c1", "white")
wB2 = Bishop("f1", "white")
wQ = Queen("d1", "white")
wK = King("e1", "white")
# black
bP1 = Pawn("a7", "black")
bP2 = Pawn("b7", "black")
bP3 = Pawn("c7", "black")
bP4 = Pawn("d7", "black")
bP5 = Pawn("e7", "black")
bP6 = Pawn("f7", "black")
bP7 = Pawn("g7", "black")
bP8 = Pawn("h7", "black")
bR1 = Rook("a8", "black")
bR2 = Rook("h8", "black")
bN1 = Knight("b8", "black")
bN2 = Knight("g8", "black")
bB1 = Bishop("c8", "black")
bB2 = Bishop("f8", "black")
bQ = Queen("d8", "black")
bK = King("e8", "black")
# list of figures:
FIGURES = [wP1, wP2, wP3, wP4, wP5, wP6, wP7, wP8,
           wR1, wR2, wN1, wN2, wB1, wB2, wQ, wK,
           bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8,
           bR1, bR2, bN1, bN2, bB1, bB2, bQ, bK]
# figure string to instance
FIGURES_DICT = {"wP1": wP1, "wP2": wP2, "wP3": wP3, "wP4": wP4,
                "wP5": wP5, "wP6": wP6, "wP7": wP7, "wP8": wP8,
                "wR1": wR1, "wR2": wR2, "wN1": wN1, "wN2": wN2,
                "wB1": wB1, "wB2": wB2, "wQ": wQ, "wK": wK,
                "bP1": bP1, "bP2": bP2, "bP3": bP3, "bP4": bP4,
                "bP5": bP5, "bP6": bP6, "bP7": bP7, "bP8": bP8,
                "bR1": bR1, "bR2": bR2, "bN1": bN1, "bN2": bN2,
                "bB1": bB1, "bB2": bB2, "bQ": bQ, "bK": bK}