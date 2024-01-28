import sys
import os
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
from memory_board import MemoryBoard
from memory_game import MemoryGame

class MemoryWindow(QtWidgets.QWidget):
    def __init__(self, game):
        super().__init__()
        self.game = game

        self.window_size = 800
        self.sleeping_time = 700    # In milliseconds
        # Number of rows/cols. Should be same as the board's size.
        # Could be retrieved from game, but instead use constant to make
        # the code a bit more robost against errors in MemoryGame.
        self.size = 4
                                     
        self.sleeping = False       # Events are ignored during sleeping
        self.pixmaps = dict()       # Used for caching images

        self.init_components()

    def init_components(self):
        self.setWindowTitle('Memory-spel')

        # Use a grid layout for placing components
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        # Create all cards as buttons
        for row in range(self.size):
            for col in range(self.size):
                image_filename = self.game.current_card_side_up(row, col)
                pixmap = self._get_pixmap(image_filename)
                button = QtWidgets.QPushButton(flat=pixmap is not None)
                if pixmap:
                    button.setIcon(QtGui.QIcon(pixmap))
                    button.setIconSize(pixmap.rect().size())
                    button.setFixedSize(pixmap.rect().size())
                button.clicked.connect(lambda _,r=row,c=col: self.card_clicked(r, c))
                self.grid.addWidget(button, row, col)

        # Create label and restart button
        self.label = QtWidgets.QLabel('')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.restart_button = QtWidgets.QPushButton('Starta om')
        self.restart_button.clicked.connect(self.restart_clicked)
        self.grid.addWidget(self.label, self.size, 0, 1, self.size//2)
        self.grid.addWidget(self.restart_button, self.size, 2, 1, self.size//2)

        # Show GUI
        self.show()

    def card_clicked(self, row, col):
        # Ignore click events while sleeping
        if not self.sleeping:
            should_sleep = self.game.card_clicked(row, col)
            self.update_all_images()
            if self.game.has_won():
                n = self.game.num_tries()
                self.label.setText(f'Grattis! Du klarade det på {n} försök!')
            if should_sleep:
                self.sleep()

    def restart_clicked(self):
        # Ignore click events while sleeping
        if not self.sleeping:
            self.game.start_game()
            self.label.setText('')
            self.update_all_images()

    def update_all_images(self):
        # Update all button images according to the state of the board
        # Could be implemented incrementally by only updating the changed cards...
        for r in range(self.size):
            for c in range(self.size):
                self.update_image(r, c)

    def update_image(self, row, col):
        # Update a button image according to the state of the board
        image_filename = self.game.current_card_side_up(row, col)
        pixmap = self._get_pixmap(image_filename)
        button = self.grid.itemAtPosition(row, col).widget()
        button.setIcon(QtGui.QIcon(pixmap))

    def sleep(self):
        # Sleep for a certain time and then call the sleep_done method
        self.sleeping = True
        self.restart_button.setDisabled(True)
        QtCore.QTimer.singleShot(self.sleeping_time, self.sleep_done)

    def sleep_done(self):
        # This method is called when sleeping is done
        self.game.sleep_done()
        self.update_all_images()
        self.restart_button.setDisabled(False)
        self.sleeping = False

    def _get_pixmap(self, filename):
        # Make code somewhat robust
        if filename is None:
            return None

        # Only load each image once from disk (cache images for subsequent accesses).
        # Check if already loaded
        if filename in self.pixmaps:
            # Retrieve image (pixmap) from dictionary
            return self.pixmaps[filename]
        else:
            # Read image from file and put the loaded image into the dictionary
            # Make filename relative to the script's directory
            full_path = os.path.join(os.path.dirname(__file__), filename)
            image_size = self.window_size // self.size
            pixmap = QtGui.QPixmap(full_path)
            if pixmap.isNull():
                # File doesn't exist or can't be loaded
                print(f"ERROR! Can't load image: {full_path}")
                pixmap = None
            else:
                pixmap = pixmap.scaled(image_size, image_size)
            self.pixmaps[filename] = pixmap
            return pixmap


if __name__ == '__main__':
    # Create memory board and game logic
    fronts = ['friends.jpg', 'mrs_rabbit.jpg', 'can.jpg', 
             'mrs_tittlemouse.jpg', 'flopsy_mopsy_cottontail.jpg', 
             'mr_mcgregor.jpg', 'radishes.jpg', 'mother_ladybird.jpg']
    fronts = [f'images/{f}' for f in fronts]
    back = 'images/back.jpg'
    board = MemoryBoard(4, fronts, back)
    game = MemoryGame(board)

    # Create memory window
    app = QtWidgets.QApplication(sys.argv)
    window = MemoryWindow(game)
    # Start listening on GUI events (mouse clicks etc)
    sys.exit(app.exec())
