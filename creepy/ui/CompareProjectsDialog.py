# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compareProjectsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_compareProjectsDialog(object):
    def setupUi(self, compareProjectsDialog):
        compareProjectsDialog.setObjectName("compareProjectsDialog")
        compareProjectsDialog.resize(928, 403)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/creepy/calendar"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        compareProjectsDialog.setWindowIcon(icon)
        compareProjectsDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(compareProjectsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.containerLayout = QtWidgets.QVBoxLayout()
        self.containerLayout.setObjectName("containerLayout")
        self.titleLabel = QtWidgets.QLabel(compareProjectsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setObjectName("titleLabel")
        self.containerLayout.addWidget(self.titleLabel)
        self.projectsSelectionContainerLayout = QtWidgets.QHBoxLayout()
        self.projectsSelectionContainerLayout.setObjectName("projectsSelectionContainerLayout")
        self.firstProjectContainer = QtWidgets.QVBoxLayout()
        self.firstProjectContainer.setObjectName("firstProjectContainer")
        self.firstProjectLabel = QtWidgets.QLabel(compareProjectsDialog)
        self.firstProjectLabel.setTextFormat(QtCore.Qt.AutoText)
        self.firstProjectLabel.setObjectName("firstProjectLabel")
        self.firstProjectContainer.addWidget(self.firstProjectLabel)
        self.firstProjectListWidget = QtWidgets.QListWidget(compareProjectsDialog)
        self.firstProjectListWidget.setObjectName("firstProjectListWidget")
        self.firstProjectContainer.addWidget(self.firstProjectListWidget)
        self.projectsSelectionContainerLayout.addLayout(self.firstProjectContainer)
        self.secondProjectContainer = QtWidgets.QVBoxLayout()
        self.secondProjectContainer.setObjectName("secondProjectContainer")
        self.secondProjectLabel = QtWidgets.QLabel(compareProjectsDialog)
        self.secondProjectLabel.setObjectName("secondProjectLabel")
        self.secondProjectContainer.addWidget(self.secondProjectLabel)
        self.secondProjectListWidget = QtWidgets.QListWidget(compareProjectsDialog)
        self.secondProjectListWidget.setObjectName("secondProjectListWidget")
        self.secondProjectContainer.addWidget(self.secondProjectListWidget)
        self.projectsSelectionContainerLayout.addLayout(self.secondProjectContainer)
        self.containerLayout.addLayout(self.projectsSelectionContainerLayout)
        self.verticalLayout.addLayout(self.containerLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(compareProjectsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(compareProjectsDialog)
        self.buttonBox.accepted.connect(compareProjectsDialog.accept)
        self.buttonBox.rejected.connect(compareProjectsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(compareProjectsDialog)

    def retranslateUi(self, compareProjectsDialog):
        _translate = QtCore.QCoreApplication.translate
        compareProjectsDialog.setWindowTitle(_translate("compareProjectsDialog", "Compare Projects"))
        self.titleLabel.setText(_translate("compareProjectsDialog", "<html><head/><body><p><span style=\" font-size:9pt;\">Select the two projects you want to compare</span></p></body></html>"))
        self.firstProjectLabel.setText(_translate("compareProjectsDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Project A</span></p></body></html>"))
        self.secondProjectLabel.setText(_translate("compareProjectsDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Project B</span></p></body></html>"))

import creepy_resources_rc
