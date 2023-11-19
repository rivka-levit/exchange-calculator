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
        self.setFixedHeight(30)
        self.setFont(QFont('Helvetica', 16, weight=900))
        self.setStyleSheet(
            """
                QPushButton {
                    background-color: #ff9d9c;
                    color: #ffffff;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #fba8a7;
                }
                QPushButton:pressed {
                    background-color: #e98584;
                }
            """
        )
        effect = QGraphicsDropShadowEffect(offset=QPointF(QPoint(1, 2)),
                                           blurRadius=5,
                                           color=QColor('#505050'))
        self.setGraphicsEffect(effect)
