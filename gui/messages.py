"""
Message windows.
"""

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMessageBox


class InvalidInputMessage(QMessageBox):
    """Invalid input value message."""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Invalid input!")
        self.setContentsMargins(10, 10, 20, 10)
        self.setStyleSheet('background-color: #f2f2f2;')
        self.setFont(QFont('Helvetica', 12))
        self.setText("You must provide a number!")
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.setIcon(QMessageBox.Icon.Warning)
