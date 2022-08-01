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

    def __str__(self):
        return "{}".format(self.cells)

    __repr__ = __str__

class Column(Row):
    pass


class Box(Row):
    pass

class Board:
    def __init__(self):
        """
        Constructor for a Sudoku board. Cells are given proper meta values and initialized to 0
        
        """
        self.create_rows()


    def init_board(self):
        cells = []
        for i in range(9):
            for j in range(9):
                new_cell = Cell(i, i, j, (j//3)+(i//3)*3) # change value back to 0
                cells.append(new_cell)
        board = np.array(cells)
        board = board.reshape(9, 9)
        return board

    def create_rows(self):
        rows = []
        board = self.init_board()
        for i in board:
            current_row = Row()
            for j in i:
                current_row.add_cell(j)
            rows.append(current_row)
        return rows

    def create_cols(self):





def test():
    board = Board()

if __name__ == '__main__':
    test()
