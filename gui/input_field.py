"""
Input field for amount to convert.
"""

from PyQt6.QtCore import Qt, QPoint, QPointF
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import QLineEdit, QGraphicsDropShadowEffect


class AmountInput(QLineEdit):
    """Amount input field."""

    def __init__(self, slot=None):
        super().__init__()
        self.slot = slot
        self.set_ui()

    def set_ui(self):
        self.setMinimumWidth(180)
        self.setFixedHeight(40)
        self.setFont(QFont('Helvetica', 12, weight=600))
        self.setPlaceholderText('Enter amount...')
        self.setStyleSheet(
            f'qproperty-alignment: {Qt.AlignmentFlag.AlignCenter};'
            f'color: #505050;'
            f'background-color: #f2f2f2;'
            f'border-radius: 5px;'
            f'padding: 5px;'
        )
        effect = QGraphicsDropShadowEffect(offset=QPointF(QPoint(1, 1)),
                                           blurRadius=10,
                                           color=QColor('#545f72'))
        self.setGraphicsEffect(effect)

    def keyPressEvent(self, event):
        """Handle Enter key pressed in the input field."""

        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.slot()
        else:
            super().keyPressEvent(event)

