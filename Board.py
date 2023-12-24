import numpy as np


class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols))

    def getBoard(self):  # This function return the matrix of the board
        return self.board

    def drop_piece(self, row, col, piece):  # put the piece in the location we got
        self.board[row][col] = piece

    def is_valid_location(self, col):  # check if there is a place in the col
        return self.board[self.rows - 1][col] == 0

    def get_valid_locations(self):
        """
        The function goes through all the columns in the board and returns a list of all the valid columns that are
        not yet full.
        """
        valid_locations = []
        for col in range(self.cols):
            if self.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

    def get_next_free_row(self, col):
        """
        This function find the first free row in this columמ
        :param: specific col
        :type: integer
        :return: the next free row
        :rtype: integer
        """
        for r in range(self.rows):
            if self.board[r][col] == 0:
                return r

    def win_on_the_board(self, piece):
        """
        This function check if there is victory of the player somewhere in the board.
        :param: piece that symbolizes the player
        :type: integer
        :return: true or false
        :rtype: boolean
        """
        # check vertical locations for win
        for r in range(self.rows - 3):
            for c in range(self.cols):
                if self.board[r][c] == piece and self.board[r + 1][c] == piece and self.board[r + 2][c] == piece and \
                        self.board[r + 3][c] == piece:
                    return True

        # check horizontal locations for win
        for r in range(self.rows):
            for c in range(self.cols - 3):
                if self.board[r][c] == piece and self.board[r][c + 1] == piece and self.board[r][c + 2] == piece \
                        and self.board[r][c + 3] == piece:
                    return True

        # check ascending diagonal
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                if self.board[r][c] == piece and self.board[r + 1][c + 1] == piece and self.board[r + 2][c + 2] ==\
                        piece and self.board[r + 3][c + 3] == piece:
                    return True

        # check descending diagonal
        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                if self.board[r][c] == piece and self.board[r - 1][c + 1] == piece and self.board[r - 2][c + 2] ==\
                        piece and self.board[r - 3][c + 3] == piece:
                    return True
        return False

    def place_is_over(self):  # Checks if there is no free space on the board
        if len(self.get_valid_locations()) == 0:
            return True
        else:
            return False

    def __str__(self):
        # Flip 2-D array vertically
        return str(np.flip(self.board, 0))
