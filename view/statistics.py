from PyQt5.QtWidgets import (QApplication,QWidget,QTextEdit,QLabel,QLineEdit,QGridLayout,QProgressBar)
from PyQt5.QtCore import QBasicTimer

class UMCStats(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(100, self)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()
        
    def timerEvent(self, e):
      
        if self.step >= 96:
            
            self.timer.stop()
            self.pbar.setValue(self.step)
            return
            
        self.step = self.step + 1
        self.pbar.setValue(self.step)