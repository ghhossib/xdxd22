# Импорт необходимых модулей
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QListWidget, QLineEdit, QPushButton, QHBoxLayout)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont


class TodoApp(QMainWindow):
    def __init__(self):
        """
        Инициализация приложения списка дел.
        """
        super().__init__()

        # Настройка основного окна
        self.setWindowTitle("Список дел")
        self.setWindowIcon(QIcon('todo.png'))
        self.setMinimumSize(400, 500)  # Минимальный размер окна

        # Создание центрального виджета
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()

        # Поле ввода новой задачи
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Введите новую задачу...")
        self.task_input.setStyleSheet("""
            font-size: 16px;
            padding: 8px;
            border: 1px solid #ccc;
        """)
        layout.addWidget(self.task_input)

        # Горизонтальный layout для кнопок
        buttons_layout = QHBoxLayout()

        # Кнопка добавления задачи
        add_button = QPushButton("Добавить")
        add_button.setIcon(QIcon('add.png'))  # Иконка кнопки
        add_button.setIconSize(QSize(24, 24))  # Размер иконки
        add_button.setStyleSheet("""
            font-size: 14px;
            padding: 6px;
        """)
        add_button.clicked.connect(self.add_task)

        # Кнопка удаления задачи
        delete_button = QPushButton("Удалить")
        delete_button.setIcon(QIcon('delete.png'))
        delete_button.setIconSize(QSize(24, 24))
        delete_button.setStyleSheet("""
            font-size: 14px;
            padding: 6px;
        """)
        delete_button.clicked.connect(self.delete_task)

        # Добавление кнопок в layout
        buttons_layout.addWidget(add_button)
        buttons_layout.addWidget(delete_button)
        layout.addLayout(buttons_layout)

        # Список задач
        self.tasks_list = QListWidget()
        self.tasks_list.setStyleSheet("""
            font-size: 16px;
            border: 1px solid #ddd;
        """)
        # Обработчик двойного клика для отметки выполнения
        self.tasks_list.itemDoubleClicked.connect(self.toggle_task)
        layout.addWidget(self.tasks_list)

        main_widget.setLayout(layout)

    def add_task(self):
        """Добавление новой задачи в список"""
        task = self.task_input.text().strip()  # Получаем текст, убираем пробелы
        if task:  # Если строка не пустая
            self.tasks_list.addItem(task)  # Добавляем в список
            self.task_input.clear()  # Очищаем поле ввода

    def delete_task(self):
        """Удаление выбранной задачи"""
        current_item = self.tasks_list.currentItem()  # Получаем выбранный элемент
        if current_item:  # Если элемент выбран
            # Удаляем элемент по его индексу
            self.tasks_list.takeItem(self.tasks_list.row(current_item))

    def toggle_task(self, item):
        """Отметка задачи как выполненной/невыполненной"""
        font = item.font()  # Получаем текущий шрифт
        if font.strikeOut():  # Если текст перечеркнут
            font.setStrikeOut(False)  # Убираем перечеркивание
        else:
            font.setStrikeOut(True)  # Перечеркиваем текст
        item.setFont(font)  # Применяем изменения


if __name__ == '__main__':
    app = QApplication([])
    todo = TodoApp()
    todo.show()
    app.exec_()