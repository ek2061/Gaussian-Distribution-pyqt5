# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gaussian_Distribution.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider.setMaximum(10000)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_3.addWidget(self.horizontalSlider)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider_2.setMaximum(1000)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout_3.addWidget(self.horizontalSlider_2)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider_3.setMaximum(1000)
        self.horizontalSlider_3.setProperty("value", 500)
        self.horizontalSlider_3.setSliderPosition(500)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setTickInterval(0)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.verticalLayout_3.addWidget(self.horizontalSlider_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(16)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(10000)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_4.addWidget(self.spinBox)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(16)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setMaximum(1000)
        self.spinBox_2.setProperty("value", 1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_4.addWidget(self.spinBox_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(16)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setMinimum(0.3)
        self.doubleSpinBox.setMaximum(0.8)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", 0.5)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout_4.addWidget(self.doubleSpinBox)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 30)
        self.verticalLayout_13.addLayout(self.verticalLayout_9)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalSlider_4 = QtWidgets.QSlider(self.groupBox_4)
        self.horizontalSlider_4.setMaximum(10000)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.verticalLayout_11.addWidget(self.horizontalSlider_4)
        self.horizontalSlider_5 = QtWidgets.QSlider(self.groupBox_4)
        self.horizontalSlider_5.setMaximum(1000)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.verticalLayout_11.addWidget(self.horizontalSlider_5)
        self.horizontalSlider_6 = QtWidgets.QSlider(self.groupBox_4)
        self.horizontalSlider_6.setMaximum(1000)
        self.horizontalSlider_6.setProperty("value", 500)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.verticalLayout_11.addWidget(self.horizontalSlider_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(16)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setMaximum(10000)
        self.spinBox_3.setProperty("value", 1)
        self.spinBox_3.setObjectName("spinBox_3")
        self.verticalLayout_12.addWidget(self.spinBox_3)
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(16)
        self.spinBox_4.setFont(font)
        self.spinBox_4.setMaximum(1000)
        self.spinBox_4.setProperty("value", 1)
        self.spinBox_4.setObjectName("spinBox_4")
        self.verticalLayout_12.addWidget(self.spinBox_4)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(16)
        self.doubleSpinBox_2.setFont(font)
        self.doubleSpinBox_2.setMinimum(0.3)
        self.doubleSpinBox_2.setMaximum(0.8)
        self.doubleSpinBox_2.setSingleStep(0.01)
        self.doubleSpinBox_2.setProperty("value", 0.5)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.verticalLayout_12.addWidget(self.doubleSpinBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 30)
        self.verticalLayout_14.addLayout(self.verticalLayout_10)
        self.horizontalLayout_4.addWidget(self.groupBox_4)
        self.verticalLayout_16.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 30)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_8.addWidget(self.groupBox_2)
        self.verticalLayout_16.addLayout(self.verticalLayout_8)
        self.verticalLayout_16.setStretch(0, 1)
        self.verticalLayout_16.setStretch(1, 5)
        self.verticalLayout_15.addLayout(self.verticalLayout_16)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 44))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Coin 1"))
        self.label.setText(_translate("MainWindow", "Rounds(N)"))
        self.label_2.setText(_translate("MainWindow", "Times(D)"))
        self.label_3.setText(_translate("MainWindow", "Threshold(θ)"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Coin 2"))
        self.label_4.setText(_translate("MainWindow", "Rounds(N)"))
        self.label_5.setText(_translate("MainWindow", "Times(D)"))
        self.label_6.setText(_translate("MainWindow", "Threshold(θ)"))
        self.pushButton.setText(_translate("MainWindow", "Random Parameter"))
        self.pushButton_2.setText(_translate("MainWindow", "Run and Plot"))
        self.groupBox_2.setTitle(_translate("MainWindow", "histogram image"))

