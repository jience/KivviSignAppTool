# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_signapp.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(551, 492)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_apkPath = QtWidgets.QLabel(Form)
        self.label_apkPath.setObjectName("label_apkPath")
        self.gridLayout.addWidget(self.label_apkPath, 0, 0, 1, 1)
        self.lineEdit_apkPath = QtWidgets.QLineEdit(Form)
        self.lineEdit_apkPath.setObjectName("lineEdit_apkPath")
        self.gridLayout.addWidget(self.lineEdit_apkPath, 0, 1, 1, 2)
        self.pushButton_apkPath = QtWidgets.QPushButton(Form)
        self.pushButton_apkPath.setObjectName("pushButton_apkPath")
        self.gridLayout.addWidget(self.pushButton_apkPath, 0, 3, 1, 1)
        self.label_certPath = QtWidgets.QLabel(Form)
        self.label_certPath.setObjectName("label_certPath")
        self.gridLayout.addWidget(self.label_certPath, 1, 0, 1, 1)
        self.lineEdit_certPath = QtWidgets.QLineEdit(Form)
        self.lineEdit_certPath.setObjectName("lineEdit_certPath")
        self.gridLayout.addWidget(self.lineEdit_certPath, 1, 1, 1, 2)
        self.pushButton_certPath = QtWidgets.QPushButton(Form)
        self.pushButton_certPath.setObjectName("pushButton_certPath")
        self.gridLayout.addWidget(self.pushButton_certPath, 1, 3, 1, 1)
        self.label_keyPath = QtWidgets.QLabel(Form)
        self.label_keyPath.setObjectName("label_keyPath")
        self.gridLayout.addWidget(self.label_keyPath, 2, 0, 1, 1)
        self.lineEdit_keyPath = QtWidgets.QLineEdit(Form)
        self.lineEdit_keyPath.setObjectName("lineEdit_keyPath")
        self.gridLayout.addWidget(self.lineEdit_keyPath, 2, 1, 1, 2)
        self.pushButton_keyPath = QtWidgets.QPushButton(Form)
        self.pushButton_keyPath.setObjectName("pushButton_keyPath")
        self.gridLayout.addWidget(self.pushButton_keyPath, 2, 3, 1, 1)
        self.label_signedApkPath = QtWidgets.QLabel(Form)
        self.label_signedApkPath.setObjectName("label_signedApkPath")
        self.gridLayout.addWidget(self.label_signedApkPath, 3, 0, 1, 2)
        self.lineEdit_signedApkPath = QtWidgets.QLineEdit(Form)
        self.lineEdit_signedApkPath.setObjectName("lineEdit_signedApkPath")
        self.gridLayout.addWidget(self.lineEdit_signedApkPath, 3, 2, 1, 1)
        self.pushButton_signedApkPath = QtWidgets.QPushButton(Form)
        self.pushButton_signedApkPath.setObjectName("pushButton_signedApkPath")
        self.gridLayout.addWidget(self.pushButton_signedApkPath, 3, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_cleanLog = QtWidgets.QPushButton(Form)
        self.pushButton_cleanLog.setObjectName("pushButton_cleanLog")
        self.horizontalLayout.addWidget(self.pushButton_cleanLog)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_sign = QtWidgets.QPushButton(Form)
        self.pushButton_sign.setObjectName("pushButton_sign")
        self.horizontalLayout.addWidget(self.pushButton_sign)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox_log = QtWidgets.QGroupBox(Form)
        self.groupBox_log.setObjectName("groupBox_log")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_log)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_log = QtWidgets.QTextBrowser(self.groupBox_log)
        self.textBrowser_log.setObjectName("textBrowser_log")
        self.verticalLayout.addWidget(self.textBrowser_log)
        self.verticalLayout_2.addWidget(self.groupBox_log)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_apkPath.setText(_translate("Form", "Apk Path:"))
        self.pushButton_apkPath.setText(_translate("Form", "..."))
        self.label_certPath.setText(_translate("Form", "Cert Path:"))
        self.pushButton_certPath.setText(_translate("Form", "..."))
        self.label_keyPath.setText(_translate("Form", "Key Path:"))
        self.pushButton_keyPath.setText(_translate("Form", "..."))
        self.label_signedApkPath.setText(_translate("Form", "Signed Apk Path:"))
        self.pushButton_signedApkPath.setText(_translate("Form", "..."))
        self.pushButton_cleanLog.setText(_translate("Form", "Clean"))
        self.pushButton_sign.setText(_translate("Form", "Sign"))
        self.groupBox_log.setTitle(_translate("Form", "Log"))

