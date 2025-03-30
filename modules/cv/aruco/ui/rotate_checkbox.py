from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtCore import pyqtSignal

class RotateCheckbox(QCheckBox):
    rotateChanged = pyqtSignal(bool)
    
    def __init__(self):
        super().__init__("Разрешить поворот кодов")
        self.is_rotated = False
        self.stateChanged.connect(self.on_state_changed)
    
    def on_state_changed(self, state):
        self.is_rotated = state == 2
        self.rotateChanged.emit(self.is_rotated)