"""
Main window of the app.
"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QCloseEvent
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)
from requests.exceptions import ConnectionError

from calculs.calculations import CurrencyConverter
from calculs.extractors import RateScrapeExtractor
from gui.choice_boxes import ChoiceBox
from gui.input_field import AmountInput
from gui.output_label import ConvertedAmount
from gui.buttons import ConvertButton, ListButton, ReverseButton
from gui.fonts import CustomFonts
from gui.messages import InvalidInputMessage, ConnectionErrorMessage
from gui.list_window import ListWindow


class MainWindow(QMainWindow):
    """Main window of the app."""

    def __init__(self):
        super().__init__()
        try:
            self.currencies = RateScrapeExtractor().get_currencies()
        except ConnectionError:
            msg = ('Internet connection failed!\nPlease check it '
                   'and try again.')
            err_message = ConnectionErrorMessage(msg, parent=self)
            err_message.exec()
        except Exception as e:
            err_message = ConnectionErrorMessage(str(e), parent=self)
            err_message.exec()
        self.converter = CurrencyConverter()
        self.fonts = CustomFonts()
        self.from_box = ChoiceBox(self.currencies.keys(), fonts=self.fonts)
        self.to_box = ChoiceBox(self.currencies.keys(), fonts=self.fonts)
        self.amount = AmountInput(slot=self.slot)
        self.converted_amount = ConvertedAmount()
        self.list_window = None
        self.set_ui()

    def set_ui(self):
        """Set user interface."""

        self.setWindowIcon(QIcon('_internal/assets/icon.ico'))
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
        choice_layout.setSpacing(15)

        self.from_box.setCurrentText('USD')
        choice_layout.addWidget(self.from_box, stretch=2)

        reverse_btn = ReverseButton()
        choice_layout.addWidget(reverse_btn, stretch=1)
        reverse_btn.clicked.connect(self.reverse_currencies)

        self.to_box.setCurrentText('ILS')
        choice_layout.addWidget(self.to_box, stretch=2)

        choice_layout.setContentsMargins(0, 0, 0, 10)

        return choice_layout

    def set_bottom_layout(self):
        """Set layout for buttons."""

        bottom_layout = QHBoxLayout()

        list_btn = ListButton(currencies=self.currencies, fonts=self.fonts)
        bottom_layout.addWidget(list_btn, stretch=1)
        list_btn.clicked.connect(self.show_currencies)

        convert_btn = ConvertButton(fonts=self.fonts)
        bottom_layout.addWidget(convert_btn, stretch=7,
                                alignment=Qt.AlignmentFlag.AlignHCenter)
        convert_btn.clicked.connect(self.slot)

        bottom_layout.setContentsMargins(0, 10, 0, 0)

        return bottom_layout

    def slot(self):
        from_cur = self.from_box.currentText()
        to_cur = self.to_box.currentText()
        amount = self.amount.text()

        if not amount:
            self.converted_amount.setText('')

        elif self.valid_input(amount):
            try:
                self.converted_amount.setText(
                    str(self.converter.convert(from_cur, to_cur, float(amount)))
                )
            except ConnectionError:
                msg = ('Internet connection failed!\nPlease check it '
                       'and try again.')
                err_message = ConnectionErrorMessage(msg, parent=self)
                err_message.exec()
            except Exception as e:
                err_message = ConnectionErrorMessage(str(e), parent=self)
                err_message.exec()
        else:
            warning = InvalidInputMessage(parent=self)
            warning.exec()

    def reverse_currencies(self):
        """Exchange currencies names in boxes."""

        from_cur = self.from_box.currentText()
        to_cur = self.to_box.currentText()
        self.to_box.setCurrentText(from_cur)
        self.from_box.setCurrentText(to_cur)

    def show_currencies(self):
        """Show additional window with list of currencies."""

        if self.list_window is None:
            self.list_window = ListWindow(currencies=self.currencies,
                                          fonts=self.fonts)
            self.set_list_window_position()
        self.list_window.show()

    def set_list_window_position(self):
        """Set geometry for list currencies window."""

        rt = self.list_window.geometry()
        bl = self.geometry().bottomLeft()
        rt.moveBottomRight(bl)
        self.list_window.move(rt.topLeft())

    @staticmethod
    def close_all_windows():
        """On closing the main window, close all the windows."""

        all_windows = QApplication.allWindows()
        for w in all_windows:
            w.close()

    def closeEvent(self, event: QCloseEvent):
        event.accept()
        self.close_all_windows()

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
