# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verifyDeleteDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_verifyDeleteDialog(object):
    def setupUi(self, verifyDeleteDialog):
        verifyDeleteDialog.setObjectName("verifyDeleteDialog")
        verifyDeleteDialog.setWindowModality(QtCore.Qt.NonModal)
        verifyDeleteDialog.resize(407, 216)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/creepy/cross-circle"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        verifyDeleteDialog.setWindowIcon(icon)
        verifyDeleteDialog.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(verifyDeleteDialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 170, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(verifyDeleteDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 20, 321, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(verifyDeleteDialog)
        self.buttonBox.accepted.connect(verifyDeleteDialog.accept)
        self.buttonBox.rejected.connect(verifyDeleteDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(verifyDeleteDialog)

    def retranslateUi(self, verifyDeleteDialog):
        _translate = QtCore.QCoreApplication.translate
        verifyDeleteDialog.setWindowTitle(_translate("verifyDeleteDialog", "Delete Project"))
        self.label.setText(_translate("verifyDeleteDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Are you sure you want to </span><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">delete</span><span style=\" font-size:10pt;\"> project </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">@project@</span><span style=\" font-size:10pt;\"> ? </span></p></body></html>"))

import creepy_resources_rc
