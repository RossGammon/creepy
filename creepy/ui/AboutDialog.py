# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/aboutDialog.ui'
#
# Created: Thu Jul 13 19:39:20 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(519, 729)
        aboutDialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/creepy/creepy"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutDialog.setWindowIcon(icon)
        aboutDialog.setModal(False)
        self.verticalLayoutWidget = QtWidgets.QWidget(aboutDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 478, 706))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(aboutDialog)
        self.buttonBox.accepted.connect(aboutDialog.accept)
        self.buttonBox.rejected.connect(aboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About"))
        self.label.setText(_translate("aboutDialog", "<html><head/><body><p align=\"center\"><img src=\":/creepy/creepy\"/></p><p><br/></p><p align=\"center\"><span style=\" font-size:9pt;\">Creepy is </span><span style=\" font-size:9pt; font-style:italic;\">the</span><span style=\" font-size:9pt;\"> geolocation OSINT tool. </span></p><p><br/></p><p><span style=\" font-weight:600;\">Version : </span>1.4 - Codename &quot;GIJC&quot;</p><p><span style=\" font-weight:600;\">Author</span> : Ioannis Kakavas &lt; jkakavas@gmail.com &gt;</p><p><span style=\" font-weight:600;\">Website</span>: www.geocreepy.com</p></body></html>"))

import creepy_resources_rc
