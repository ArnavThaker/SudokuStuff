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
        self.init_board()


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
        print(board)
        for i in board:
            current_row = Row()
            for j in i:
                current_row.add_cell(j)
            rows.append(current_row)
        print(rows)
        rows = np.array(rows)
        print(rows.shape)
        rows.reshape(3, 3)
        print(rows.shape)
        print(rows)
        return rows

    def create_cols(self):
        cols = []
        board = self.init_board()
        for i in range(9):
            current_col = Column()
            for j in board[0:9, i]:
                current_col.add_cell(j)
            cols.append(current_col)
        cols = np.array(cols)
        cols = cols.reshape(1, 9)
        print(cols)
        return cols

    def create_boxes(self):
        boxes = []
        board = self.init_board()
        for i in range(3):
            current_box = Box()
            for j in board[(i//3)*3:(i//3)*3+3, i*3:i*3+3]:
                for k in j:
                    current_box.add_cell(k)
            boxes.append(current_box)
        for i in range(3, 6):
            current_box = Box()
            for j in board[(i//3)*3:(i//3)*3+3, (i-3)*3:(i-3)*3+3]:
                for k in j:
                    current_box.add_cell(k)
            boxes.append(current_box)
        for i in range(6, 9):
            current_box = Box()
            for j in board[(i//3)*3:(i//3)*3+3, (i-6)*3:(i-6)*3+3]:
                for k in j:
                    current_box.add_cell(k)
            boxes.append(current_box)
        boxes = np.array(boxes)
        boxes = boxes.reshape(1, 9)
        print(boxes)
        return boxes






def test():
    board = Board()
    board.create_rows()
    board.create_cols()
    board.create_boxes()


if __name__ == '__main__':
    test()
