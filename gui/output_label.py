"""
Output label for converted amount.
"""

from PyQt6.QtCore import Qt, QPoint, QPointF
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import QLabel, QGraphicsDropShadowEffect


class ConvertedAmount(QLabel):
    """Output label for converted amount."""

    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        self.setText('')
        self.setMinimumWidth(200)
        self.setFixedHeight(40)
        self.setFont(QFont('Helvetica', 12, weight=600))
        self.setStyleSheet(
            f'qproperty-alignment: {Qt.AlignmentFlag.AlignCenter};'
            f'color: #505050;'
            f'background-color: #ffffff;'
            f'border-radius: 5px;'
            f'padding: 5px;'
        )
        effect = QGraphicsDropShadowEffect(offset=QPointF(QPoint(1, 1)),
                                           blurRadius=10,
                                           color=QColor('#505050'))
        self.setGraphicsEffect(effect)
