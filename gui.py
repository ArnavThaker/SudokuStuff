import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])
window = QWidget()
window.setWindowTitle("Sudoku")
window.setGeometry(100, 100, 280, 80) # x start, y start, width, height
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window) # This is in HTML, which I have 0 clue how to use
helloMsg.move(60, 15)