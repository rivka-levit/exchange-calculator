"""
Scroll box for the list of currencies.
"""

from PyQt6.QtWidgets import QScrollArea
from PyQt6.QtCore import Qt


class ScrollCurrencies(QScrollArea):
    """Scroll box for currencies."""

    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        """Set user interface."""

        self.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.setWidgetResizable(True)
        self.setStyleSheet(
            """
                QScrollArea {
                    border-radius: 5px;
                    padding: 10px 10px 10px 10px;
                    color: #505050;
                }
            """
        )
