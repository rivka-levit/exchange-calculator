"""
Choice currencies box.
"""

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QComboBox


class ChoiceBox(QComboBox):
    """Choice currency box"""

    def __init__(self, currencies, fonts=None):
        super().__init__()
        self.currencies = currencies
        self.fonts = fonts
        self.set_ui()

    def set_ui(self):
        self.setMinimumWidth(80)
        self.setFixedHeight(35)
        self.setFont(QFont(self.fonts.gentium_bold, 12, weight=600))
        self.addItems(self.currencies)
        self.setStyleSheet(
            'background-color: #d7d5d4;'
            'border: 2px solid #545f72;'
            'border-radius: 5px;'
            'padding: 4px;'
            'color: #505050;'
        )
