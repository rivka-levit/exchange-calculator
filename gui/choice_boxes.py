"""
Choice currencies box.
"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QComboBox


class ChoiceBox(QComboBox):
    """Choice currency box"""

    def __init__(self, currencies):
        super().__init__()
        self.currencies = currencies
        self.set_ui()

    def set_ui(self):
        self.setMinimumWidth(100)
        self.setMinimumHeight(20)
        self.setFont(QFont('Helvetica', 12, weight=600))
        self.addItems(self.currencies)
        self.setStyleSheet(
            'background-color: #ffffff;'
            'border: 2px solid #ff9d9c;'
            'border-radius: 5px;'
            'padding: 5px;'
            'color: #505050;'
        )
