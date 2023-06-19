# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/james/Projects/DearthOS/Notepad.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NoteWindow(object):
    def setupUi(self, NoteWindow):
        NoteWindow.setObjectName("NoteWindow")
        NoteWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(NoteWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
        NoteWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NoteWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 34))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        NoteWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NoteWindow)
        self.statusbar.setObjectName("statusbar")
        NoteWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(NoteWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_As = QtWidgets.QAction(NoteWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QtWidgets.QAction(NoteWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(NoteWindow)
        QtCore.QMetaObject.connectSlotsByName(NoteWindow)

    def retranslateUi(self, NoteWindow):
        _translate = QtCore.QCoreApplication.translate
        NoteWindow.setWindowTitle(_translate("NoteWindow", "Notepad"))
        self.menuFile.setTitle(_translate("NoteWindow", "File"))
        self.menuAbout.setTitle(_translate("NoteWindow", "About"))
        self.actionOpen.setText(_translate("NoteWindow", "Open"))
        self.actionSave_As.setText(_translate("NoteWindow", "Save As"))
        self.actionExit.setText(_translate("NoteWindow", "Exit"))