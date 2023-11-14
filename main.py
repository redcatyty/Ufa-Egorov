from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from random import randint



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.draw_circle)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)


    def draw_circle(self, painter):
        rnd = randint(1, 200)
        print(rnd)
        painter.setBrush(QColor(255, 255, 0))
        painter.drawEllipse(390, 270, rnd, rnd)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())