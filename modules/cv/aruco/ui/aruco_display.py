from PyQt6.QtWidgets import (QLabel, QVBoxLayout, QWidget, QFileDialog, 
                            QMessageBox)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
import cv2
import cv2.aruco as aruco
from utils.aruco_utils import get_aruco_dict

class ArUcoDisplay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(300, 300)
        self.layout = QVBoxLayout(self)
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.image_label)
        
        self.current_id = 0
        self.current_dict = "DICT_4X4_50"
        self.image_size = 400
        
    def generate_marker(self, marker_id, dict_type, image_size):
        self.current_id = marker_id
        self.current_dict = dict_type
        self.image_size = image_size
        
        try:
            aruco_dict = get_aruco_dict(dict_type)
            
            max_id = int(dict_type.split("_")[-1]) - 1
            if marker_id < 0 or marker_id > max_id:
                raise ValueError(f"ID должен быть в диапазоне 0-{max_id} для выбранного словаря")
            
            marker_img = aruco.generateImageMarker(aruco_dict, marker_id, self.image_size)
            marker_img = cv2.cvtColor(marker_img, cv2.COLOR_GRAY2RGB)
            
            height, width, channel = marker_img.shape
            bytes_per_line = 3 * width
            q_img = QImage(marker_img.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)
            
            self.image_label.setPixmap(pixmap)
            
        except ValueError as e:
            self.show_error("Некорректный ID маркера", str(e))
        except Exception as e:
            self.show_error("Ошибка генерации маркера", str(e))
    
    def save_marker(self):
        options = QFileDialog.Option()
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Сохранить ArUco маркер",
            "",
            "JPEG Images (*.jpg);;PNG Images (*.png)",
            options=options
        )
        
        if file_path:
            try:
                aruco_dict = get_aruco_dict(self.current_dict)
                marker_img = aruco.generateImageMarker(aruco_dict, self.current_id, self.image_size)
                marker_img = cv2.cvtColor(marker_img, cv2.COLOR_GRAY2RGB)
                cv2.imwrite(file_path, marker_img)
                
                QMessageBox.information(
                    self, 
                    "Сохранение успешно", 
                    f"Маркер успешно сохранен как:\n{file_path}"
                )
            except Exception as e:
                self.show_error("Ошибка сохранения маркера", str(e))
    
    def show_error(self, title, message):
        QMessageBox.critical(
            self,
            title,
            message,
            QMessageBox.StandardButton.Ok
        )