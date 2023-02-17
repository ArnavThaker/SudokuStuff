import numpy as np
import gui


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
        nums = np.arange(1, 10)
        cells = []
        for i in range(9):
            for j in range(9):
                new_cell = Cell(0, i, j, (j // 3) + (i // 3) * 3)  # change value back to 0
                cells.append(new_cell)
        self.board = np.array(cells)
        self.board = self.board.reshape(9, 9)

    def populate_board(self):
        """
        Instance method to populate 17 (the minimum number to have a solvable Sudoku) random cells in
        the board with numbers

        :return: None
        """
        nums = np.arange(1, 10)
        indices = np.arange(0, 9)
        for i in range(17):
            cell = self.board[np.random.choice(indices)][np.random.choice(indices)]
            while cell.val != 0:
                cell = self.board[np.random.choice(indices)][np.random.choice(indices)]
            while self.check_row(cell) + self.check_col(cell) + self.check_box(cell) != 3:
                value = np.random.choice(nums, replace=False)
                cell.val = value
            nums = np.delete(nums, np.where(nums == value))
            if nums.size == 0:
                nums = np.arange(1, 10)

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
        for i in self.board[cell.row]:
            flag = self.check_val(i, cell)
            if i != cell and flag == 0:
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
            if self.board[i][cell.col] != cell and flag == 0:
                return flag
        return 1

    def check_box(self, cell):
        """
        Instance method to check if a cell has the same value as anther cell in its box

        :param cell: the cell whose value is being checked against every other cell in the box
        :return: 0 if the cell has the same value as another cell in the column, 1 otherwise
        """
        box_coords = {
            0: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
            1: [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
            2: [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
            3: [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
            4: [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
            5: [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
            6: [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
            7: [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
            8: [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)],
        }
        box = cell.box
        for i in box_coords[box]:
            flag = self.check_val(cell, self.board[i[0]][i[1]])
            if self.board[i[0]][i[1]] != cell and flag == 0:
                return flag
        return 1

    def is_valid(self, cell):
        """
        Instance method and helper for solve() that determines if a cell placement is valid per Sudoku rules

        :param cell: a cell that is being placed in the board
        :return: 1 if the cell is a valid placement, 0 otherwise
        """
        if self.check_row(cell) + self.check_col(cell) + self.check_box(cell) == 3:
            return 1
        else:
            return 0

    def find_empty(self):
        for i in self.board:
            for j in i:
                if j.val == 0:
                    return j.row, j.col
        return -1, -1

    def solve(self):
        nums = np.arange(1, 10)
        index = self.find_empty()
        if index[0] == -1 and index[1] == -1:
            return 1
        cell = self.board[index[0]][index[1]]
        for i in nums:
            cell.val = i
            if self.is_valid(cell):
                if self.solve():
                    return 1
            else:
                cell.val = 0
        return 0

    def final_check(self):
        for i in self.board:
            for j in i:
                if self.check_row(j) + self.check_col(j) + self.check_box(j) != 3:
                    return 0
        return 1

def test():
    board = Board()
    board.populate_board()
    print("Board before solving: \n", board.board)
    board.solve()
    if board.final_check():
        print("\nBoard after solving: \n", board.board)
    else:
        print("Sudoku Solve failed")


if __name__ == '__main__':
    test()
