import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)  # Загрузить интерфейс из файла

        self.circles = []  # список для хранения окружностей (диаметр, позиция)
        self.pushButton.clicked.connect(self.draw_circles)

    def draw_circles(self):
        # Генерируем случайный диаметр и добавляем окружность
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((diameter, x, y))
        self.update()  # перерисовать окно

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        for diameter, x, y in self.circles:
            painter.setBrush(QColor(255, 255, 0))  # желтый цвет
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())