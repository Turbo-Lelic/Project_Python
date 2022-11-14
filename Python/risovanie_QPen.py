
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(400, 400, 380, 370)
        self.setWindowTitle('Color')
        self.show()


    def paintEvent(self,e):

        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()


    def drawLines(self, qp):

        pen1 = QPen(Qt.red, 2, Qt.SolidLine)
        pen2 = QPen(Qt.blue, 2, Qt.SolidLine)

        qp.setPen(pen1)
        qp.drawLine(20, 40, 350, 40)

        pen1.setStyle(Qt.DashLine)
        qp.setPen(pen1)
        qp.drawLine(20, 80, 350, 80)

        pen1.setStyle(Qt.DashDotLine)
        qp.setPen(pen1)
        qp.drawLine(20, 120, 350, 120)

        pen1.setStyle(Qt.DotLine)
        qp.setPen(pen1)
        qp.drawLine(20, 160, 350, 160)

        pen1.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen1)
        qp.drawLine(20, 200, 350, 200)

        pen2.setStyle(Qt.CustomDashLine)
        pen2.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen2)
        qp.drawLine(20, 240, 350, 24)

        pen2.setStyle(Qt.CustomDashLine)
        pen2.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen2)
        qp.drawLine(20, 24, 350, 240)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())