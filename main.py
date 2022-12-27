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
        cells = []
        for i in range(9):
            for j in range(9):
                new_cell = Cell(' ', i, j, (j // 3) + (i // 3) * 3)  # change value back to 0
                cells.append(new_cell)
        self.board = np.array(cells)
        self.board = self.board.reshape(9, 9)
        print(self.board)
        self.rows = self.create_rows()
        self.cols = self.create_cols()
        self.boxes = self.create_boxes()


    def create_rows(self):
        rows = []
        for i in self.board:
            current_row = Row()
            for j in i:
                current_row.add_cell(j)
            rows.append(current_row)
        # subscript family with object[row][0].cells[col]
        return rows

    def create_cols(self):
        cols = []
        for i in range(9):
            current_col = Column()
            for j in self.board[0:9, i]:
                current_col.add_cell(j)
            cols.append(current_col)
        return cols

    def create_boxes(self):
        boxes = []
        for i in range(3):
            current_box = Box()
            for j in self.board[(i//3)*3:(i//3)*3+3, i*3:i*3+3]:
                for k in j:
                    current_box.add_cell(k)
            boxes.append(current_box)
        for i in range(3, 6):
            current_box = Box()
            for j in self.board[(i//3)*3:(i//3)*3+3, (i-3)*3:(i-3)*3+3]:
                for k in j:
                    current_box.add_cell(k)
            boxes.append(current_box)
        for i in range(6, 9):
            current_box = Box()
            for j in self.board[(i//3)*3:(i//3)*3+3, (i-6)*3:(i-6)*3+3]:
                for k in j:
                    current_box.add_cell(k)
            boxes.append(current_box)
        return boxes

    def populate_board(self):
        for row in self.rows:
            digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for cell in row.cells:
                val = random.choice(digits)
                digits.remove(val)
                if self.check(val, row.cells) and self.check(val, self.cols[cell.col].cells) and self.check(val, self.boxes[cell.box].cells):
                    cell.val = val
                else:
                    cell.val = 'changed'

    @staticmethod
    def check(val, obj):
        for cell in obj:
            if cell.val == val:
                return False
            else:
                return True


def test():
    board = Board()
    board.populate_board()
    print(board.board)


if __name__ == '__main__':
    test()
