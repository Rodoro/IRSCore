from PyQt6.QtWidgets import QLineEdit, QLabel, QHBoxLayout, QWidget
from PyQt6.QtGui import QIntValidator

class IdInput(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)
        self.label = QLabel("Введите ID маркера:")
        self.input = QLineEdit()
        self.input.setText("0")
        self.input.setValidator(QIntValidator(0, 9999))
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
    
    def get_id(self):
        try:
            return int(self.input.text())
        except ValueError:
            return 0