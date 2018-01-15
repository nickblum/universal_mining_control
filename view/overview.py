from PyQt5.QtWidgets import (QApplication,QWidget,QTextEdit,QLabel,QLineEdit,QGridLayout,QHBoxLayout,QPushButton,QComboBox,QLayout,QAction,QFrame)
from PyQt5.QtGui import QFont,QIcon,QColor
from PyQt5.QtCore import pyqtSignal
from .TestingTools import MakeRigs

class ClickableFrame(QFrame):
    """
        A Frame that emits a signal when clicked.
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
        rigs = MakeRigs(4,5,True).rigs

        grid = QGridLayout(self)
        grid.setSizeConstraint(QLayout.SizeConstraint())
        grid.setSpacing(0)
#TODO certainly there's a better solution here. Could be a problem if you have more than 999 mining rigs...
        grid.setRowStretch(1000, 1200)
        

        ### RIG OVERVIEW ###)
        self.expandedIcon = QIcon('img/btn-expanded.png')
        self.collapsedIcon = QIcon('img/btn-collapsed.png') 
        self.toggleBtn = QPushButton( self.expandedIcon, '', self )
        self.toggleBtn.expandRigs = True
        self.toggleBtn.setStyleSheet( 'QPushButton {border:none; background-color:transparent; padding: 3px;} QPushButton:hover{background-color: #E5F3FF;} ' )
        self.toggleBtn.clicked.connect(self.toggleAllRigs)
        grid.addWidget(self.toggleBtn,0,0,1,1)

        ### RIG LIST ###
        rigFont = QFont('Helvetica', 10, QFont.Bold)

        self.rigObjs = []
        self.minerObjs = []

        row = 1
        for rigId in rigs:
            rigLabel = QLabel()
            rigLabel.rigId = rigId
            rigLabel.showMiners = True
            rigLabel.setText(rigs[rigId]['name'])
            rigLabel.setFont(rigFont)
            #rigLabel.setStyleSheet( 'QLabel { color: #444; background-color: #ddd; padding: 4px; border-radius: 3px; border:1px solid #d6d6d6;} QLabel:hover {background-color:#eee;}' )
            #rigLabel.clicked.connect(self.toggleRig)
            self.rigObjs.append(rigLabel)

            rigDescr = QLabel(rigs[rigId]['description'])

            rigWrapper = ClickableFrame()
            rigWrapper.clicked.connect(self.toggleRig)
            rigWrapper.setObjectName('rigWrapper')
            rigWrapper.setStyleSheet( 'QFrame#rigWrapper { color: #444; background-color: #ddd; padding: 0px; border-radius: 3px; border:1px solid #d6d6d6;} QFrame#rigWrapper:hover {background-color:#eee;}' )
            rigWrapperGrid = QGridLayout()
            rigWrapperGrid.setSpacing(0)
            rigWrapperGrid.addWidget(rigLabel,0,0,1,24)
            rigWrapperGrid.addWidget(rigDescr,1,1,1,24)
            rigWrapper.setLayout(rigWrapperGrid)
            

            subgrid = QGridLayout()
            
            subrow = 1
            for minerId, miner in rigs[rigId]['miners'].items():
                minerLabel = QLabel( text=miner['type'] )
                minerLabel.setStyleSheet( 'QLabel { color: #444;padding:4px; background-color: white;} QLabel:hover { background-color: #eaf2ff;}' )
                minerLabel.rigId = rigId
                subgrid.addWidget(minerLabel,subrow,0)
                self.minerObjs.append(minerLabel)
                subrow += 1
#TODO really need to figure out this grid stuff... maybe Hbox layout instead?
            grid.addWidget(rigWrapper,row,0,1,24)
            grid.addLayout(subgrid,row+2,1,1,23)
            row += 2

        self.show()
    
    def toggleAllRigs(self):
        self.toggleBtn.expandRigs = not self.toggleBtn.expandRigs
        if self.toggleBtn.expandRigs:
            self.toggleBtn.setIcon( self.expandedIcon )
        else:
            self.toggleBtn.setIcon( self.collapsedIcon )
        
        for rig in self.rigObjs:
            rig.showMiners = self.toggleBtn.expandRigs
        
        for miner in self.minerObjs:
            if self.toggleBtn.expandRigs:
                miner.show()
            else:
                miner.hide()

    def toggleRig(self):
        print('frame click')
        '''
        self.sender().showMiners = not self.sender().showMiners
        for miner in self.minerObjs:
            if miner.rigId == self.sender().rigId:
                if self.sender().showMiners:
                    miner.show()
                else:
                    miner.hide()'''
    
    
                    
        