from PyQt5.QtWidgets import (QApplication,QWidget,QTextEdit,QLabel,QLineEdit,QGridLayout,QHBoxLayout,QPushButton,QComboBox,QLayout,QAction,QFrame)
from PyQt5.QtGui import QFont,QIcon,QColor,QPixmap
from PyQt5.QtCore import pyqtSignal, Qt
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
        rigs = MakeRigs(6,5,True).rigs

        grid = QGridLayout(self)
        grid.setSizeConstraint(QLayout.SizeConstraint())
        grid.setSpacing(0)
#TODO certainly there's a better solution here. Could be a problem if you have more than 999 mining rigs...
        grid.setRowStretch(1000, 1200)
        
        ### RIG OVERVIEW ###
        self.expandedIcon = QIcon('img/btn-expanded.png')
        self.collapsedIcon = QIcon('img/btn-collapsed.png') 
        self.toggleBtn = QPushButton( self.expandedIcon, '', self )
        self.toggleBtn.expandRigs = True
        self.toggleBtn.setStyleSheet( 'QPushButton {border:none; background-color:transparent; padding: 3px;} QPushButton:hover{background-color: #E5F3FF;} ' )
        self.toggleBtn.clicked.connect(self.toggleAllRigs)
        grid.addWidget(self.toggleBtn,0,0,1,1)

        rigFont = QFont('Helvetica', 10, QFont.Bold)
        rigDescrFont = QFont('Helvetica', 10)

        self.rigObjs = []
        self.minerObjs = []

        row = 1
        for rigId in rigs:
            rigLabel = QLabel(rigs[rigId]['name'])
            rigLabel.setFont(rigFont)
            rigHash = QLabel(str(rigs[rigId]['hashRate']) + ' MH/s')
            rigHash.setAlignment(Qt.AlignRight)
            rigHash.setFont(rigFont)
            rigDescr = QLabel(rigs[rigId]['description'])
            rigDescr.setFont(rigDescrFont)

            rigWrapper = ClickableFrame()
            rigWrapper.setContentsMargins(0, 0, 0, 0)
            rigWrapper.rigId = rigId
            rigWrapper.showMiners = True
            rigWrapper.clicked.connect(self.toggleRig)
            rigWrapper.setObjectName('rigWrapper')
            rigWrapper.setStyleSheet( 'QLabel {color:#444;} QFrame#rigWrapper { background-color: #ddd; padding: 1px 3px; border-radius: 2px; border:1px solid #d6d6d6;} QFrame#rigWrapper:hover {background-color:#eee;}' )
            self.rigObjs.append(rigWrapper)

            rigWrapperGrid = QGridLayout()
            rigWrapperGrid.setSpacing(0)
            rigWrapperGrid.setContentsMargins(0,0,0,0)
            rigWrapperGrid.addWidget(rigLabel,0,0,1,20)
            rigWrapperGrid.addWidget(rigHash,0,20,1,3)
            
            #rigStatus = QFrame()
            #rigStatus.setGeometry(0,0,1,1)
            #rigStatus.setStyleSheet('QWidget {background-color:#6CE679; width: 4px; height:4px; padding:0; margin: 3px 12px; border-radius:5px;}')
            #testimg = QPixmap('img/tab-bitcoin.png')
            #rigWrapperGrid.addWidget(rigStatus,0,23,1,1)
            if rigDescr.text() != '':
                rigWrapperGrid.addWidget(rigDescr,1,1,1,24)
            else:
                rigDescr.close()
            rigWrapperGrid.setRowStretch(1000, 1200)
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
                
            grid.addWidget(rigWrapper,row,0,1,24)
            grid.addLayout(subgrid,row+1,1,1,23)
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
        self.sender().showMiners = not self.sender().showMiners
        for miner in self.minerObjs:
            if miner.rigId == self.sender().rigId:
                if self.sender().showMiners:
                    miner.show()
                else:
                    miner.hide()
    
    
                    
        