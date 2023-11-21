"""
Buttons for the main window.
"""

from PyQt6.QtCore import QPoint, QPointF
from PyQt6.QtGui import QFont, QColor, QIcon
from PyQt6.QtWidgets import QPushButton, QGraphicsDropShadowEffect

from gui.list_window import ListWindow


class ConvertButton(QPushButton):
    """The Convert button."""

    def __init__(self, fonts=None):
        super().__init__()
        self.fonts = fonts
        self.set_ui()

    def set_ui(self):
        """Set user interface."""

        self.setText('Convert')
        self.setMinimumWidth(108)
        self.setFixedHeight(35)
        self.setFont(QFont(self.fonts.gentium_bold, 18, weight=900))
        self.setStyleSheet(
            """
                QPushButton {
                    background-color: #545f71;
                    color: #f2f2f2;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #855751;
                }
                QPushButton:pressed {
                    background-color: #74433e;
                }
            """
        )
        effect = QGraphicsDropShadowEffect(offset=QPointF(QPoint(1, 2)),
                                           blurRadius=5,
                                           color=QColor('#545f72'))
        self.setGraphicsEffect(effect)


class ListButton(QPushButton):
    """Button for the list of currencies."""

    def __init__(self, currencies=None, fonts=None):
        super().__init__()
        self.currencies = currencies
        self.fonts = fonts
        self.set_ui()
        self.list_window = None
        self.clicked.connect(self.slot)

    def set_ui(self):
        """Set user interface."""
        self.setIcon(QIcon('assets/list.png'))
        self.setMinimumWidth(35)
        self.setFixedHeight(35)
        self.setStyleSheet(
            """
                QPushButton {
                    background-color: #d7d5d4;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #c8c3c0;
                }
                QPushButton:pressed {
                    background-color: #c0b7b4;
                }
            """
        )

        effect = QGraphicsDropShadowEffect(offset=QPointF(QPoint(1, 2)),
                                           blurRadius=5,
                                           color=QColor('#545f72'))
        self.setGraphicsEffect(effect)

    def slot(self):
        if self.list_window is None:
            self.list_window = ListWindow(currencies=self.currencies,
                                          fonts=self.fonts)
        self.list_window.show()

