# 590PZ-Project

# Name: Mohit Gupta
# NetID: mohitg2


# Game: Kurotto
# Game Link: https://www.gmpuzzles.com/blog/kurotto-rules-and-info/

# About: 
Kurotto is one of the rarest and brilliant Japenese games which requires the players to fill up the
cells adjacent to the numbered cells and exactly the same number as mentioned in the circled number.
If any adjacent cell adds up to the sum more than the mentioned in the adjacent circled number, then the solution or that
particular move is said to be void.

# Approach: Brute Force
# Additional Attempts: 1. (Branch & Bound [Uses Depth First Search]), 2. (Backtracking [Uses Breadth First Search])

# Problem Statement:

As the game is having very less number of devised puzzle options, I wanted to generate all the legal possible
and valid game boards for the game. Below are the variations that I want to try:

# 1. Generating squared board game from size 1 x 1 upto 10 x 10.
Example of board size 2 x 2, total cells = 4

# 2. To find out possible number of numbered circles that can be inserted in every board.
Example, board 2 x 2 can have (4 - 1) as the highest number with range from [ (0) to (4-1) ]

# 3. To find the maximum number of circled numbers that can be inserted in every board.
Example, board 2 x 2 can have one circled number, two circled numbers or three circled numbers.

# 4. Different ways in which the empty circled numbers can be arranged in the board itself.
Example, for board 2 x 2 with two numbered circles, you can have C(4, 2) = 6, possible arrangement options.

Once the board is generated, you can easily find the solution by applying Bounding Functions.


Generating variations of puzzle is the main task of this problem statement.

Like we all have certain fears, I was also scared to develop codes using OOP. My past assignments were never
written using OOP. I certainly had a good command over mathematics and coding but the moment I saw "self" in a script,
I got confused every single time. I wanted to remove this confusion so developing the final game on OOP.

