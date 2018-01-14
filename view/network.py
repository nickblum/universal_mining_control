from PyQt5.QtWidgets import (QApplication,QWidget,QTextEdit,QLabel,QLineEdit,QGridLayout)

class UMCNetwork(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        title = QLabel('Network')
        grid = QGridLayout()
        grid.setSpacing(10) #padding between gridlines
        grid.addWidget(title, 1, 0)
        
        self.setLayout(grid) 
        self.show()