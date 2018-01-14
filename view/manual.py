from PyQt5.QtWidgets import (QApplication,QWidget,QTextEdit,QLabel,QLineEdit,QGridLayout,QPushButton,QComboBox)

class UMCManual(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        comboBox = QComboBox(self)
        comboBox.addItem("Bitcoin")
        comboBox.addItem("Monero")

        grid = QGridLayout()
        grid.setSpacing(10) #padding between gridlines

        grid.addWidget(QLabel('Manual Miner v1.2'), 1, 0)
        grid.addWidget(QLabel('Select Currency:'), 2, 0)
        grid.addWidget(comboBox, 2, 1)
        grid.addWidget(QLabel('Guess a Hash:'), 3, 0)
        grid.addWidget(QLineEdit(), 3, 1, 1, 4 )#row,col,rowspan,colspan
        grid.addWidget(QPushButton("Submit", self), 4, 1)
        
        self.setLayout(grid) 
        
        self.show()