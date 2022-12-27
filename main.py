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
                new_cell = Cell(0, i, j, (j // 3) + (i // 3) * 3)  # change value back to 0
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





def test():
    board = Board()
    board.populate_board()


if __name__ == '__main__':
    test()
