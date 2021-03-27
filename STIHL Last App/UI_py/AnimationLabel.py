import sys

from PyQt5.QtCore import QVariant, pyqtSlot

from PySide2.QtCore import QEventLoop, QTimer, QEasingCurve, QVariantAnimation
from PySide2.QtGui import QColor, QPalette
from PySide2.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QGraphicsOpacityEffect


class AnimationLabel(QLabel):
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.animation = QVariantAnimation()
        self.animation.valueChanged.connect(self.changeColor)

    @pyqtSlot(QVariant)
    def changeColor(self, color):
        palette = self.palette()
        palette.setColor(QPalette.WindowText, color)
        self.setPalette(palette)

    def startFadeIn(self):
        self.animation.stop()
        self.animation.setStartValue(QColor("#333"))
        self.animation.setEndValue(QColor("white"))
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.InBack)
        self.animation.start()

    def startFadeOut(self):
        self.animation.stop()
        self.animation.setStartValue(QColor("white"))
        self.animation.setEndValue(QColor("#333"))
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.OutBack)
        self.animation.start()

    def startAnimation(self):
        self.startFadeIn()
        loop = QEventLoop()
        self.animation.finished.connect(loop.quit)
        loop.exec_()
        QTimer.singleShot(1000, self.startFadeOut)


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #333;")
        lay = QVBoxLayout(self)
        self.greeting_text = AnimationLabel("greeting_text")
        self.greeting_text.setStyleSheet("font : 45px; font : bold; font-family : HelveticaNeue-UltraLight")
        lay.addWidget(self.greeting_text)
        btnFadeIn = QPushButton("fade in")
        btnFadeOut = QPushButton("fade out")
        btnAnimation = QPushButton("animation")
        lay.addWidget(btnFadeIn)
        lay.addWidget(btnFadeOut)
        lay.addWidget(btnAnimation)
        btnFadeIn.clicked.connect(self.greeting_text.startFadeIn)
        btnFadeOut.clicked.connect(self.greeting_text.startFadeOut)
        btnAnimation.clicked.connect(self.greeting_text.startAnimation)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())