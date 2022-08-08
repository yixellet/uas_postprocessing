from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class ErrorMessage(QDialog):
    def __init__(self):
        super(ErrorMessage,  self).__init__()
        loadUi("error_message.ui", self)