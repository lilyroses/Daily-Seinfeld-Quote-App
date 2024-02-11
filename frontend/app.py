from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Title in top bar
        self.setWindowTitle("Seinfeld Quote of the Day")

        # Button for changing to the previous quote
        previous_quote_button = QPushButton("Previous Quote")
        previous_quote_button.clicked.connect(
            self.the_previous_quote_button_was_clicked
        )
        # Button for favoriting the quote
        favorite_quote_button = QPushButton("Favorite")
        favorite_quote_button.setCheckable(True)
        favorite_quote_button.clicked.connect(self.the_favorite_button_was_clicked)
        favorite_quote_button.clicked.connect(self.the_favorite_button_was_toggled)
        # favorite_quote_button_is_checked = False

        # Set size of window
        self.setFixedSize(QSize(400, 300))

        layout = QHBoxLayout()

        buttons = [previous_quote_button, favorite_quote_button]
        for button in buttons:
            layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)

        # Set central widget of window
        self.setCentralWidget(widget)

    def the_previous_quote_button_was_clicked(self):
        print("Switching windows to the previous quote")

    def the_favorite_button_was_clicked(self):
        print("Favorited")

    def the_favorite_button_was_toggled(self, checked):
        self.favorite_button_is_checked = checked
        print(self.favorite_button_is_checked)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
