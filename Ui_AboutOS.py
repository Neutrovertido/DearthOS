# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/james/Projects/DearthOS/AboutOS.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import platform, psutil
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SystemWindow(object):
    def setupUi(self, SystemWindow):
        SystemWindow.setObjectName("SystemWindow")
        SystemWindow.resize(500, 440)
        SystemWindow.setMinimumSize(QtCore.QSize(500, 440))
        SystemWindow.setMaximumSize(QtCore.QSize(500, 440))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main/img/computer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SystemWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SystemWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OSL = QtWidgets.QLabel(self.centralwidget)
        self.OSL.setGeometry(QtCore.QRect(10, 170, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.OSL.setFont(font)
        self.OSL.setObjectName("OSL")
        self.OS = QtWidgets.QLineEdit(self.centralwidget)
        self.OS.setEnabled(False)
        self.OS.setGeometry(QtCore.QRect(210, 160, 271, 36))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.OS.setFont(font)
        self.OS.setObjectName("OS")
        self.CPU = QtWidgets.QLineEdit(self.centralwidget)
        self.CPU.setEnabled(False)
        self.CPU.setGeometry(QtCore.QRect(210, 220, 271, 36))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CPU.setFont(font)
        self.CPU.setText("")
        self.CPU.setObjectName("CPU")
        self.CPUL = QtWidgets.QLabel(self.centralwidget)
        self.CPUL.setGeometry(QtCore.QRect(10, 230, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CPUL.setFont(font)
        self.CPUL.setObjectName("CPUL")
        self.RAM = QtWidgets.QLineEdit(self.centralwidget)
        self.RAM.setEnabled(False)
        self.RAM.setGeometry(QtCore.QRect(210, 280, 271, 36))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.RAM.setFont(font)
        self.RAM.setText("")
        self.RAM.setObjectName("RAM")
        self.RAML = QtWidgets.QLabel(self.centralwidget)
        self.RAML.setGeometry(QtCore.QRect(10, 290, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.RAML.setFont(font)
        self.RAML.setObjectName("RAML")
        self.hostL = QtWidgets.QLabel(self.centralwidget)
        self.hostL.setGeometry(QtCore.QRect(10, 350, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hostL.setFont(font)
        self.hostL.setObjectName("hostL")
        self.host = QtWidgets.QLineEdit(self.centralwidget)
        self.host.setEnabled(False)
        self.host.setGeometry(QtCore.QRect(210, 340, 271, 36))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.host.setFont(font)
        self.host.setText("")
        self.host.setObjectName("host")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(150, 0, 181, 151))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/Main/img/dearth-logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        SystemWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SystemWindow)
        self.statusbar.setObjectName("statusbar")
        SystemWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(SystemWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 34))
        self.menubar.setObjectName("menubar")
        SystemWindow.setMenuBar(self.menubar)

        # Modified
        self.CPU.setText(platform.processor())
        self.RAM.setText(str(psutil.virtual_memory().total/1000000000) + " GB")
        self.host.setText(platform.system())

        self.retranslateUi(SystemWindow)
        QtCore.QMetaObject.connectSlotsByName(SystemWindow)

    def retranslateUi(self, SystemWindow):
        _translate = QtCore.QCoreApplication.translate
        SystemWindow.setWindowTitle(_translate("SystemWindow", "System Information"))
        self.OSL.setText(_translate("SystemWindow", "Operative System:"))
        self.OS.setText(_translate("SystemWindow", "Dearth OS v0.4"))
        self.CPUL.setText(_translate("SystemWindow", "CPU:"))
        self.RAML.setText(_translate("SystemWindow", "RAM:"))
        self.hostL.setText(_translate("SystemWindow", "Host OS:"))
import Resources_rc
