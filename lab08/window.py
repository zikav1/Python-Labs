from board import TicTacToeBoard
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
import sys

class TicTacToeWindow(QtWidgets.QWidget):
    def __init__(self, board):
        super().__init__()
        self.board = board
        self.init_state()
        self.init_components()
        self.update()

    def init_state(self):
        self.current_marker = 'X'
        self.is_running = True

    def init_components(self):
        self.setWindowTitle('Tre-i-rad')

        # Create grid layout to place (graphical) components
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        # Create all buttons and add them to the grid layout
        for row in range(3):
            for col in range(3):
                button = QtWidgets.QPushButton(flat=True)
                button.setStyleSheet('border: 3px solid #C0C0C0; font-size: 40pt; background-color: #fff;')
                button.setFixedSize(100, 100)
                # Use a lambda expression to call self.clicked when a button is 
                # clicked with the correct argument values (row and col):
                button.clicked.connect(lambda _,r=row,c=col: self.clicked(r, c))
                self.grid.addWidget(button, row, col)

        # Create label and restart button. Add them to the grid layout
        self.label = QtWidgets.QLabel()
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet('font-size: 20pt;')
        self.restart_button = QtWidgets.QPushButton('Starta om')
        self.restart_button.clicked.connect(self.restart)
        self.grid.addWidget(self.label, 3, 0, 1, 2)
        self.grid.addWidget(self.restart_button, 3, 2, 1, 1)

        self.show()

    def clicked(self, row, col):
        if self.is_running and self.board.is_empty(row, col):
            self.board.place(self.current_marker, row, col)
            self.current_marker = 'O' if self.current_marker == 'X' else 'X'
            self.update()

    def update(self):
        # Update all buttons according to the state of the board
        for row in range(3):
            for col in range(3):
                button = self.grid.itemAtPosition(row, col).widget()
                marker = self.board.get(row, col)
                text = marker if marker != '-' else ''
                button.setText(text)

        # Update label and if game is running
        if self.board.is_winner('X'):
            self.label.setText('X vann!')
            self.is_running = False
        elif self.board.is_winner('O'):
            self.label.setText('O vann!')
            self.is_running = False
        elif self.board.is_full():
            self.label.setText('Oavgjort!')
            self.is_running = False
        else:
            self.label.setText(self.current_marker + ':s tur')

    def restart(self):
        self.init_state()
        self.board.restart()
        self.update()


if __name__ == '__main__':
    board = TicTacToeBoard()
    app = QtWidgets.QApplication(sys.argv)
    window = TicTacToeWindow(board)
    sys.exit(app.exec())