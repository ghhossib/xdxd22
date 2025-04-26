# Импорт необходимых модулей из PyQt5
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox)


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()  # Вызов конструктора родительского класса QWidget

        # Настройка основного окна
        self.setWindowTitle("Форма входа")  # Установка заголовка окна
        self.setFixedSize(300, 200)  # Фиксированный размер окна

        # Создание элементов интерфейса
        self.username_label = QLabel("Имя пользователя:")  # Метка для поля ввода имени
        self.username_input = QLineEdit()  # Поле ввода имени

        self.password_label = QLabel("Пароль:")  # Метка для поля ввода пароля
        self.password_input = QLineEdit()  # Поле ввода пароля
        self.password_input.setEchoMode(QLineEdit.Password)  # Скрытие вводимых символов пароля

        self.login_button = QPushButton("Войти")  # Кнопка входа
        self.login_button.clicked.connect(self.check_credentials)  # Подключение обработчика нажатия

        # Настройка основного вертикального расположения элементов
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)  # Добавление метки имени
        layout.addWidget(self.username_input)  # Добавление поля ввода имени
        layout.addWidget(self.password_label)  # Добавление метки пароля
        layout.addWidget(self.password_input)  # Добавление поля ввода пароля

        # Горизонтальное расположение для кнопки (чтобы выровнять по правому краю)
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Растягиваемое пространство слева
        button_layout.addWidget(self.login_button)  # Добавление кнопки

        layout.addLayout(button_layout)  # Добавление горизонтального layout в основной
        self.setLayout(layout)  # Установка layout для виджета

    def check_credentials(self):
        """Метод проверки введенных данных"""
        username = self.username_input.text()  # Получение введенного имени
        password = self.password_input.text()  # Получение введенного пароля

        if not username or not password:
            # Если одно из полей пустое
            QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены")
        elif len(password) < 6:
            # Если пароль слишком короткий
            QMessageBox.warning(self, "Ошибка", "Пароль должен содержать не менее 6 символов")
        else:
            # Если все в порядке
            QMessageBox.information(self, "Успех", f"Добро пожаловать, {username}")


if __name__ == '__main__':
    # Точка входа в приложение
    app = QApplication([])  # Создание объекта приложения
    form = LoginForm()  # Создание экземпляра формы
    form.show()  # Отображение формы
    app.exec_()  # Запуск основного цикла приложения