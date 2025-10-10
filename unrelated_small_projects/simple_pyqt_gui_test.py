# simple pyqt5 test window with hello world and a text input with a button to change the text box above it
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple PyQt5 GUI')

        # Create widgets
        self.label = QLabel('Hello World!', self)
        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText('Enter new text here...')
        self.button = QPushButton('Change Text', self)

        # Create layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.text_input)
        vbox.addWidget(self.button)

        self.setLayout(vbox)

        # Connect button to a function
        self.button.clicked.connect(self.change_label_text)

    def change_label_text(self):
        new_text = self.text_input.text()
        if new_text: # Only change if there's text in the input field
            self.label.setText(new_text)
            self.text_input.clear() # Clear the input field after changing

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
    