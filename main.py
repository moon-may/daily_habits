import sys
from PySide6.QtWidgets import *
from core.models import *
from core.database import *
from GUI.windows import MainWindow

app = QApplication(sys.argv)

font = app.font()
font.setPointSize(14)
app.setFont(font)

app.setStyle("Fusion")
main_window = MainWindow()
main_window.show()
app.exec()