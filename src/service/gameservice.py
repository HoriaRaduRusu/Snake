from random import choice

from domain.cell import Cell
from domain.snake import Snake


class GameService:
    def __init__(self, board, apple_count):
        self.__board = board
        self.__apple_count = apple_count
        self.__snake = self.place_snake()
        self.__snake_directions = {"up": [-1, 0], "down": [1, 0], "right": [0, 1], "left": [0, -1]}

    def place_snake(self):
        dimension = self.__board.dimension
        snake_head = Cell(dimension // 2 - 1, dimension // 2, "*")
        snake_body = [Cell(dimension // 2, dimension // 2, "+"), Cell(dimension // 2 + 1, dimension // 2, "+")]
        return Snake(snake_head, snake_body, "up")

    def place_apples(self):
        apple_count = 0
        can_be_placed = True
        while apple_count < self.__apple_count and can_be_placed:
            can_be_placed = self.place_apple()
            if can_be_placed:
                apple_count += 1
        self.__apple_count = apple_count

    def place_apple(self):
        """
        Places an apple on the board if possible.
        :return: True if the apple could be placed, otherwise False
        """
        empty_cells = self.__board.get_empty_cells()
        index = 0
        while index < len(empty_cells):
            if not self.check_space_validity_for_apple_placement(empty_cells[index].row, empty_cells[index].column):
                empty_cells.pop(index)
            else:
                index += 1
        if len(empty_cells) != 0:
            apple_cell = choice(empty_cells)
            self.change_cell_value(apple_cell.row, apple_cell.column, ".")
            return True
        return False

    def check_space_validity_for_apple_placement(self, row, column):
        """
        Checks if a given space on the board is a valid placement for an apple
        :param row: The row of the space
        :param column: The column of the space
        :return: True if it's a valid placement for an apple, otherwise False
        """
        if self.__board.get_cell_value(row, column) != " ":
            return False
        if row != 0 and self.__board.get_cell_value(row - 1, column) == ".":
            return False
        if row != self.__board.dimension - 1 and self.__board.get_cell_value(row + 1, column) == ".":
            return False
        if column != 0 and self.__board.get_cell_value(row, column - 1) == ".":
            return False
        if column != self.__board.dimension - 1 and self.__board.get_cell_value(row, column + 1) == ".":
            return False
        return True

    def check_space_inside_board(self, row, column):
        return 0 <= row <= self.__board.dimension - 1 and 0 <= column <= self.__board.dimension - 1

    def draw_snake(self, removed_bit=None):
        """
        Draws the snake on the board
        :param removed_bit: The space that the snake lost, representing the old end of his tail
        :return: nothing
        """
        if removed_bit is not None:
            self.change_cell_value(removed_bit.row, removed_bit.column, " ")
        self.change_cell_value(self.__snake.head.row, self.__snake.head.column, "*")
        for snake_cell in self.__snake.body:
            self.change_cell_value(snake_cell.row, snake_cell.column, snake_cell.value)

    def move_snake(self):
        """
        Moves the snake one space in its current direction
        :return: True if the game is over after the move (meaning the snake is out of the board or ate itself),
        otherwise False
        """
        new_head_cell_row = self.__snake.head.row + self.__snake_directions[self.__snake.direction][0]
        new_head_cell_column = self.__snake.head.column + self.__snake_directions[self.__snake.direction][1]
        if self.check_space_inside_board(new_head_cell_row, new_head_cell_column):
            current_cell_value = self.__board.get_cell_value(new_head_cell_row, new_head_cell_column)
            if current_cell_value == ".":
                # If the snake eats an apple, we increase its length by one and place a new apple
                self.__snake.move_snake_with_eating(new_head_cell_row, new_head_cell_column)
                self.draw_snake()
                apple_could_be_placed = self.place_apple()
                if not apple_could_be_placed:
                    self.__apple_count -= 1
            else:
                # If the snake did not eat an apple, we just move him and check if it ate itself
                removed_bit = self.__snake.move_snake_without_eating(new_head_cell_row, new_head_cell_column)
                if self.__snake.check_snake_intact():
                    self.draw_snake(removed_bit)
                else:
                    return True
            return False
        return True

    def turn(self, direction):
        """
        Turns the snake if the given direction is a valid turn. If the snake tries to turn the way it's already going,
        do nothing.
        :param direction: The way the snake will turn
        :return: True if the game ends after the turn, otherwise False
        Raise ValueError if the snake tries to do a 180 degree turn
        """
        snake_directions = ["up", "left", "right", "down"]
        if direction == self.__snake.direction:
            return False
        if snake_directions.index(direction) + snake_directions.index(self.__snake.direction) == 3:
            raise ValueError("The snake cannot do a 180 degree turn!")
        self.__snake.direction = direction
        return self.move_snake()

    def change_cell_value(self, row, column, value):
        self.__board.change_cell(row, column, value)

    def set_up(self):
        """
        Sets up the initial state of the board
        :return: nothing
        """
        self.place_snake()
        self.draw_snake()
        self.place_apples()

    def get_board_for_printing(self):
        return str(self.__board)
