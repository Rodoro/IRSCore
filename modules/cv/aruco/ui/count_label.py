from PyQt6.QtWidgets import QLabel

class CountLabel(QLabel):
    def __init__(self):
        super().__init__("Доступно кодов: 0")
    
    def update_count(self, count):
        self.setText(f"Доступно кодов: {count}")