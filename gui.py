# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(546, 445)
        MainWindow.setMinimumSize(QtCore.QSize(546, 445))
        MainWindow.setMaximumSize(QtCore.QSize(546, 445))
        MainWindow.setStyleSheet(_fromUtf8(""))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(546, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(547, 16777215))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ser_box = QtGui.QLineEdit(self.centralwidget)
        self.ser_box.setGeometry(QtCore.QRect(80, 40, 121, 31))
        self.ser_box.setObjectName(_fromUtf8("ser_box"))
        self.download_btn = QtGui.QPushButton(self.centralwidget)
        self.download_btn.setEnabled(False)
        self.download_btn.setGeometry(QtCore.QRect(150, 170, 75, 23))
        self.download_btn.setObjectName(_fromUtf8("download_btn"))
        self.info_label = QtGui.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(10, 230, 221, 16))
        self.info_label.setText(_fromUtf8(""))
        self.info_label.setObjectName(_fromUtf8("info_label"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(240, 10, 3, 369))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(250, 10, 291, 371))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        spacerItem = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.webView = QtWebKit.QWebView(self.layoutWidget)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.horizontalLayout_12.addWidget(self.webView)
        spacerItem1 = QtGui.QSpacerItem(17, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 59, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
        self.sea_box = QtGui.QSpinBox(self.centralwidget)
        self.sea_box.setEnabled(False)
        self.sea_box.setGeometry(QtCore.QRect(80, 90, 33, 31))
        self.sea_box.setMinimum(1)
        self.sea_box.setProperty("value", 1)
        self.sea_box.setObjectName(_fromUtf8("sea_box"))
        self.epis_box = QtGui.QSpinBox(self.centralwidget)
        self.epis_box.setEnabled(False)
        self.epis_box.setGeometry(QtCore.QRect(80, 130, 33, 31))
        self.epis_box.setMinimum(1)
        self.epis_box.setProperty("value", 1)
        self.epis_box.setObjectName(_fromUtf8("epis_box"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(10, 124, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 59, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.valid_btn = QtGui.QPushButton(self.centralwidget)
        self.valid_btn.setGeometry(QtCore.QRect(60, 170, 75, 23))
        self.valid_btn.setObjectName(_fromUtf8("valid_btn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMain = QtGui.QMenu(self.menubar)
        self.menuMain.setObjectName(_fromUtf8("menuMain"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Teenoh", None))
        self.ser_box.setPlaceholderText(_translate("MainWindow", "Series", None))
        self.download_btn.setText(_translate("MainWindow", "Download", None))
        self.label.setText(_translate("MainWindow", "Series Name", None))
        self.label_3.setText(_translate("MainWindow", "Episode", None))
        self.label_2.setText(_translate("MainWindow", "Season", None))
        self.valid_btn.setText(_translate("MainWindow", "Validate", None))
        self.menuMain.setTitle(_translate("MainWindow", "Main", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))

from PyQt4 import QtWebKit
