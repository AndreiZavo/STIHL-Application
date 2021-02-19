import sys

from PySide2 import QtCore, QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QApplication

from UI_py.ui_ErrorWindow import Ui_errorWindow


class ErrorWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_errorWindow()

        self.ui.setupUi(self)

        # Hide the preformed toolbar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set window icon
        self.setWindowIcon(QtGui.QIcon(":/Icons/Icons/Stihl_Server_IconToolBar.svg"))

        # Set window title
        self.setWindowTitle("Warning Message")

        # Create connection for buttons
        self.ui.closeButton.clicked.connect(lambda: self.close())
        self.ui.OKButton.clicked.connect(lambda: self.close())

        # Set action for left click mouse for moving the window
        def moveWindow(e):
            if self.isMaximized() is False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        # Set on what elements the moveWindow applies
        self.ui.topbar_menu.mouseMoveEvent = moveWindow

        self.show()

    """ Function sets events to the window """
    def mousePressEvent(self, event):
        # get current position of the mouse
        self.clickPosition = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ErrorWindow()
    sys.exit(app.exec_())
