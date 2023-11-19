"""
Buttons for the main window.
"""

from PyQt6.QtCore import QPoint, QPointF
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import QPushButton, QGraphicsDropShadowEffect


class ConvertButton(QPushButton):
    """The Convert button."""

    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        self.setText('Convert')
        self.setMinimumWidth(120)
        self.setFixedHeight(35)
        self.setFont(QFont('Helvetica', 16, weight=900))
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
