from PyQt5.QtWidgets import (QApplication,QWidget,QTextEdit,QLabel,QLineEdit,QGridLayout)

class UMCLoot(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        title = QLabel('Gimme the loot!')
        
        #author = QLabel('Author')
        #review = QLabel('Review')

        #titleEdit = QLineEdit()
        #authorEdit = QLineEdit()
        #reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10) #padding between gridlines

        grid.addWidget(title, 1, 0)
        #grid.addWidget(titleEdit, 1, 1)

        #grid.addWidget(author, 2, 0)
        #grid.addWidget(authorEdit, 2, 1)

        #grid.addWidget(review, 3, 0)
        #grid.addWidget(reviewEdit, 3, 1, 5, 1)
        
        self.setLayout(grid) 
        
        self.show()