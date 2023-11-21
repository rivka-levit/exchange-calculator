"""
Message windows.
"""

from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QMessageBox


class BaseMessage(QMessageBox):
    """Base message class."""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setContentsMargins(10, 10, 20, 10)
        self.setStyleSheet('background-color: #f2f2f2;')
        self.setFont(QFont('Helvetica', 12))
        self.setStandardButtons(QMessageBox.StandardButton.Ok)


class InvalidInputMessage(BaseMessage):
    """Invalid input value message."""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Invalid input!")
        self.setText("You must provide a number!")
        self.setIcon(QMessageBox.Icon.Warning)


class ConnectionErrorMessage(BaseMessage):
    """Connection error message."""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowIcon(QIcon('assets/icon.ico'))
        self.setWindowTitle("Connection Error!")
        self.setText("Oops! Connection failed!\nPlease, check your internet "
                     "connection and try again.")
        self.setIcon(QMessageBox.Icon.Critical)
