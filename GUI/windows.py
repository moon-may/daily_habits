import sys
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Установка параметров окна
        self.setGeometry(100, 100, 1000, 700)
        self.setWindowTitle('Трекер привычек')

        # Установка центрального виджета
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)

        # Левая панель содержит список всех привычек
        left_bar = QWidget()
        left_layout = QVBoxLayout(left_bar)

        self.habits_list = QListWidget()
        left_layout.addWidget(self.habits_list)

        add_habit_btn = QPushButton('Добавить привычку')
        left_layout.addWidget(add_habit_btn)

        main_layout.addWidget(left_bar, 1)

        # Правая панель
        self.stats_bar = QLabel('Статистика')
        main_layout.addWidget(self.stats_bar, 2)




app = QApplication(sys.argv)
app.setStyle("Fusion")
main_window = MainWindow()
main_window.show()
app.exec()
