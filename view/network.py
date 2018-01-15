from PyQt5.QtWidgets import (QApplication,QWidget,QTextEdit,QLabel,QLineEdit,QGridLayout,QTableWidget,QTableWidgetItem)

class UMCNetwork(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.table 	= QTableWidget()
        self.tableItem 	= QTableWidgetItem()
 
        # initiate table
        self.table.setWindowTitle("QTableWidget Example @pythonspot.com")
        self.table.resize(400, 250)
        self.table.setRowCount(4)
        self.table.setColumnCount(2)
    
        # set data
        self.table.setItem(0,0, QTableWidgetItem("Item (1,1)"))
        self.table.setItem(0,1, QTableWidgetItem("Item (1,2)"))
        self.table.setItem(1,0, QTableWidgetItem("Item (2,1)"))
        self.table.setItem(1,1, QTableWidgetItem("Item (2,2)"))
        self.table.setItem(2,0, QTableWidgetItem("Item (3,1)"))
        self.table.setItem(2,1, QTableWidgetItem("Item (3,2)"))
        self.table.setItem(3,0, QTableWidgetItem("Item (4,1)"))
        self.table.setItem(3,1, QTableWidgetItem("Item (4,2)"))
    
        # show table
        #table.show()
        
        title = QLabel('Network')
        grid = QGridLayout()
        grid.setSpacing(10) #padding between gridlines
        grid.addWidget(title, 1, 0)
        grid.addWidget(self.table, 1, 0)

        
        self.setLayout(grid) 
        self.show()