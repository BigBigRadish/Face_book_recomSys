# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Personal\Desktop\Face_book\CustomTitlebar\framelesswindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FramelessWindow(object):
    def setupUi(self, FramelessWindow):
        FramelessWindow.setObjectName("FramelessWindow")
        FramelessWindow.resize(560, 398)
        FramelessWindow.setWindowTitle("")
        FramelessWindow.setAutoFillBackground(False)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(FramelessWindow)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.windowFrame = QtWidgets.QWidget(FramelessWindow)
        self.windowFrame.setAutoFillBackground(False)
        self.windowFrame.setStyleSheet("#windowFrame{ border-radius:5px 5px 5px 5px;\n"
"\n"
"\n"
"}\n"
"")
        self.windowFrame.setObjectName("windowFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.windowFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windowTitlebar = WindowDragger(self.windowFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowTitlebar.sizePolicy().hasHeightForWidth())
        self.windowTitlebar.setSizePolicy(sizePolicy)
        self.windowTitlebar.setMinimumSize(QtCore.QSize(0, 0))
        self.windowTitlebar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.windowTitlebar.setAutoFillBackground(False)
        self.windowTitlebar.setStyleSheet("\n"
"\n"
"#windowTitlebar{\n"
"background-color: rgb(85, 170, 255);\n"
"border: 0px none palette(base);\n"
" border-top-left-radius:5px;\n"
" border-top-right-radius:5px;\n"
" background-color:palette(shadow); \n"
"height:20px;}")
        self.windowTitlebar.setObjectName("windowTitlebar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.windowTitlebar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titleText = QtWidgets.QLabel(self.windowTitlebar)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.titleText.setFont(font)
        self.titleText.setStyleSheet("  padding-left:5px;\n"
"background-color: rgb(85, 170, 255);")
        self.titleText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.titleText.setObjectName("titleText")
        self.horizontalLayout.addWidget(self.titleText)
        self.minimizeButton = QtWidgets.QToolButton(self.windowTitlebar)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.minimizeButton.setFont(font)
        self.minimizeButton.setStyleSheet("#minimizeButton{\n"
"background-color: rgb(85, 170, 255);\n"
"border-radius:0px;\n"
"  border:none;\n"
"  width:16px;\n"
"  height:16px;\n"
"  padding:4px;\n"
"    image: url(:/button_Ima/icon_window_minimize.png);\n"
"}\n"
"\n"
"#minimizeButton:pressed{\n"
"  background-color:palette(highlight);\n"
"}")
        self.minimizeButton.setText("")
        self.minimizeButton.setObjectName("minimizeButton")
        self.horizontalLayout.addWidget(self.minimizeButton)
        self.restoreButton = QtWidgets.QToolButton(self.windowTitlebar)
        self.restoreButton.setStyleSheet("#restoreButton{\n"
"background-color: rgb(85, 170, 255);\n"
"border-radius:0px;\n"
"  border:none;\n"
"  width:16px;\n"
"  height:16px;\n"
"  padding:4px;\n"
"    image: url(:/button_Ima/icon_window_restore.png);\n"
"}\n"
"\n"
"#restoreButton:pressed{\n"
"  background-color:palette(highlight);\n"
"}")
        self.restoreButton.setText("")
        self.restoreButton.setObjectName("restoreButton")
        self.horizontalLayout.addWidget(self.restoreButton)
        self.maximizeButton = QtWidgets.QToolButton(self.windowTitlebar)
        self.maximizeButton.setStyleSheet("#maximizeButton{\n"
"background-color: rgb(85, 170, 255);\n"
"border-radius:0px;\n"
"  border:none;\n"
"  width:16px;\n"
"  height:16px;\n"
"  padding:4px;\n"
"    image: url(:/button_Ima/icon_window_maximize.png);\n"
"}\n"
"\n"
"#maximizeButton:pressed{\n"
"  background-color:palette(highlight);\n"
"}")
        self.maximizeButton.setText("")
        self.maximizeButton.setObjectName("maximizeButton")
        self.horizontalLayout.addWidget(self.maximizeButton)
        self.closeButton = QtWidgets.QToolButton(self.windowTitlebar)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("#closeButton{\n"
"background-color: rgb(85, 170, 255);\n"
"border-radius:0px;\n"
"  border:none;\n"
"  width:16px;\n"
"  height:16px;\n"
"  padding:4px;\n"
"    image: url(:/button_Ima/icon_window_close.png);\n"
"  border-top-right-radius: 5px;\n"
"}\n"
"\n"
"#closeButton:pressed{\n"
"  background-color:palette(highlight);\n"
"}")
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addWidget(self.windowTitlebar)
        self.windowContent = QtWidgets.QWidget(self.windowFrame)
        self.windowContent.setAutoFillBackground(False)
        self.windowContent.setStyleSheet("#windowContent{\n"
"  border: 0px none palette(base);\n"
"  border-radius:0px 0px 50px 50px;\n"
"\n"
"}")
        self.windowContent.setObjectName("windowContent")
        self.verticalLayout.addWidget(self.windowContent)
        self.verticalLayout_2.addWidget(self.windowFrame)

        self.retranslateUi(FramelessWindow)
        QtCore.QMetaObject.connectSlotsByName(FramelessWindow)

    def retranslateUi(self, FramelessWindow):
        _translate = QtCore.QCoreApplication.translate
        self.titleText.setText(_translate("FramelessWindow", "铭 刻"))
        self.windowContent.setWhatsThis(_translate("FramelessWindow", "#windowContent{\n"
"  border: 0px none palette(base);\n"
"  border-radius:0px 0px 5px 5px;\n"
"}"))

from windowdragger import WindowDragger
try:
    import framelesswindow_rc
except:
    from . import framelesswindow_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FramelessWindow = QtWidgets.QWidget()
    ui = Ui_FramelessWindow()
    ui.setupUi(FramelessWindow)
    FramelessWindow.show()
    sys.exit(app.exec_())

