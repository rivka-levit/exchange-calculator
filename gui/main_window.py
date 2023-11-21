"""
Main window of the app.
"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel
)

from calculs.calculations import CurrencyConverter
from calculs.extractors import RateExtractor
from gui.choice_boxes import ChoiceBox
from gui.input_field import AmountInput
from gui.output_label import ConvertedAmount
from gui.buttons import ConvertButton, ListButton
from gui.fonts import CustomFonts


class MainWindow(QMainWindow):
    """Main window of the app."""

    def __init__(self):
        super().__init__()
        self.converter = CurrencyConverter()
        self.currencies = RateExtractor().get_currencies()
        self.fonts = CustomFonts()
        self.from_box = ChoiceBox(self.currencies.keys(), fonts=self.fonts)
        self.to_box = ChoiceBox(self.currencies.keys(), fonts=self.fonts)
        self.amount = AmountInput(slot=self.slot)
        self.converted_amount = ConvertedAmount()
        self.set_ui()

    def set_ui(self):
        """Set user interface."""

        self.setWindowIcon(QIcon('assets/icon.ico'))
        self.setWindowTitle('Converter')
        self.setStyleSheet('background-color: #f2f2f2;')
        self.setGeometry(0, 0, 150, 260)
        self.center_window()

        central_widget = QWidget()
        central_widget.setLayout(self.set_main_layout())
        central_widget.setContentsMargins(15, 15, 15, 15)
        self.setCentralWidget(central_widget)

    def set_main_layout(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.addLayout(self.set_choice_layout())
        main_layout.addWidget(self.amount)
        main_layout.addWidget(self.converted_amount)
        main_layout.addLayout(self.set_bottom_layout())

        return main_layout

    def set_choice_layout(self):
        """Set nested layout with boxes to select currencies."""

        choice_layout = QHBoxLayout()
        choice_layout.setSpacing(10)

        self.from_box.setCurrentText('USD')
        choice_layout.addWidget(self.from_box, stretch=2)

        img_label = QLabel()
        pixmap = QPixmap('assets/arrow.png')
        img_label.setPixmap(pixmap)
        choice_layout.addWidget(img_label, stretch=1)

        self.to_box.setCurrentText('ILS')
        choice_layout.addWidget(self.to_box, stretch=2)

        choice_layout.setContentsMargins(0, 0, 0, 10)

        return choice_layout

    def set_bottom_layout(self):
        """Set layout for buttons."""

        bottom_layout = QHBoxLayout()

        list_btn = ListButton(currencies=self.currencies)
        bottom_layout.addWidget(list_btn, stretch=1)

        convert_btn = ConvertButton(fonts=self.fonts)
        bottom_layout.addWidget(convert_btn, stretch=7, alignment=Qt.AlignmentFlag.AlignHCenter)
        convert_btn.clicked.connect(self.slot)

        bottom_layout.setContentsMargins(0, 10, 0, 0)

        return bottom_layout

    def slot(self):
        from_cur = self.from_box.currentText()
        to_cur = self.to_box.currentText()
        amount = self.amount.text()

        if self.valid_input(amount):
            self.converted_amount.setText(
                str(self.converter.convert(from_cur, to_cur, float(amount)))
            )
        else:
            self.converted_amount.setText('Invalid input!')

    @staticmethod
    def valid_input(value: str) -> bool:
        """Validate amount input."""

        try:
            float(value)
            return True
        except ValueError:
            return False

    def center_window(self):
        """Open main window always in the center."""

        qt_rectangle = self.frameGeometry()
        center_point = self.screen().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
