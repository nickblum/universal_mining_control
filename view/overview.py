from PyQt5.QtWidgets import (QApplication,QWidget,QTextEdit,QLabel,QLineEdit,QGridLayout,QHBoxLayout,QPushButton,QComboBox,QLayout,QAction)
from PyQt5.QtGui import QFont,QIcon,QColor
from PyQt5.QtCore import pyqtSignal

class ClickableLabel(QLabel):
    """
        A Label that emits a signal when clicked.
    """
    clicked = pyqtSignal()

    def __init__(self, *args):
        super().__init__(*args)

    def mousePressEvent(self, event):
        self.clicked.emit()

class UMCOverview(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        ### TESTING DATA... PRESUMABLY SOMETHIGN LIKE THIS WILL BE AVAILABLE GLOBALLY? ###
        rigs = {
            "Rig1":{
                "name":"Example Rig",
                "description":"Dedicated to alt coins and stuff. Unstable, something something technical jargon.",
                "miners": ['GTX-1070Ti','GTX-1070Ti','GTX-1070Ti','GTX-1070Ti']
            },
            "Rig2":{
                "name":"Another Example Rig",
                "description":"State employees retirement fund",
                "miners": ['GTX-1080','GTX-1070Ti','GTX-1070Ti']
            },
            "Rig3":{
                "name":"Personal Computer",
                "description":"",
                "miners": ['AMD 1600X','GTX-1050Ti']
            },
            "Rig4":{
                "name":"PS3",
                "description":"Why not?",
                "miners": ['Cell microprocessor','NV47']
            }

        }

        grid = QGridLayout(self)
        grid.setSizeConstraint(QLayout.SizeConstraint())
        rigFont = QFont('Helvetica', 10, QFont.Bold)

        self.rigObjs = []
        self.minerObjs = []

        row = 1
        for rigId in rigs:
            rigLabel = ClickableLabel()
            rigLabel.rigId = rigId
            rigLabel.showMiners = True
            rigLabel.setText(rigs[rigId]['name'])
            rigLabel.setFont(rigFont)
            rigLabel.setStyleSheet( 'QLabel { color: #444; background-color: #ddd; padding: 4px; border-radius: 3px; border:1px solid #d6d6d6;} QLabel:hover {background-color:#eee;}' )
            rigLabel.clicked.connect(self.toggleRig)

            subgrid = QGridLayout()
            
            subrow = 1
            for miner in rigs[rigId]['miners']:
                minerLabel = QLabel( text=miner)
                minerLabel.setStyleSheet( 'QLabel { color: #444; }' )
                minerLabel.rigId = rigId
                subgrid.addWidget(minerLabel,subrow,0)
                self.minerObjs.append(minerLabel)
                subrow += 1
            grid.addWidget(rigLabel,row,0,1,45)
            grid.addLayout(subgrid,row+1,1)
            row += 2

        self.show()
    
    def toggleRig(self):
        self.sender().showMiners = (not self.sender().showMiners)
        print(self.sender().showMiners)
        for miner in self.minerObjs:
            if miner.rigId == self.sender().rigId:
                if self.sender().showMiners:
                    miner.show()
                else:
                    miner.hide()