from PyQt6.QtWidgets import QComboBox, QLabel, QHBoxLayout, QWidget
from PyQt6.QtCore import pyqtSignal

class DictSelector(QWidget):
    dictChanged = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.label = QLabel("Тип словаря:")
        self.combo = QComboBox()
        
        # Добавляем все варианты словарей
        self.combo.addItems([
            "DICT_4X4_50", "DICT_4X4_100", "DICT_4X4_250", "DICT_4X4_1000",
            "DICT_5X5_50", "DICT_5X5_100", "DICT_5X5_250", "DICT_5X5_1000",
            "DICT_6X6_50", "DICT_6X6_100", "DICT_6X6_250", "DICT_6X6_1000",
            "DICT_7X7_50", "DICT_7X7_100", "DICT_7X7_250", "DICT_7X7_1000"
        ])
        
        self.current_dict = "DICT_4X4_50"
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.combo)
        
        self.combo.currentTextChanged.connect(self.on_dict_changed)
    
    def on_dict_changed(self, dict_type):
        self.current_dict = dict_type
        self.dictChanged.emit(dict_type)