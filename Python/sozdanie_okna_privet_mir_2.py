import sys
from PyQt5 import QtWidgets

class myBtn:
    def __init__(self):
        pass
    def btnFunc(self):
        print("Hello")

app = QtWidgets.QApplication(sys.argv)

w = QtWidgets.QWidget()
w.resize(300, 70)
w.move(800, 300)
w.setWindowTitle("Hello")

label = QtWidgets.QLabel("<center>Hello<center>")
btnQuit = QtWidgets.QPushButton("&Stop")
btn2 = QtWidgets.QPushButton("&Hello")
vBox = QtWidgets.QVBoxLayout()

vBox.addWidget(label)
vBox.addWidget(btnQuit)
vBox.addWidget(btn2)

w.setLayout(vBox)
btnQuit.clicked.connect(app.quit)

btn = myBtn()
btn2.clicked.connect(btn.btnFunc)

w.show()

sys.exit(app.exec_())