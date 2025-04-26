# Импорт необходимых модулей из PyQt5
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QLineEdit, QGridLayout, QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class Calculator(QMainWindow):
    def __init__(self):
        """
        Инициализация главного окна калькулятора.
        Наследуется от QMainWindow для создания стандартного окна приложения.
        """
        super().__init__()  # Вызов конструктора родительского класса

        # Настройка основного окна
        self.setWindowTitle("Калькулятор")  # Установка заголовка окна
        self.setWindowIcon(QIcon('calculator.png'))  # Установка иконки
        self.setFixedSize(300, 400)  # Фиксированный размер окна (ширина, высота)

        # Создание центрального виджета и основного layout
        main_widget = QWidget()  # Главный виджет-контейнер
        self.setCentralWidget(main_widget)  # Установка как центрального виджета
        layout = QVBoxLayout()  # Вертикальное расположение элементов

        # Создание и настройка дисплея (поле ввода)
        self.display = QLineEdit()  # Поле для вывода вычислений
        self.display.setAlignment(Qt.AlignRight)  # Выравнивание текста по правому краю
        self.display.setReadOnly(True)  # Запрет ручного ввода
        # Стилизация дисплея
        self.display.setStyleSheet("""
            font-size: 24px;  # Размер шрифта
            padding: 10px;    # Внутренние отступы
            border: 2px solid #ccc;  # Граница
        """)
        layout.addWidget(self.display)  # Добавление дисплея в layout

        # Создание сетки для кнопок
        buttons_layout = QGridLayout()
        # Список кнопок в порядке их расположения
        buttons = [
            '7', '8', '9', '/',  # Первый ряд
            '4', '5', '6', '*',  # Второй ряд
            '1', '2', '3', '-',  # Третий ряд
            'C', '0', '=', '+'  # Четвертый ряд
        ]

        # Создание и размещение кнопок
        for i, text in enumerate(buttons):
            button = QPushButton(text)  # Создание кнопки с текстом
            button.setStyleSheet("""
                font-size: 18px;  # Размер шрифта
                padding: 10px;    # Внутренние отступы
                border: 1px solid #888;  # Граница
            """)
            # Особый стиль для кнопки "="
            if text == '=':
                button.setStyleSheet("""
                    background-color: #4CAF50;  # Зеленый фон
                    color: white;              # Белый текст
                    font-size: 18px;
                """)
            button.clicked.connect(self.on_click)  # Подключение обработчика
            # Размещение кнопки в сетке (ряд, колонка)
            buttons_layout.addWidget(button, i // 4, i % 4)

        layout.addLayout(buttons_layout)  # Добавление сетки кнопок в основной layout
        main_widget.setLayout(layout)  # Установка layout для главного виджета

    def on_click(self):
        """Обработчик нажатия кнопок калькулятора"""
        sender = self.sender()  # Получаем объект кнопки, которая вызвала событие
        text = sender.text()  # Получаем текст с кнопки

        if text == 'C':  # Очистка дисплея
            self.display.clear()
        elif text == '=':  # Вычисление результата
            try:
                result = eval(self.display.text())  # Вычисляем выражение
                self.display.setText(str(result))  # Выводим результат
            except:
                self.display.setText("Ошибка")  # В случае ошибки
        else:  # Добавление символа к текущему тексту
            self.display.setText(self.display.text() + text)


if __name__ == '__main__':
    app = QApplication([])  # Создание объекта приложения
    calc = Calculator()  # Создание экземпляра калькулятора
    calc.show()  # Показ окна
    app.exec_()  # Запуск основного цикла приложения