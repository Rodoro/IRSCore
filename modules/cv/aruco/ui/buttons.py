from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import pyqtSignal

class Buttons(QWidget):
    generateClicked = pyqtSignal()
    saveClicked = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        
        self.generate_btn = QPushButton("Сгенерировать")
        self.save_btn = QPushButton("Сохранить как JPG (400x400)")
        
        self.generate_btn.clicked.connect(self.generateClicked)
        self.save_btn.clicked.connect(self.saveClicked)
        
        self.layout.addWidget(self.generate_btn)
        self.layout.addWidget(self.save_btn)