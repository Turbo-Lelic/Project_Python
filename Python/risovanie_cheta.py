import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor

class Example(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Color')
        self.show()


    def paintEvent(self, qp):

        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()


    def drawRectangles(self, e):

        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        e.setPen(col)

        e.setBrush(QColor(200, 0, 0))
        e.drawRect(10, 15, 90, 60)

        e.setBrush(QColor(255, 80, 0, 160))
        e.drawRect(130, 15, 90, 60)

        e.setBrush(QColor(25, 0, 90, 200))
        e.drawRect(250, 15, 90, 60)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())