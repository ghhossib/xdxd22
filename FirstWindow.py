import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton


class FirstWindow(QMainWindow): #Создал класс FirstWindow, родители которого является QMainWindow
    def __init__(self):# создал конструктор
        super().__init__() #передал все атрибуты из конструктора
        self.setWindowTitle('Первое окно')
        self.setGeometry(100,100,400,300)

        self.label = QLabel('КУ',self)
        self.label.move(150,50) # задал кординаты label в окне

        self.button = QPushButton('Кнопка',self)
        self.button.move(150,100)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.label.setText('Нажал ываываываыываыва')
        self.label.adjustSize()



if __name__ == "__main__":
    app = QApplication(sys.argv) #объект для создания окна
    window = FirstWindow() #объект класса FirstWindow - Окно
    window.show() # для объекта window применяя метод show()
    sys.exit(app.exec_()) #из библиотеки sys используется метод