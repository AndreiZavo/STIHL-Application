from PySide2.QtCore import QTimeLine
from PySide2.QtGui import QPixmap, QPainter
from PySide2.QtWidgets import QWidget, QStackedWidget


class FaderWidget(QWidget):

    def __init__(self, old_widget, new_widget):
        QWidget.__init__(self, new_widget)

        self.pixmap_opacity = 1.0
        self.old_pixmap = QPixmap(new_widget.size())
        old_widget.render(self.old_pixmap)

        self.timeline = QTimeLine()
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(230)
        self.timeline.start()

        self.resize(new_widget.size())
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.old_pixmap)
        painter.end()

    def animate(self, value):
        self.pixmap_opacity = 1.0 - value
        self.repaint()


class StackedWidget(QStackedWidget):

    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent)

    def setCurrentIndex(self, index):
        self.fader_widget = FaderWidget(self.currentWidget(), self.widget(index))
        QStackedWidget.setCurrentIndex(self, index)

    def setPage1(self):
        self.setCurrentIndex(0)

    def setPage2(self):
        self.setCurrentIndex(1)

    def setPage3(self):
        self.setCurrentIndex(2)

    def setPage4(self):
        self.setCurrentIndex(3)

    def setPage5(self):
        self.setCurrentIndex(4)

    def setPage6(self):
        self.setCurrentIndex(5)
