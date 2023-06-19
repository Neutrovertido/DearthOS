# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/james/Projects/DearthOS/Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalcWindow(object):
    def setupUi(self, CalcWindow):
        CalcWindow.setObjectName("CalcWindow")
        CalcWindow.resize(330, 450)
        CalcWindow.setMinimumSize(QtCore.QSize(330, 450))
        CalcWindow.setMaximumSize(QtCore.QSize(330, 450))
        self.centralwidget = QtWidgets.QWidget(CalcWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(10, 10, 311, 87))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.output.setFont(font)
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(10, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b7.setFont(font)
        self.b7.setObjectName("b7")
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(90, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b8.setFont(font)
        self.b8.setObjectName("b8")
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(170, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b9.setFont(font)
        self.b9.setObjectName("b9")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(10, 190, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b4.setFont(font)
        self.b4.setObjectName("b4")
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(90, 190, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b5.setFont(font)
        self.b5.setObjectName("b5")
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(170, 190, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b6.setFont(font)
        self.b6.setObjectName("b6")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(10, 270, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(90, 270, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(170, 270, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.bDiv = QtWidgets.QPushButton(self.centralwidget)
        self.bDiv.setGeometry(QtCore.QRect(250, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bDiv.setFont(font)
        self.bDiv.setObjectName("bDiv")
        self.bMul = QtWidgets.QPushButton(self.centralwidget)
        self.bMul.setGeometry(QtCore.QRect(250, 190, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bMul.setFont(font)
        self.bMul.setObjectName("bMul")
        self.bRes = QtWidgets.QPushButton(self.centralwidget)
        self.bRes.setGeometry(QtCore.QRect(250, 270, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bRes.setFont(font)
        self.bRes.setObjectName("bRes")
        self.bSum = QtWidgets.QPushButton(self.centralwidget)
        self.bSum.setGeometry(QtCore.QRect(250, 350, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bSum.setFont(font)
        self.bSum.setObjectName("bSum")
        self.b0 = QtWidgets.QPushButton(self.centralwidget)
        self.b0.setGeometry(QtCore.QRect(10, 350, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b0.setFont(font)
        self.b0.setObjectName("b0")
        self.bIgu = QtWidgets.QPushButton(self.centralwidget)
        self.bIgu.setGeometry(QtCore.QRect(170, 350, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bIgu.setFont(font)
        self.bIgu.setStyleSheet("background-color: #e66100;")
        self.bIgu.setObjectName("bIgu")
        self.bBor = QtWidgets.QPushButton(self.centralwidget)
        self.bBor.setGeometry(QtCore.QRect(90, 350, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bBor.setFont(font)
        self.bBor.setObjectName("bBor")
        CalcWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CalcWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 34))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setGeometry(QtCore.QRect(500, 300, 156, 64))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuAbout.sizePolicy().hasHeightForWidth())
        self.menuAbout.setSizePolicy(sizePolicy)
        self.menuAbout.setObjectName("menuAbout")
        CalcWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CalcWindow)
        self.statusbar.setObjectName("statusbar")
        CalcWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(CalcWindow)
        QtCore.QMetaObject.connectSlotsByName(CalcWindow)

    def retranslateUi(self, CalcWindow):
        _translate = QtCore.QCoreApplication.translate
        CalcWindow.setWindowTitle(_translate("CalcWindow", "Calculator"))
        self.b7.setText(_translate("CalcWindow", "7"))
        self.b8.setText(_translate("CalcWindow", "8"))
        self.b9.setText(_translate("CalcWindow", "9"))
        self.b4.setText(_translate("CalcWindow", "4"))
        self.b5.setText(_translate("CalcWindow", "5"))
        self.b6.setText(_translate("CalcWindow", "6"))
        self.b1.setText(_translate("CalcWindow", "1"))
        self.b2.setText(_translate("CalcWindow", "2"))
        self.b3.setText(_translate("CalcWindow", "3"))
        self.bDiv.setText(_translate("CalcWindow", "/"))
        self.bMul.setText(_translate("CalcWindow", "X"))
        self.bRes.setText(_translate("CalcWindow", "-"))
        self.bSum.setText(_translate("CalcWindow", "+"))
        self.b0.setText(_translate("CalcWindow", "0"))
        self.bIgu.setText(_translate("CalcWindow", "="))
        self.bBor.setText(_translate("CalcWindow", "⌫"))
        self.menuAbout.setTitle(_translate("CalcWindow", "About"))
