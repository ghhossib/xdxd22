# Задание 3: Приложение с несколькими экранами (QStackedWidget)

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QStackedWidget, QWidget,
    QVBoxLayout, QPushButton, QLabel
)

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()  # Инициализация родительского класса QMainWindow
        self.setWindowTitle("Приложение с переключением страниц")  # Заголовок окна
        self.setGeometry(100, 100, 400, 300)  # Позиция и размер окна (x, y, width, height)

        # Создание stacked widget (контейнера для страниц)
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)  # Установка как центрального виджета

        # Создание страниц
        self.create_page1()
        self.create_page2()

        # Добавление страниц в stacked widget
        self.stacked_widget.addWidget(self.page1)  # Индекс 0
        self.stacked_widget.addWidget(self.page2)  # Индекс 1

    def create_page1(self):
        """Создание первой страницы"""
        self.page1 = QWidget()
        layout = QVBoxLayout()  # Вертикальное расположение элементов

        label = QLabel("Это первая страница")  # Текстовая метка
        layout.addWidget(label)  # Добавление метки в layout

        button = QPushButton("Перейти на страницу 2")  # Кнопка переключения
        # При нажатии переключаемся на страницу с индексом 1 (вторая страница)
        button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        layout.addWidget(button)  # Добавление кнопки в layout

        self.page1.setLayout(layout)  # Установка layout для страницы

    def create_page2(self):
        """Создание второй страницы"""
        self.page2 = QWidget()
        layout = QVBoxLayout()  # Вертикальное расположение элементов

        label = QLabel("Это вторая страница")  # Текстовая метка
        layout.addWidget(label)  # Добавление метки в layout

        button = QPushButton("Вернуться на страницу 1")  # Кнопка переключения
        # При нажатии переключаемся на страницу с индексом 0 (первая страница)
        button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout.addWidget(button)  # Добавление кнопки в layout

        self.page2.setLayout(layout)  # Установка layout для страницы

if __name__ == '__main__':
    app = QApplication([])  # Создание QApplication
    window = MainApp()  # Создание экземпляра нашего приложения
    window.show()  # Показываем окно
    app.exec_()  # Запуск основного цикла приложения