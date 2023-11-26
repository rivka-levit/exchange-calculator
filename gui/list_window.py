"""
Window with list of all available currencies.
"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

from gui.scroll_currencies import ScrollCurrencies


class ListWindow(QWidget):
    """List of all available currencies."""

    def __init__(self, currencies=None, fonts=None):
        super().__init__()
        self.fonts = fonts
        self.currencies = currencies
        self.list_label = QLabel('')
        self.set_ui()

    def set_ui(self):
        self.setWindowIcon(QIcon('_internal/assets/icon.ico'))
        self.setWindowTitle('Currencies')
        self.setGeometry(0, 0, 400, 500)
        self.setStyleSheet('background-color: #f2f2f2;')

        layout = QVBoxLayout()
        scroll_box = ScrollCurrencies()
        scroll_box.setStyleSheet(
            """
                QScrollArea {
                    border: 1px solid #4e5f73;
                    border-radius: 5px;
                    padding: 3px 0 0 10px;
                }
            """
        )

        title = QLabel('Available Currencies')
        title.setFont(QFont(self.fonts.gentium_bold, 16, weight=900))
        title.setStyleSheet('color: #8c4b45;')
        title.setContentsMargins(0, 3, 0, 5)
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.set_currencies_output()
        scroll_box.setWidget(self.list_label)
        layout.addWidget(scroll_box)

        self.setLayout(layout)

    def set_currencies_output(self):
        """Set the list of currencies to the label output."""

        output = ''
        for ticker, descr in self.currencies.items():
            output += f'{ticker} - {descr}\n'
        self.list_label.setText(output)
        self.list_label.setFont(QFont('Helvetica', 12, weight=400))
