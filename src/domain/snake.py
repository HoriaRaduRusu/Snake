from dataclasses import dataclass

from domain.cell import Cell


@dataclass
class Snake:
    _head: Cell
    _body: list
    _direction: str = "up"

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, new_head):
        self._head = new_head

    @property
    def body(self):
        return self._body

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, new_direction):
        self._direction = new_direction

    def move_snake_without_eating(self, new_head_row, new_head_column):
        self.move_snake_with_eating(new_head_row, new_head_column)
        return self._body.pop()

    def move_snake_with_eating(self, new_head_row, new_head_column):
        self._body.insert(0, Cell(self.head.row, self.head.column, "+"))
        self._head = Cell(new_head_row, new_head_column, "*")

    def check_snake_intact(self):
        for snake_body_cell in self._body:
            if self._head.row == snake_body_cell.row and self._head.column == snake_body_cell.column:
                return False
        return True
