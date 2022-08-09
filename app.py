import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow

app = QApplication(sys.argv)
mainWindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.show()
sys.exit(app.exec_())
