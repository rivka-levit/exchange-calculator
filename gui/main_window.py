"""
Main window of the app.
"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel
)

from calculs.calculations import CurrencyConverter


class MainWindow(QMainWindow):
    """Main window of the app."""

    def __init__(self):
        super().__init__()
        self.converter = CurrencyConverter()
        self.set_ui()

    def set_ui(self):
        """Set user interface."""

        self.setWindowIcon(QIcon('assets/cur3.ico'))
        self.setWindowTitle('Exchange Converter')
        self.setStyleSheet('background-color: #e9f4bc;')
        self.setGeometry(0, 0, 240, 260)
        self.center_window()

        central_widget = QWidget()
        central_widget.setLayout(self.set_main_layout())
        central_widget.setContentsMargins(20, 0, 20, 20)
        self.setCentralWidget(central_widget)

    def set_main_layout(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        return main_layout

    def center_window(self):
        """Open main window always in the center."""

        qt_rectangle = self.frameGeometry()
        center_point = self.screen().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
