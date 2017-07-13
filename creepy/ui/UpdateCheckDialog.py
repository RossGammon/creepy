# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateCheckDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UpdateCheckDialog(object):
    def setupUi(self, UpdateCheckDialog):
        UpdateCheckDialog.setObjectName("UpdateCheckDialog")
        UpdateCheckDialog.resize(473, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/creepy/creepy"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UpdateCheckDialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(UpdateCheckDialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(UpdateCheckDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.versionsTableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.versionsTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.versionsTableWidget.setTabKeyNavigation(False)
        self.versionsTableWidget.setProperty("showDropIndicator", False)
        self.versionsTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.versionsTableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.versionsTableWidget.setRowCount(1)
        self.versionsTableWidget.setColumnCount(5)
        self.versionsTableWidget.setObjectName("versionsTableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.versionsTableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.versionsTableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.versionsTableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.versionsTableWidget.setItem(0, 3, item)
        self.versionsTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.versionsTableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.versionsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.versionsTableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.versionsTableWidget)
        self.dlNewVersionLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dlNewVersionLabel.setText("")
        self.dlNewVersionLabel.setOpenExternalLinks(True)
        self.dlNewVersionLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.dlNewVersionLabel.setObjectName("dlNewVersionLabel")
        self.verticalLayout.addWidget(self.dlNewVersionLabel)

        self.retranslateUi(UpdateCheckDialog)
        self.buttonBox.accepted.connect(UpdateCheckDialog.accept)
        self.buttonBox.rejected.connect(UpdateCheckDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(UpdateCheckDialog)

    def retranslateUi(self, UpdateCheckDialog):
        _translate = QtCore.QCoreApplication.translate
        UpdateCheckDialog.setWindowTitle(_translate("UpdateCheckDialog", "Update Check"))
        self.label.setText(_translate("UpdateCheckDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Results of Update Check</span></p></body></html>"))
        __sortingEnabled = self.versionsTableWidget.isSortingEnabled()
        self.versionsTableWidget.setSortingEnabled(False)
        self.versionsTableWidget.setSortingEnabled(__sortingEnabled)

import creepy_resources_rc
