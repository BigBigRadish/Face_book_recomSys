from PyQt5 import  QtGui, QtWidgets, QtCore, QtWinExtras
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class WindowDragger(QWidget):
    doubleClicked = pyqtSignal()
    def __init__(self, parent):
        super(WindowDragger, self).__init__(parent)
        self.mousePressed = False;
        self.mousePos=QPoint()
        self.wndPos=QPoint()
        
    def mousePressEvent(self,event):
        self.mousePressed = True;
        self.mousePos = event.globalPos();
        
        parent = self.parentWidget();#QWidget *parent = parentWidget();
        if (parent):
            parent = parent.parentWidget();
            self.wndPos = parent.pos();
    def mouseMoveEvent(self,event):
        parent = self.parentWidget();
        if (parent):
            parent = parent.parentWidget();
        
        if (parent and self.mousePressed):
            parent.move(self.wndPos + (event.globalPos() -self.mousePos));
    def mouseReleaseEvent(self,event):
#        Q_UNUSED(event);
        self.mousePressed = False;
    def mouseDoubleClickEvent(self,event):
        self.doubleClicked.emit()
        
    def enterEvent(self, e):
        self.setCursor(Qt.ArrowCursor)
