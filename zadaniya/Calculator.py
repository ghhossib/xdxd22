from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QLineEdit, QGridLayout, QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setWindowIcon(QIcon('calculator.png'))
        self.setFixedSize(300, 400)

        # Главный виджет и layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()

        # Поле ввода
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px; padding: 10px;")
        layout.addWidget(self.display)

        # Кнопки
        buttons_layout = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for i, text in enumerate(buttons):
            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px; padding: 10px;")
            button.clicked.connect(self.on_click)
            if text == '=':
                button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 18px;")
            buttons_layout.addWidget(button, i // 4, i % 4)

        layout.addLayout(buttons_layout)
        main_widget.setLayout(layout)

    def on_click(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except:
                self.display.setText("Ошибка")
        else:
            self.display.setText(self.display.text() + text)


if __name__ == '__main__':
    app = QApplication([])
    calc = Calculator()
    calc.show()
    app.exec_()