import sys
import random

from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.paint.clicked.connect(self.painting)
        self.do_paint = False

    def painting(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            r = random.randint(20, 50)
            x = random.randint(50, 600)
            y = random.randint(50, 600)
            qp.drawEllipse(QPoint(x, y), r, r)
            qp.end()
            self.do_paint = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
