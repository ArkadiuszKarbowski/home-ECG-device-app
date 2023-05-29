# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ekg_app_front.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EKGApp(object):
    def setupUi(self, EKGApp):
        EKGApp.setObjectName("EKGApp")
        EKGApp.resize(1039, 642)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EKGApp.sizePolicy().hasHeightForWidth())
        EKGApp.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(EKGApp)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1001, 611))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("border-radius:40px;\n"
"border-image: url(static/background_logo.png);\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(90, 20, 846, 562))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 348, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(186, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 308, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)
        self.Signal_bckgrnd = QtWidgets.QWidget(self.widget)
        self.Signal_bckgrnd.setMinimumSize(QtCore.QSize(790, 330))
        self.Signal_bckgrnd.setBaseSize(QtCore.QSize(3, 1))
        self.Signal_bckgrnd.setStyleSheet("border-image: none;\n"
"background-color: rgb(0, 58, 173, 0);\n"
"border-radius:40px;")
        self.Signal_bckgrnd.setObjectName("Signal_bckgrnd")
        self.gridLayout.addWidget(self.Signal_bckgrnd, 3, 1, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(186, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(400, 0))
        self.label.setMaximumSize(QtCore.QSize(400, 100))
        self.label.setBaseSize(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("border-image: none;\n"
"background-color: rgba(255, 255, 255, 220);\n"
"color: rgb(0, 76, 255);\n"
"border-radius:15px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(818, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 4, 1, 1, 3)
        EKGApp.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EKGApp)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        EKGApp.setStatusBar(self.statusbar)

        self.retranslateUi(EKGApp)
        QtCore.QMetaObject.connectSlotsByName(EKGApp)

    def retranslateUi(self, EKGApp):
        _translate = QtCore.QCoreApplication.translate
        EKGApp.setWindowTitle(_translate("EKGApp", "EKG App"))
        self.label.setText(_translate("EKGApp", "EKG Signal:"))



