import sys

import keyboard
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel, QMessageBox, QLineEdit
)
from PyQt5.QtCore import QTimer


class TextPrinterApp(QWidget):
    def __init__(self):
        super().__init__()

        # Настройка окна
        self.setWindowTitle("Text Printer")
        self.resize(400, 300)

        # Основной макет
        layout = QVBoxLayout(self)

        # Поле для ввода времени задержки
        self.delay_label = QLabel("Введите время задержки (с):", self)
        self.delay_input = QLineEdit(self)
        self.delay_input.setPlaceholderText("Например, 3")
        layout.addWidget(self.delay_label)
        layout.addWidget(self.delay_input)

        # Поле для ввода текста
        self.text_label = QLabel("Введите текст для вставки (абзацы поддерживаются):", self)
        self.text_input = QTextEdit(self)
        layout.addWidget(self.text_label)
        layout.addWidget(self.text_input)

        # Кнопка "Печать"
        self.print_button = QPushButton("Печать", self)
        layout.addWidget(self.print_button)

        # Связываем кнопку с обработчиком
        self.print_button.clicked.connect(self.handle_print)

    def handle_print(self):
        # Получаем задержку
        try:
            delay = int(self.delay_input.text().strip())
            if delay < 0:
                raise ValueError
        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Введите корректное положительное время!")
            return

        # Получаем текст
        text = self.text_input.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, "Предупреждение", "Поле текста не может быть пустым!")
            return

        self.print_button.setEnabled(False)
        # Задержка и вывод текста
        QTimer.singleShot(delay * 1000, lambda: self.print_text(text))

    def print_text(self, text):
        keyboard.write(text)
        self.print_button.setEnabled(True)


# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TextPrinterApp()
    window.show()

    sys.exit(app.exec_())
