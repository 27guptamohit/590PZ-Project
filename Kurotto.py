# Name: Mohit Gupta
# NetID: mohitg2


# Game: Kurotto
# Game Link: https://www.gmpuzzles.com/blog/kurotto-rules-and-info/

# About: Kurotto is one of the rarest and brilliant Japenese games which requires the players to fill up the
# cells adjacent to the numbered cells and exactly the same number as mentioned in the circled number.
# If any adjacent cell adds up to the sum more than the mentioned in the adjacent circled number, then the solution or that
# particular move is said to be void.

# Approach: Brute Force
# Additional Attempts: 1. (Branch & Bound [Uses Depth First Search]), 2. (Backtracking [Uses Breadth First Search])

# Problem Statement:

# As the game is having very less number of devised puzzle options, I wanted to generate all the legal possible
# and valid game boards for the game. Below are the variations that I want to try:

# 1. Generating squared board game from size 1 x 1 upto 10 x 10.
# Example of board size 2 x 2, total cells = 4

# 2. To find out possible number of numbered circles that can be inserted in every board.
# Example, board 2 x 2 can have (4 - 1) as the highest number with range from [ (0) to (4-1) ]

# 3. To find the maximum number of circled numbers that can be inserted in every board.
# Example, board 2 x 2 can have one circled number, two circled numbers or three circled numbers.

# 4. Different ways in which the empty circled numbers can be arranged in the board itself.
# Example, for board 2 x 2 with two numbered circles, you can have C(4, 2) = 6, possible arrangement options.

# Once the board is generated, you can easily find the solution by applying Bounding Functions.


# Generating variations of puzzle is the main task of this problem statement.

# Like we all have certain fears, I was also scared to develop codes using OOP. My past assignments were never
# written using OOP. I certainly had a good command over mathematics and coding but the moment I saw "self" in a script,
# I got confused every single time. I wanted to remove this confusion so developing the final game on OOP.

# Solution:


import numpy as np
from itertools import combinations
import itertools as it


class Kurotto():


    def __init__(self, grid_size = 2):
        """
        I'm taking the size of the grid as an input in the __name__ by the user.
        The options are limited only from 2 x 2 to 10 x 10.

        :param grid_size: The size of the grid as input by the user
        """

        self.grid_size = grid_size


    def grid_coordinates_structure(self):
        """
        This function's only work is to generate the coordinates of the grid of the selected size and
        an empty numpy array.

        :return: The list containing the tuple of coordinates, and an empty grid structure of the user selected size
        """

        coordinates = []

        for i in range(self.grid_size):

            for j in self.grid_size:

                b = (i, j)
                coordinates.append(b)


        grid_structure = np.empty((self.grid_size,self.grid_size), dtype = str )


        return coordinates, grid_structure


    def possible_number_of_circled_numbers(self):
        """
        For example, in a grid of 2 x 2, there are 4 cells in total.
        There needs to be at least one grid empty so that a solution could be possible.
        In this case, the max number of circled numbers can be 4-1 = 3

        :return: possibile number of circled number that can occupy the grid
        """


        possibilities = (self.grid_size ** 2) - 1

        return possibilities



    def possible_combination_of_circled_numbers(self, possibilities, coordinates):
        """
        I learnt the use of itertools from the below link:
        https://www.geeksforgeeks.org/itertools-combinations-module-python-print-possible-combinations/


        Here, I am generating the total number of possible variations according to the number of circled numbers present
        in the grid.

        For example, in a grid of 2 x 2, when one circled number is allowed, then it will have
        C(4,1) possible variations possible = 4.
        C(4, 2), possible variations = 6
        C(4, 3), possible variations = 4


        For a grid of 3 x 3, possible variations:
        C(9, 1) = 9 Variations
        C(9, 2) = 36 Variations
        C(9, 3) = 84 Variations
        C(9, 4) = 126 Variations
        C(9, 4) = 126 Variations
        C(9, 3) = 84 Variations
        C(9, 2) = 36 Variations
        C(9, 1) = 9 Variations


        :param possibilities: Total number of circled numbers that can be present in the grid
        :param coordinates: Coordinates of the grid of the requested size

        :return: A dictionary where the key represents the number of circled numbers in the grid,
                 and values represent the set of possible coordinates for each possible variation.
        """

        possible_combinations = {}


        for i in range(1, possibilities+1):
            # " i " means that for example, in a grid of 2 x 2, how many circled numbers are present.

            a = list(combinations(coordinates, i))

            possible_combinations[i] = a

        return possible_combinations



    def possible_permutation_of_numbers_in_range(self, possible_combination, possibilities):
        """
        In the function, possible_combination_of_circled_numbers, I found out that where the circles can be placed
        in the grid.

        Now in this function, I will find out that in the grid of every possible combination previously,
        what are the possible PERMUTATIONS WITH REPETITION of the range of numbers that I can introduce in every
        single grid.

        Thus, the dictionary that I will return will have every possible formation of puzzle which I can later
        break down into the ones which are valid.

        I am not removing them now as I want to visually analyze it.


        :return: Final dictionary of all the possibilities
        """

        possible_combinations = possible_combination
        possibilities1 = possibilities

        all_the_possibilities = {}

        # Below variable contains the dictionary of

        for key, values in possible_combinations.items():

            for i in values:
                b[i] = [x for x in it.product(range(possibilities+1), repeat=key)]

        return all_the_possibilities








if __name__ == "__main__":
   while True:
       try:
           a = int(input("Please enter the length of the square grid from 2 to 10:"))
           if a in range(2, 11):
            break
       except:
           print("Please print the NUMBER from the given range only")

   grid_1 = Kurotto(a)









