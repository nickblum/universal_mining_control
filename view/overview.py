from PyQt5.QtWidgets import (QApplication,QWidget,QTextEdit,QLabel,QLineEdit,QGridLayout,QHBoxLayout,QPushButton,QComboBox,QLayout)
from PyQt5.QtGui import QFont,QIcon,QColor

class UMCOverview(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        ### TESTING DATA... PRESUMABLY SOMETHIGN LIKE THIS WILL BE AVAILABLE GLOBALLY? ###
        rigs = {
            "RigID1":{
                "name":"Example Rig",
                "description":"Dedicated to alt coins and stuff. Unstable, something something technical jargon.",
                "miners": ['GTX-1070Ti','GTX-1070Ti','GTX-1070Ti','GTX-1070Ti']
            },
            "RigID2":{
                "name":"Another Example Rig",
                "description":"State employees retirement fund",
                "miners": ['GTX-1080','GTX-1070Ti','GTX-1070Ti']
            },
            "RigID3":{
                "name":"Personal Compter",
                "description":"",
                "miners": ['AMD 1600X','GTX-1050Ti']
            }

        }

        grid = QGridLayout(self)
        grid.setSizeConstraint(QLayout.SizeConstraint())
        rigFont = QFont('Helvetica', 10, QFont.Bold)

        row = 1
        for key in rigs:
            rigLabel = QLabel(text=key)
            rigLabel.setFont(rigFont)
            subgrid = QGridLayout()
            subrow = 1
            for miner in rigs[key]['miners']:
                subgrid.addWidget(QLabel(text=miner),subrow,0)
                subrow += 1
            grid.addWidget(rigLabel,row,0)
            grid.addLayout(subgrid,row+1,1)
            row += 2

#TODO Find a proper way to minimize the row/column sizes for the regular items
        grid.addWidget(QLabel(text="placeholder"),row,0,50,50)

        self.show()