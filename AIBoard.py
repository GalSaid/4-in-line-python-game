from Board import Board
import random


class AIBoard(Board):
    EMPTY = 0  # sign of empty location
    WINDOW_LENGTH = 4
    PLAYER_PIECE = 1
    AI_PIECE = 2

    @staticmethod
    def evaluate_window(window, piece):
        """
        This function calculate the score of this window(a sequence of 4).
        :param: piece and list of 4 locations in sequence
        :type: list and integer
        :return: socre the symbolizes  higher is better
        :rtype: integer
        """
        score = 0
        opp_piece = AIBoard.PLAYER_PIECE
        if piece == AIBoard.PLAYER_PIECE:
            opp_piece = AIBoard.AI_PIECE
        if window.count(piece) == 3 and window.count(AIBoard.EMPTY) == 1:
            score += 1001
        elif window.count(piece) == 2 and window.count(AIBoard.EMPTY) == 2:
            score += 10
        if window.count(opp_piece) == 3 and window.count(AIBoard.EMPTY) == 1:  # Blocks the opponent from winning
            score += 120
        return score

    def score_position(self, piece, col):
        """
        The function goes through all the options of a window (row, column, ascending diagonal, descending diagonal)
        in size 4 that the column we are checking  is included in it.
        :param: piece that we want drop and the colum we check in order to know if it is worth putting the piece there.
        :type: integers
        :return: socre the symbolizes  higher is better
        :rtype: integer
        """
        score = 0
        r = self.get_next_free_row(col)  # Check the location (r, col)
        # score vertical
        col_array = [int(i) for i in list(self.board[:, col])]  # Returns a list of all the values in the column
        for row in range(self.rows - 3):
            if row <= r < row + AIBoard.WINDOW_LENGTH:  # check if the row we check will be in the window
                window = col_array[row:row + AIBoard.WINDOW_LENGTH]
                score += AIBoard.evaluate_window(window, piece)

        # score Horizontal
        row_array = [int(i) for i in list(self.board[r, :])]  # Returns a list of all the values in the row
        for c in range(self.cols - 3):
            if c <= col < c + AIBoard.WINDOW_LENGTH:  # check if the col we check will be in the window
                window = row_array[c:c + AIBoard.WINDOW_LENGTH]
                score += AIBoard.evaluate_window(window, piece)

        # score ascending diagonal
        for row in range(self.rows - 3):
            for c in range(self.cols - 3):
                if c <= col < c + AIBoard.WINDOW_LENGTH and row <= r < row + AIBoard.WINDOW_LENGTH:  # Checks whether
                    # the position that is given a score will be in the window
                    window = [self.board[row + i][c + i] for i in range(AIBoard.WINDOW_LENGTH)]
                    score += AIBoard.evaluate_window(window, piece)

        # score descending diagonal
        for row in range(self.rows - 3):
            for c in range(self.cols - 3):
                if c <= col < c + AIBoard.WINDOW_LENGTH and row <= r < row + AIBoard.WINDOW_LENGTH:  # Checks whether
                    # the position that is given a score will be in the window
                    window = [self.board[row + 3 - i][c + i] for i in range(AIBoard.WINDOW_LENGTH)]
                    score += AIBoard.evaluate_window(window, piece)
        return score

    def get_best_move(self, piece):
        """
        The function return the best column for the computer to drop the piece.
        :param: piece that we want drop
        :type: integer
        :return: the colum with the best score
        :rtype: integer
        """
        valid_locations = self.get_valid_locations()
        best_score = 0
        best_col = random.choice(valid_locations)  # Randomly selects a column from the valid columns
        for c in valid_locations:  # pass over all the columns that return from the function above
            score = self.score_position(piece, c)  # give for each col score
            if score > best_score:  # if this score is higher -> save the best score
                best_score = score
                best_col = c
        return best_col
