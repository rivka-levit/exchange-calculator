"""
Window with list of all available currencies.
"""

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
        self.center_window()
        self.set_ui()

    def set_ui(self):
        self.setWindowIcon(QIcon('assets/icon.ico'))
        self.setWindowTitle('Currencies')
        self.setGeometry(0, 0, 400, 500)
        self.setStyleSheet('background-color: #f2f2f2;')

        layout = QVBoxLayout()
        scroll_box = ScrollCurrencies()
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
        self.list_label.setFont(QFont(self.fonts.gentium_bold, 12))

    def center_window(self):
        """Open the window always in the center."""

        qt_rectangle = self.frameGeometry()
        center_point = self.screen().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
