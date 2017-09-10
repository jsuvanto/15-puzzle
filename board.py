import random

# String used to represent the empty tile.
EMPTYSTRING = "*"

# Moves are stored in a dictionary to access them easily.
# Consider self.__empty and MOVES[direction] as vectors. The sum of
# these two vectors is the new position of the empty tile.
MOVES = {"u": [-1, 0], "d": [1, 0], "l": [0, -1], "r": [0, 1]}


class Board:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__size = rows * cols

        # Initialize the board data structure as a list of lists.
        # __board consists of lists, each representing a row.
        # Each row consists of integers representing tiles or
        # EMPTYSTRING representing the empty tile.
        self.__board = []

        # Fill the board with tiles, except leave the last tile empty.
        tilecount = 1
        for row in range(rows):
            self.__board.append([])
            for col in range(cols):
                if tilecount == self.__size:
                    self.__board[row].append(EMPTYSTRING)
                else:
                    self.__board[row].append(tilecount)
                    tilecount += 1

        # Remember the location of the empty tile
        self.__empty = [rows - 1, cols - 1]

    # Draw the board. TODO: consider changing this to __repr__
    def draw(self):
        for row in self.__board:
            for col in row:
                print("{:>3}".format(str(col)), end="")
            print()
        print()

    # Return a list of all legal moves for the empty tile.
    # u = up, d = down, l = left, r = right
    def legalmoves(self):
        moves = []
        if self.__empty[0] > 0:
            moves.append("u")
        if self.__empty[0] < self.__rows - 1:
            moves.append("d")
        if self.__empty[1] > 0:
            moves.append("l")
        if self.__empty[1] < self.__cols - 1:
            moves.append("r")
        return moves

    # Move the empty tile in a direction
    # direction must be a string "u", "d", "l" or "r"
    # u = up, d = down, l = left, r = right
    def move(self, direction):
        # Check if the requested move is legal.
        if direction in self.legalmoves():
            # Store the current position of the empty tile
            curr_x, curr_y = self.__empty
            # Calculate the new position of the empty tile with a "vector sum".
            new_x = self.__empty[0] + MOVES[direction][0]
            new_y = self.__empty[1] + MOVES[direction][1]

            # Copy the tile in new empty position to current empty position.
            self.__board[curr_x][curr_y] = self.__board[new_x][new_y]

            # Move empty tile to new empty position.
            self.__empty = [new_x, new_y]
            self.__board[new_x][new_y] = EMPTYSTRING
            return True
        else:
            # If the move is illegal, do nothing and return false.
            return False

    # Shuffle the board by randomly moving the empty tile around "moves" times
    # and return the sequence of moves.
    def shuffle(self, moves):
        movecount = 0
        movesequence = ""
        while movecount < moves:
            direction = random.choice("udlr")
            if self.move(direction):
                movecount += 1
                # Debug information
                movesequence += direction
        return movesequence