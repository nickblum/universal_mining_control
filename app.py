import sys
from view.overview import UMCOverview
from view.statistics import UMCStats
from view.loot import *
from view.network import UMCNetwork
from view.manual import UMCManual
from view.settings import UMCSettings
from PyQt5.QtCore import Qt, QSize#, pyqtSignal, QObject
from PyQt5.QtWidgets import (QApplication,QWidget,QMainWindow,QAction,QMenu,qApp,QDesktopWidget,QMessageBox,QActionGroup,QStackedWidget,QHBoxLayout,QToolBar,QSizePolicy,QLabel)#,,QDesktopWidget,QTextEdit,QLabel,QLineEdit,QGridLayout
from PyQt5.QtGui import QIcon,QFont

class UMC(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
#TODO: Move actions somewhere else? Seems like this could get cluttered quickly
        ### ACTIONS ###
        menuHelpAboutAct = QAction('&About UMC', self)
        menuHelpAboutAct.triggered.connect(self.showDialogAbout)
        menuFileExitAct = QAction('&Exit', self) #QIcon('img/icon.png'), 
        menuFileExitAct.setShortcut('Ctrl+Q')
        menuFileExitAct.setStatusTip('Exit application')
        menuFileExitAct.triggered.connect(qApp.quit)
        menuViewThemeLightAct = QAction('Light', self, checkable=True)
        menuViewThemeLightAct.setChecked(True)
        menuViewThemeLightAct.triggered.connect(self.toggleTheme)
        menuViewThemeDarkAct = QAction('Dark', self, checkable=True)
        menuViewThemeDarkAct.triggered.connect(self.toggleTheme)

        tabMarketAct = QAction(QIcon('img/tab-bitcoin.png'), 'Loot', self)
        tabMarketAct.triggered.connect(self.switchAppTab)
        tabManualAct = QAction(QIcon('img/tab-muscle.png'), 'John Henry Mode', self)
        tabManualAct.triggered.connect(self.switchAppTab)
        tabNetworkAct = QAction(QIcon('img/tab-network.png'), 'Network', self)
        tabNetworkAct.triggered.connect(self.switchAppTab)
        tabOverviewAct = QAction(QIcon('img/tab-home.png'), 'Overview', self)
        tabOverviewAct.triggered.connect(self.switchAppTab)
        tabSettingsAct = QAction(QIcon('img/tab-settings.png'), 'Settings', self)
        tabSettingsAct.triggered.connect(self.switchAppTab)
        tabStatsAct = QAction(QIcon('img/tab-graph.png'), 'Statistics', self)
        tabStatsAct.triggered.connect(self.switchAppTab)
        tabStatusAct = QAction(QIcon('img/tab-status-ok.png'), 'Status', self)
        tabStatusAct.triggered.connect(self.switchAppTab)

        ### MENU BAR ###
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(menuFileExitAct)
        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(menuHelpAboutAct)
        
        themesMenu = QMenu('Theme', self)
        ag = QActionGroup(self, exclusive=True)
        themesMenu.addAction(ag.addAction(menuViewThemeLightAct))
        themesMenu.addAction(ag.addAction(menuViewThemeDarkAct))
        viewMenu = menubar.addMenu('&View')
        viewMenu.addMenu(themesMenu)

        ### TOOLBAR ###
        toolbarFont = QFont('Helvetica', 10, QFont.Bold)
        self.toolbar = QToolBar(self)
        self.toolbar.setStyleSheet('QToolBar QToolButton,QToolBar QLabel { padding: 4; color: #555;}')
        self.toolbar.setIconSize(QSize(24, 24))
        self.toolbar.setObjectName("toolBar")
        self.toolbar.setMovable( False )
        self.addToolBar(Qt.ToolBarArea(Qt.TopToolBarArea), self.toolbar)
        self.toolbar.addAction(tabOverviewAct)
        self.toolbar.addAction(tabStatsAct)
        self.toolbar.addAction(tabNetworkAct)
        self.toolbar.addAction(tabMarketAct)
        self.toolbar.addAction(tabSettingsAct)
        self.toolbar.addSeparator()
        self.toolbar.addAction(tabManualAct)
        
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.toolbar.addWidget(spacer)
        self.btcLbl = QLabel("0.003007 BTC ($41.50 USD)/Day")
        self.btcLbl.setFont(toolbarFont)
        self.toolbar.addWidget(self.btcLbl)
        self.hashLbl = QLabel("2763.45 MH/s")
        self.hashLbl.setFont(toolbarFont)
        self.toolbar.addWidget(self.hashLbl)
        self.toolbar.addAction(tabStatusAct)
        
        ### BODY ###
        self.Stack = QStackedWidget (self)
        self.Stack.addWidget(UMCOverview(self))
        self.Stack.addWidget(UMCStats(self))
        self.Stack.addWidget(UMCNetwork(self))
        self.Stack.addWidget(UMCLoot(self))
        self.Stack.addWidget(UMCSettings(self))
        self.Stack.addWidget(UMCManual(self))
        self.setCentralWidget(self.Stack)

        ### MAIN WINDOW ###
        self.setWindowTitle('Univeral Mining Control')
        self.setStyleSheet("QMainWindow {background: '#FFF';}")
        self.setWindowIcon(QIcon('img/icon.png'))         
        self.resize(800, 600)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

# TODO this keypress is pretty handy for testing, probably needs to go away though
    def keyPressEvent(self, e): 
        if e.key() == Qt.Key_Escape:
            self.close()

    def showDialogAbout(self):
        msgBox = QMessageBox()
        msgBox.setText("Look! I made this!")
        msgBox.setWindowIcon(QIcon('img/qmessagebox-info.png'))
        msgBox.setWindowTitle("About Universal Mining Control")
        msgBox.exec_()

    def switchAppTab(self):
#TODO attach index to widget so the order can change without breaking things..
        if self.sender().text() == "Overview":
            self.Stack.setCurrentIndex(0)
        elif self.sender().text() == "Statistics":
            self.Stack.setCurrentIndex(1)
        elif self.sender().text() == "Network":
            self.Stack.setCurrentIndex(2)
        elif self.sender().text() == "Loot":
            self.Stack.setCurrentIndex(3)
        elif self.sender().text() == "Settings":
            self.Stack.setCurrentIndex(4)
        elif self.sender().text() == "John Henry Mode":
            self.Stack.setCurrentIndex(5)

    def toggleTheme(self):
        # I know I know, this isn't pretty, just throwing some ideas around...
        if self.sender().text() == "Dark":
            self.setStyleSheet("QMainWindow {background: '#666';}")
        else:
            self.setStyleSheet("QMainWindow {background: '#FFF';}")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    umc = UMC()
    sys.exit(app.exec_())