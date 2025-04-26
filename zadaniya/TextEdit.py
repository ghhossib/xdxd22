# Импорт необходимых модулей
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit,
                             QFileDialog, QAction, QToolBar)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt


class TextEditor(QMainWindow):
    def __init__(self):
        """
        Инициализация текстового редактора.
        """
        super().__init__()

        # Настройка основного окна
        self.setWindowTitle("Текстовый редактор")
        self.setWindowIcon(QIcon('editor.png'))
        self.setMinimumSize(600, 500)  # Минимальный размер окна

        # Создание текстового поля
        self.text_edit = QTextEdit()
        self.text_edit.setStyleSheet("""
            font-size: 14px;
            border: none;
        """)
        self.setCentralWidget(self.text_edit)  # Установка как центрального виджета

        # Создание меню и тулбара
        self.create_menu()
        self.create_toolbar()

    def create_menu(self):
        """Создание меню приложения"""
        # Меню "Файл"
        file_menu = self.menuBar().addMenu("Файл")

        # Действие "Новый"
        new_action = QAction(QIcon('new.png'), "Новый", self)
        new_action.setShortcut(QKeySequence.New)  # Горячая клавиша Ctrl+N
        new_action.setToolTip("Создать новый документ")  # Подсказка
        new_action.triggered.connect(self.new_file)

        # Действие "Открыть"
        open_action = QAction(QIcon('open.png'), "Открыть", self)
        open_action.setShortcut(QKeySequence.Open)  # Ctrl+O
        open_action.setToolTip("Открыть файл")
        open_action.triggered.connect(self.open_file)

        # Действие "Сохранить"
        save_action = QAction(QIcon('save.png'), "Сохранить", self)
        save_action.setShortcut(QKeySequence.Save)  # Ctrl+S
        save_action.setToolTip("Сохранить файл")
        save_action.triggered.connect(self.save_file)

        # Добавление действий в меню
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

    def create_toolbar(self):
        """Создание панели инструментов"""
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Добавление кнопок на тулбар
        toolbar.addAction(self.findChild(QAction, "Новый"))
        toolbar.addAction(self.findChild(QAction, "Открыть"))
        toolbar.addAction(self.findChild(QAction, "Сохранить"))

    def new_file(self):
        """Создание нового документа"""
        self.text_edit.clear()  # Очистка текстового поля

    def open_file(self):
        """Открытие файла"""
        # Диалог выбора файла
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Открыть файл",
            "",
            "Текстовые файлы (*.txt);;Все файлы (*)"
        )
        if filename:  # Если файл выбран
            with open(filename, 'r', encoding='utf-8') as file:
                self.text_edit.setText(file.read())  # Загрузка текста

    def save_file(self):
        """Сохранение файла"""
        # Диалог сохранения файла
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Сохранить файл",
            "",
            "Текстовые файлы (*.txt);;Все файлы (*)"
        )
        if filename:  # Если указано имя файла
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(self.text_edit.toPlainText())  # Сохранение текста


if __name__ == '__main__':
    app = QApplication([])
    editor = TextEditor()
    editor.show()
    app.exec_()