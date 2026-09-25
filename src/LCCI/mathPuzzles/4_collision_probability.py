"""
how do i solve for this CTCI problem Ants on a Triangle: There are three ants on different vertices of a triangle.
What is the probability of collision (between any two or all of them) if they start walking on the sides of the triangle? Assume that each ant randomly picks a direction, with either direction being equally likely to be chosen, and that they walk at the same speed. 
Similarly, find the probability of collision with n ants on an n-vertex polygon.
Answer - 
What counts as a collision? Two ants meet when they're on the same edge heading toward each other.
What are the choices? Each ant has 2 options, so there are 2³ = 8 equally likely outcomes.

If all ants walk clockwise, each one chases the ant ahead of it at the same speed. They never meet.
If all walk counterclockwise, same story.
If the directions are mixed, walk around the triangle and you'll hit a spot where an ant going clockwise is followed by an ant 
going counterclockwise. Those two are on the same edge, heading toward each other. Collision.
So the only safe outcomes are "everyone clockwise" or "everyone counterclockwise": 2 safe outcomes out of 2³.
P(no collision) = 2 / 2^3
P(collision) = 1 - (2 / 2 ^ 3)
"""

def collision_probability(n) -> bool:
    return 1 - (2 / (2 ** n) )
