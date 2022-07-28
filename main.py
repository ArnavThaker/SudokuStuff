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

    def __str__(self):
        return "Value is {}, row is {}, col is {}, box is {}".format(self.val, self.row, self.col, self.box)


class Board:
    def __init__(self):
        cells = []
        """
        Constructor for a Sudoku board. Cells are given proper meta values and initialized to 0
        
        Test commit and push
        """
        for i in range(9):
            for j in range(9):
                new_cell = Cell(0, i, j, (j//3)+(i//3)*3)
                cells.append(new_cell)
        np_cells = np.array(cells)
        np_cells.reshape(9, 9)
        print(np_cells)


    #def populate_board(self):



def test():
    board = Board()

if __name__ == '__main__':
    test()
