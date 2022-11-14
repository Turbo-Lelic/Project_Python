import sys
from PyQt5.QtWidgets import (QWidget, QSlider,
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setFocusPolicy(Qt.NoFocus)
        self.sld.setGeometry(30, 40, 100, 30)
        self.sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png'))
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Dowload')
        self.show()

    def changeValue(self, value):

        if value == 0:
            print("0%")
            self.label.setPixmap(QPixmap('mute.png'))

        elif value > 0 and value <= 10:
            print("10%")
            self.label.setPixmap(QPixmap('min.png'))

        elif value > 10 and value < 20:
            print("20%")
            self.label.setPixmap(QPixmap('med.png'))

        elif value > 20 and value < 30:
            print("30%")
            self.label.setPixmap(QPixmap('med.png'))

        elif value > 30 and value < 40:
            print("40%")
            self.label.setPixmap(QPixmap('med.png'))

        elif value > 40 and value < 50:
            print("50%")
            self.label.setPixmap(QPixmap('med.png'))

        elif value > 50 and value < 60:
            print("60%")
            self.label.setPixmap(QPixmap('med.png'))

        elif value > 60 and value < 70:
            print("70%")
            self.label.setPixmap(QPixmap('med.png'))

        elif value > 70 and value < 80:
            print("80%")
            self.label.setPixmap(QPixmap('med.png'))

        elif value > 80 and value < 90:
            print("90%")
            self.label.setPixmap(QPixmap('med.png'))

        else:
            print("100%")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())