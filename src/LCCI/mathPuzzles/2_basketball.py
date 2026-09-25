"""
Basketball: You have a basketball hoop and someone says that you can play one of two games. Game 1: You get one shot to make the hoop. 
Game 2: You get three shots and you have to make two of three shots.
If p is the probability of making a particular shot, for which values of p should you pick one game or the other?
hints: 
Sequence   Hits   Wins Game 2?   Probability
HHH         3        yes         p · p · p       = p³
HHM         2        yes         p · p · (1-p)   = p²(1-p)
HMH         2        yes         p · (1-p) · p   = p²(1-p)
MHH         2        yes         (1-p) · p · p   = p²(1-p)
HMM         1        no
MHM         1        no
MMH         1        no
MMM         0        no
P(Game 1) = p
P(Game 2) = 3p²(1-p) + p³
          = 3p² - 3p³ + p³
          = 3p² - 2p³
"""
import math
def best_game(p: float) -> str:
    p_g1 , p_g2 = p , 3*(p**2) - 2*(p**3)

    if abs(p_g1 - p_g2) < 1e-12:
        return "Tie"
    # math.isclose(p_g1, p_g2, abs_tol=1e-12)
    return "Game 1" if p_g1 > p_g2 else "Game 2"