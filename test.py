import sys
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, 
    QDesktopWidget, QMainWindow, QAction, qApp, QMenu, QTextEdit, QFrame, QColorDialog,
    QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QInputDialog, QFileDialog)
from PyQt5.QtGui import QFont,QIcon,QColor 

class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        #
        # EVENT STUFF
        #
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        #
        # APPLICATION BODY STUFF
        #
        '''btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(70, 70)       
        
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 100)       

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit) #this overrides my buttons! Damnit!'''
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 75)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 75)
      
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)

        #
        # MENU BAR STUFF
        #
        exitAct = QAction(QIcon('img/exit.png'), '&Exit', self)        
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        miningAct = QAction(QIcon('img/exit.png'), '&Mine Stuff!', self)        
        miningAct.setShortcut('Ctrl+M')
        miningAct.setStatusTip('Do something, I guess')
        miningAct.triggered.connect(qApp.quit)

        openFile = QAction(QIcon('img/exit.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showFileDialog)

        menubar = self.menuBar()
        
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        fileMenu.addAction(openFile)
        miningMenu = menubar.addMenu('&Mining')
        miningMenu.addAction(miningAct)

        subbyMenu = menubar.addMenu('&Submenu')
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self) 
        impMenu.addAction(impAct)
        newAct = QAction('New', self)        
        subbyMenu.addAction(newAct)
        subbyMenu.addMenu(impMenu)

        viewMenu = menubar.addMenu('View')
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewStatAct)

        #
        # TOOLBAR STUFF
        #
        exitAct = QAction(QIcon('img/radioactive.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)
        
        #
        # DIALOG
        #
        self.btn = QPushButton('Popup Text', self)
        self.btn.move(20, 120)
        self.btn.clicked.connect(self.showDialog)
        
        self.le = QLineEdit(self)
        self.le.move(130, 120)

        col = QColor(0, 0, 0) 

        self.btnCol = QPushButton('Popup Color', self)
        self.btnCol.move(20, 200)

        self.btnCol.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(120, 200, 100, 100)

        #
        # MAIN WINDOW STUFF
        #
        self.setWindowTitle('Univeral Mining Control')
        self.setWindowIcon(QIcon('icon.png'))         
        self.resize(1000, 520)
        self.center()
        self.show()

    def buttonClicked(self):
      
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',"Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        
        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        
        if action == quitAct:
            qApp.quit()

    def keyPressEvent(self, e): 
        if e.key() == Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, event):
        print("You clicked the app! WOW!")
        #this will close the app on mouseclick... not too useful :/
        #self.c.closeApp.emit()
        
    def showDialog(self):
        print("I made it this far...")
        if self.sender().text() == "Popup Color":
            
            col = QColorDialog.getColor()

            if col.isValid():
                self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        else:
            text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
            if ok:
                self.le.setText(str(text))

    def showFileDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                # ERROR, TEXT EDIT NOT DEFINED! LOL!
                self.textEdit.setText(data)
    
    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())