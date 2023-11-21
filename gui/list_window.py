"""
Window with list of all available currencies.
"""

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout


class ListWindow(QWidget):
    """List of all available currencies."""

    def __init__(self, currencies=None):
        super().__init__()
        self.currencies = currencies
        self.list_label = QLabel('')
        self.set_ui()

    def set_ui(self):
        self.setWindowIcon(QIcon('assets/icon.ico'))
        self.setWindowTitle('All Currencies')
        self.setGeometry(0, 0, 400, 500)
        self.setStyleSheet('background-color: #f2f2f2;')

        layout = QVBoxLayout()
        output = ''
        for ticker, descr in self.currencies.items():
            output += f'{ticker} - {descr}\n'
        self.list_label.setText(output)
        layout.addWidget(self.list_label)

        self.setLayout(layout)

