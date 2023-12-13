import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from data_circle.ui.MainWindow import Ui_MainWindow


class QMyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMyMainWindow()
    main_window.show()
    sys.exit(app.exec())
