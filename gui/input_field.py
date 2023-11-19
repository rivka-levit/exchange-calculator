"""
Input field for amount to convert.
"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLineEdit


class AmountInput(QLineEdit):
    """Amount input field."""

    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        self.setMinimumWidth(200)
        self.setFixedHeight(40)
        self.setFont(QFont('Helvetica', 12, weight=600))
        self.setPlaceholderText('Enter amount...')
        self.setStyleSheet(
            f'qproperty-alignment: {Qt.AlignmentFlag.AlignCenter};'
            f'color: #505050;'
            f'background-color: #ffffff;'
            f'border: 2px solid #ff9d9c;'
            f'border-radius: 5px;'
            f'padding: 5px;'
        )

