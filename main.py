import numpy as np


class Cell:
    def __init__(self, val, row, col, box):
        """
        Constructor for a single Sudoku cell

        :param val: The current value of the cell
        :param row: The row the cell is in (unchangeable after init)
        :param col: The column the cell is in (unchangeable after init)
        :param box: The box the cell is in (unchangable after init)
        """
        self.val = val
        self.row = row
        self.col = col
        self.box = box

    #def __str__(self):
     #   return "{}{}{}".format(self.row, self.col, self.box)

    def __str__(self):
        return "{}".format(self.val)

    __repr__ = __str__

class Row:
    def __init__(self):
        self.cells = []

    def add_cell(self, cell):
        self.cells.append(cell)

class Column(Row):
    pass


class Box(Row):
    pass

class Board:
    def __init__(self):
        """
        Constructor for a Sudoku board. Cells are given proper meta values and initialized to 0
        
        """
        self.populate_board()


    def init_board(self):
        cells = []
        for i in range(9):
            for j in range(9):
                new_cell = Cell(0, i, j, (j//3)+(i//3)*3)
                cells.append(new_cell)
        board = np.array(cells)
        board = board.reshape(9, 9)
        return board

    def populate_board(self):
        board = self.init_board()
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(len(board)):
            for j in range(len(board)):
                selected = np.random.randint(1, 10, 1)[0]
                digits.remove(selected)
                board[i][j].val =
        print(board)

    def create_rows_cols_boxes(self):


def test():
    board = Board()

if __name__ == '__main__':
    test()
