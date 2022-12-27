import numpy as np
import random

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
        return "{}".format(self.val)

    __repr__ = __str__


class Board:
    def __init__(self):
        # INDEX A CELL WITH self.board[row][column]
        """
        Constructor for a Sudoku board. Cells are given proper meta values and initialized to 0
        
        """
        cells = []
        for i in range(9):
            for j in range(9):
                new_cell = Cell(' ', i, j, (j // 3) + (i // 3) * 3)  # change value back to 0
                cells.append(new_cell)
        self.board = np.array(cells)
        self.board = self.board.reshape(9, 9)
        print(self.board)


    def populate_board(self):
        """
        Instance method to populate 17 (the minimum number to have a solvable Sudoku) random cells in
        the board with numbers

        :return: None
        """
        nums = np.arange(1, 10)
        indices = np.arange(0, 9)
        count = 0
        #while nums.size != 0:
         #   herb = np.random.choice(nums, replace=False)
          #  nums = np.delete(nums, np.where(nums == herb))
           # print(herb)
            #print(nums)
        while count < 17:
            row = np.random.choice(indices)
            col = np.random.choice(indices)
            if self.board[row][col].val == 0:
                value = np.random.choice(nums, replace=False)
                self.board[row][col].val = value
                nums = np.delete(nums, np.where(nums == value))
                count += 1
            if nums.size == 0:
                nums = np.arange(1, 10)
        print(self.board)

    def check_val(self, cell1, cell2):
        """
        Instance method to check if two cells share the same value, a helper method for the row and column
        checking methods

        :param cell1: the first cell whose value is to be compared (of type Cell)
        :param cell2: the second cell whose value is to be compared (of type Cell)
        :return: 0 if the cells have the same value, 1 otherwise
        """
        if cell1.val == cell2.val:
            return 0
        else:
            return 1

    def check_row(self, cell):
        """
        Instance method to check if a cell has the same value as another cell in its row

        :param cell: the cell whose value is being checked against every other cell in the row (of
        type Cell)
        :return: 0 if the cell has the same value as another cell in the row, 1 otherwise
        """
        for i in self.board[cell.row][cell.col]:
            flag = self.check_val(i, cell)
            if flag == 0:
                return flag
        return 1

    def check_col(self, cell):
        """
        Instance method to check if a cell has the same value as another cell in its column

        :param cell: the cell whose value is being checked against every other cell in the column
        :return: 0 if the cell has the same value as another cell in the column, 1 otherwise
        """
        for i in range(9):
            flag = self.check_val(self.board[i][cell.col], cell)
            if flag == 0:
                return flag
        return 1

    def check_box(self, cell):
        """
        Instance method to check if a cell has the same value as anther cell in its box

        :param cell: the cell whose value is being checked against every other cell in the box
        :return: 0 if the cell has the same value as another cell in the column, 1 otherwise
        """






def test():
    board = Board()
    board.populate_board()


if __name__ == '__main__':
    test()
