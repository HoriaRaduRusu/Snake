from texttable import Texttable

from domain.cell import Cell


class Board:
    def __init__(self, dimension):
        self.__dimension = dimension
        self.__board = self.__create_board()

    @property
    def dimension(self):
        return self.__dimension

    def get_cell_value(self, row, column):
        return self.__board[row][column].value

    def change_cell(self, row, column, new_value):
        self.__board[row][column].value = new_value

    def __create_board(self):
        return [[Cell(row, column, " ") for column in range(self.__dimension)] for row in range(self.__dimension)]

    def get_empty_cells(self):
        empty_cells = []
        for row in self.__board:
            empty_cells += list(filter(lambda x: x.value == " ", row))
        return empty_cells

    def __str__(self):
        table = Texttable()
        for row in range(self.__dimension):
            table.add_row([x.value for x in self.__board[row]])
        return table.draw()
