import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt

# Класс интерфейса
class MyUI:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        self.parent.setWindowTitle("Круги случайных цветов и размеров")
        self.parent.setGeometry(100, 100, 600, 400)

        self.button = QPushButton("Нарисовать окружности", self.parent)
        self.button.setGeometry(10, 10, 200, 40)


# Основной класс окна
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # подключаем интерфейс
        self.ui = MyUI(self)

        self.circles = []

        # соединяем сигнал кнопки с обработчиком
        self.ui.button.clicked.connect(self.draw_circles)

    def draw_circles(self):
        # Генерируем случайный диаметр и цвет
        diameter = random.randint(10, 100)
        color = QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        x = random.randint(0, self.width() - diameter)
        y = random.randint(50, self.height() - diameter)  # избегаем области с кнопкой
        self.circles.append((diameter, color, x, y))
        self.update()  # перерисовать окно

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        for diameter, color, x, y in self.circles:
            painter.setBrush(color)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())