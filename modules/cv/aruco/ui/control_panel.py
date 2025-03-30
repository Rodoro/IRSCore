from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QSpinBox, 
                            QLabel, QHBoxLayout, QMessageBox)
from PyQt6.QtCore import pyqtSignal
from ui.dict_selector import DictSelector
from ui.id_input import IdInput
from ui.count_label import CountLabel
from ui.buttons import Buttons

class ControlPanel(QWidget):
    generateClicked = pyqtSignal(int, str, int)
    saveClicked = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        
        self.dict_selector = DictSelector()
        self.id_input = IdInput()
        self.count_label = CountLabel()
        self.size_selector = self.create_size_selector()
        self.buttons = Buttons()
        
        self.dict_selector.dictChanged.connect(self.update_count)
        self.buttons.generateClicked.connect(self.emit_generate)
        self.buttons.saveClicked.connect(self.saveClicked)
        
        self.layout.addWidget(self.dict_selector)
        self.layout.addWidget(self.count_label)
        self.layout.addWidget(self.id_input)
        self.layout.addWidget(self.size_selector)
        self.layout.addWidget(self.buttons)
        
        self.update_count()
    
    def create_size_selector(self):
        widget = QWidget()
        layout = QHBoxLayout(widget)
        label = QLabel("Размер изображения:")
        self.size_spinbox = QSpinBox()
        self.size_spinbox.setRange(100, 2000)
        self.size_spinbox.setValue(400)
        self.size_spinbox.setSingleStep(50)
        
        layout.addWidget(label)
        layout.addWidget(self.size_spinbox)
        return widget
    
    def update_count(self):
        dict_type = self.dict_selector.current_dict
        max_ids = int(dict_type.split("_")[-1]) 
        self.count_label.update_count(max_ids)
    
    def emit_generate(self):
        try:
            marker_id = self.id_input.get_id()
            dict_type = self.dict_selector.current_dict
            image_size = self.size_spinbox.value()
            
            max_id = int(dict_type.split("_")[-1]) - 1
            if marker_id < 0 or marker_id > max_id:
                raise ValueError(f"ID должен быть в диапазоне 0-{max_id} для выбранного словаря")
            
            self.generateClicked.emit(marker_id, dict_type, image_size)
            
        except ValueError as e:
            QMessageBox.warning(
                self,
                "Некорректный ID",
                str(e),
                QMessageBox.StandardButton.Ok
            )