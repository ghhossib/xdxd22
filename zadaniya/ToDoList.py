from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QListWidget, QLineEdit, QPushButton, QHBoxLayout)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon


class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Список дел")
        self.setWindowIcon(QIcon('todo.png'))
        self.setMinimumSize(400, 500)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()

        # Поле ввода
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Введите новую задачу...")
        self.task_input.setStyleSheet("font-size: 16px; padding: 8px;")
        layout.addWidget(self.task_input)

        # Кнопки
        buttons_layout = QHBoxLayout()

        add_button = QPushButton("Добавить")
        add_button.setIcon(QIcon('add.png'))
        add_button.setIconSize(QSize(24, 24))
        add_button.clicked.connect(self.add_task)

        delete_button = QPushButton("Удалить")
        delete_button.setIcon(QIcon('delete.png'))
        delete_button.setIconSize(QSize(24, 24))
        delete_button.clicked.connect(self.delete_task)

        buttons_layout.addWidget(add_button)
        buttons_layout.addWidget(delete_button)
        layout.addLayout(buttons_layout)

        # Список задач
        self.tasks_list = QListWidget()
        self.tasks_list.setStyleSheet("font-size: 16px;")
        self.tasks_list.itemDoubleClicked.connect(self.toggle_task)
        layout.addWidget(self.tasks_list)

        main_widget.setLayout(layout)

    def add_task(self):
        task = self.task_input.text()
        if task:
            self.tasks_list.addItem(task)
            self.task_input.clear()

    def delete_task(self):
        current_item = self.tasks_list.currentItem()
        if current_item:
            self.tasks_list.takeItem(self.tasks_list.row(current_item))

    def toggle_task(self, item):
        if item.font().strikeOut():
            font = item.font()
            font.setStrikeOut(False)
            item.setFont(font)
        else:
            font = item.font()
            font.setStrikeOut(True)
            item.setFont(font)


if __name__ == '__main__':
    app = QApplication([])
    todo = TodoApp()
    todo.show()
    app.exec_()