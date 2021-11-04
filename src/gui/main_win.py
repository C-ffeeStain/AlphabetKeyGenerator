from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('ui/main.ui', self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()