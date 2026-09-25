"""
Dominos: There is an 8x8 chessboard in which two diagonally opposite corners have been cut off. 
You are given 31 dominos, and a single domino can cover exactly two squares. 
Can you use the 31 dominos to cover the entire board? Prove your answer (by providing an example or showing why it's impossible).

Answer - No, 31 dominoes cannot cover the board.
Color the board like a chessboard. It has 32 black and 32 white squares.
Two diagonally opposite corners, such as (0,0) and (7,7), always have the same color, because their row+column parities match. Removing them leaves 30 of one color and 32 of the other.
Every domino covers two adjacent squares, and adjacent squares always have opposite colors. So each domino covers exactly one black and one white square.
31 dominos would therefore cover 31 black and 31 white squares, but the board has 30 and 32. Contradiction, so no tiling exists.
"""

def can_cover_board()-> bool:
    n = 8
    removed = [(0,0) , (n-1, n-1)]
    counts = []
    for r in range(n):
        for c in range(n):
            if (r,c) not in removed:
                counts[(r+c)% 2] +=1
    return counts[0] == counts[1]