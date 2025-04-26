from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit,
                             QFileDialog, QAction, QToolBar)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Текстовый редактор")
        self.setWindowIcon(QIcon('editor.png'))
        self.setMinimumSize(600, 500)

        # Текстовое поле
        self.text_edit = QTextEdit()
        self.text_edit.setStyleSheet("font-size: 14px;")
        self.setCentralWidget(self.text_edit)

        # Создание меню
        self.create_menu()

        # Создание тулбара
        self.create_toolbar()

    def create_menu(self):
        # Меню Файл
        file_menu = self.menuBar().addMenu("Файл")

        new_action = QAction(QIcon('new.png'), "Новый", self)
        new_action.setShortcut(QKeySequence.New)
        new_action.triggered.connect(self.new_file)

        open_action = QAction(QIcon('open.png'), "Открыть", self)
        open_action.setShortcut(QKeySequence.Open)
        open_action.triggered.connect(self.open_file)

        save_action = QAction(QIcon('save.png'), "Сохранить", self)
        save_action.setShortcut(QKeySequence.Save)
        save_action.triggered.connect(self.save_file)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        toolbar.addAction(self.findChild(QAction, "Новый"))
        toolbar.addAction(self.findChild(QAction, "Открыть"))
        toolbar.addAction(self.findChild(QAction, "Сохранить"))

    def new_file(self):
        self.text_edit.clear()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Текстовые файлы (*.txt);;Все файлы (*)")
        if filename:
            with open(filename, 'r', encoding='utf-8') as file:
                self.text_edit.setText(file.read())

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Текстовые файлы (*.txt);;Все файлы (*)")
        if filename:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(self.text_edit.toPlainText())


if __name__ == '__main__':
    app = QApplication([])
    editor = TextEditor()
    editor.show()
    app.exec_()