"""
Custom fonts for the application.
"""

from PyQt6.QtGui import QFontDatabase


class CustomFonts:
    """Custom fonts for the application."""

    def __init__(self):
        self.gentium_bold = self.add_font(
            '_internal/assets/gentium-book-basic.bold.ttf'
        )

    @staticmethod
    def add_font(filename):
        """Add font to font database and return font family name."""

        font_id = QFontDatabase.addApplicationFont(filename)
        families = QFontDatabase.applicationFontFamilies(font_id)
        return families[0]
