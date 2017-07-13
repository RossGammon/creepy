# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pluginsConfig.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PluginsConfigurationDialog(object):
    def setupUi(self, PluginsConfigurationDialog):
        PluginsConfigurationDialog.setObjectName("PluginsConfigurationDialog")
        PluginsConfigurationDialog.resize(810, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PluginsConfigurationDialog.sizePolicy().hasHeightForWidth())
        PluginsConfigurationDialog.setSizePolicy(sizePolicy)
        PluginsConfigurationDialog.setMinimumSize(QtCore.QSize(810, 640))
        PluginsConfigurationDialog.setMaximumSize(QtCore.QSize(810, 640))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/creepy/properties"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PluginsConfigurationDialog.setWindowIcon(icon)
        self.BtnBox = QtWidgets.QDialogButtonBox(PluginsConfigurationDialog)
        self.BtnBox.setGeometry(QtCore.QRect(430, 600, 341, 32))
        self.BtnBox.setOrientation(QtCore.Qt.Horizontal)
        self.BtnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.BtnBox.setObjectName("BtnBox")
        self.PluginsList = QtWidgets.QListView(PluginsConfigurationDialog)
        self.PluginsList.setGeometry(QtCore.QRect(10, 10, 211, 581))
        self.PluginsList.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.PluginsList.setObjectName("PluginsList")

        self.retranslateUi(PluginsConfigurationDialog)
        self.BtnBox.accepted.connect(PluginsConfigurationDialog.accept)
        self.BtnBox.rejected.connect(PluginsConfigurationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PluginsConfigurationDialog)

    def retranslateUi(self, PluginsConfigurationDialog):
        _translate = QtCore.QCoreApplication.translate
        PluginsConfigurationDialog.setWindowTitle(_translate("PluginsConfigurationDialog", "Plugins Configuration"))

import creepy_resources_rc
