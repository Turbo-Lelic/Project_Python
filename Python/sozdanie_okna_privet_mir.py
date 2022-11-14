import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

w = QtWidgets.QWidget()
w.resize(300, 30)
w.move(800, 300)
w.setWindowTitle("Hello World")

label = QtWidgets.QLabel("<center>Hello World<center>")
btnQuit = QtWidgets.QPushButton("&Stop")
vBox = QtWidgets.QVBoxLayout()

vBox.addWidget(label)
vBox.addWidget(btnQuit)

w.setLayout(vBox)
btnQuit.clicked.connect(app.quit)
w.show()

sys.exit(app.exec_())