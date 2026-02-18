import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget

from fdia_generation_page import FDIAFrontend
from testing_page_updated import TestingPage


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FDIA Research Tool")
        self.setMinimumSize(700, 800)

        layout = QVBoxLayout()
        self.stack = QStackedWidget()

        # Pages
        self.fdia_page = FDIAFrontend()
        self.testing_page = TestingPage()

        # Add pages to stack
        self.stack.addWidget(self.fdia_page)    # index 0
        self.stack.addWidget(self.testing_page) # index 1

        layout.addWidget(self.stack)
        self.setLayout(layout)

        # Connect navigation signals
        self.fdia_page.test_requested.connect(self.show_testing_page)
        self.testing_page.back_requested.connect(self.show_fdia_page)

    def show_testing_page(self):
        self.stack.setCurrentIndex(1)

    def show_fdia_page(self):
        self.stack.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
