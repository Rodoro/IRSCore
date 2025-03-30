import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.aruco_display import ArUcoDisplay
from ui.control_panel import ControlPanel

class ArUcoGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генератор ArUco кодов")
        self.setGeometry(100, 100, 900, 600)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)
        
        self.aruco_display = ArUcoDisplay()
        self.control_panel = ControlPanel()
        
        self.control_panel.generateClicked.connect(self.aruco_display.generate_marker)
        self.control_panel.saveClicked.connect(self.aruco_display.save_marker)
        
        layout.addWidget(self.aruco_display)
        layout.addWidget(self.control_panel)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArUcoGeneratorApp()
    window.show()
    sys.exit(app.exec())