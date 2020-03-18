import numpy

class Board:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = numpy.zeros((rows, columns))

    def get_board(self):
        return self.board

    def get_next_open_row(self, column):
        for row in range(self.rows):
            if self.board[row][column] != 0:
                return row - 1
        return self.rows - 1

    def add_chip(self, column, chip):
        if self.is_position_free_in_column(column):
            self.board[self.get_next_open_row(column)][column] = chip

    def is_position_free_in_column(self, column):
        return self.get_next_open_row(column) >= 0

    def winning_move(self, chip):
        ##################
        ### check draw ###
        for column in range(self.columns):
            for row in range(self.rows):
                if self.board[row][column] != 0:
                    return False

        ############################
        ### check horizontal win ###
        for column in range(self.columns -3):
            for row in range(self.rows):
                if self.board[row][column] == chip and self.board[row][column +1] == chip and self.board[row][column +2] == chip and self.board[row][column +3] == chip:
                    return True

        ##########################
        ### check vertikal win ###
        for column in range(self.columns):
            for row in range(self.rows -3):
                if self.board[row][column] == chip and self.board[row +1][column] == chip and self.board[row +2][column] == chip and self.board[row +3][column] == chip:
                    return True

        ##########################
        ### check diagonal win ###
        for column in range(self.columns -3):
            for row in range(self.rows -3):
                if self.board[row][column] == chip and self.board[row +1][column +1] == chip and self.board[row +2][column +2] == chip and self.board[row +3][column +3] == chip:
                    return True
        
        #####################################
        ### check diagonal win in reverse ###
        for column in range(self.columns -3):
            for row in range(3, self.rows):
                if self.board[row][column] == chip and self.board[row -1][column +1] == chip and self.board[row -2][column +2] == chip and self.board[row -3][column +3] == chip:
                    return True
