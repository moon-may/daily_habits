from PySide6.QtWidgets import *
from core.models import *

class MainWindow(QMainWindow):
    '''Главное окно приложения'''
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
        add_habit_btn.clicked.connect(self.add_habit_clicked)
        left_layout.addWidget(add_habit_btn)

        main_layout.addWidget(left_bar, 1)

        # Правая панель
        self.stats_bar = QLabel('Статистика')
        main_layout.addWidget(self.stats_bar, 2)


    def add_habit_clicked(self):
        dialog = AddHabitWindow()
        if dialog.exec() == QDialog.DialogCode.Accepted:
            habit_name = dialog.name_input.text()
            habit_type = dialog.type_input.currentText()
            unit = dialog.unit_input.text()
            goal = dialog.goal_input.value()
            add_habit((habit_name, habit_type, unit, goal))



class AddHabitWindow(QDialog):
    '''Диалоговое окно для добавления новой привычки'''
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 120, 500, 700)
        self.setWindowTitle('Добавить привычку')

        layout = QVBoxLayout(self)

        form = QFormLayout()
        self.name_input = QLineEdit()
        self.type_input = QComboBox()
        self.type_input.addItems(['Выполнено', 'Счетчик', 'Время'])
        self.unit_input = QLineEdit()
        self.goal_input = QSpinBox()

        form.addRow('Название: ', self.name_input)
        form.addRow('Тип: ', self.type_input)
        form.addRow('В чем будем измерять? ', self.unit_input)
        form.addRow('Ежедневная цель: ', self.goal_input)

        layout.addLayout(form)

        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)




