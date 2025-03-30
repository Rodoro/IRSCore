from PyQt6.QtWidgets import QComboBox, QLabel, QHBoxLayout, QWidget
from PyQt6.QtCore import pyqtSignal

class SizeSelector(QWidget):
    sizeChanged = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.label = QLabel("Размер ArUco кода:")
        self.combo = QComboBox()
        self.combo.addItems(["4x4", "5x5", "6x6", "7x7"])
        self.combo.setCurrentText("4x4")
        self.current_size = "4x4"
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.combo)
        
        self.combo.currentTextChanged.connect(self.on_size_changed)
    
    def on_size_changed(self, size):
        self.current_size = size
        self.sizeChanged.emit(size)