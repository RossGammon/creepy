# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pluginConfigCheckDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_checkPluginConfigurationDialog(object):
    def setupUi(self, checkPluginConfigurationDialog):
        checkPluginConfigurationDialog.setObjectName("checkPluginConfigurationDialog")
        checkPluginConfigurationDialog.resize(378, 222)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(checkPluginConfigurationDialog.sizePolicy().hasHeightForWidth())
        checkPluginConfigurationDialog.setSizePolicy(sizePolicy)
        checkPluginConfigurationDialog.setMinimumSize(QtCore.QSize(378, 222))
        checkPluginConfigurationDialog.setMaximumSize(QtCore.QSize(378, 222))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/creepy/creepy"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        checkPluginConfigurationDialog.setWindowIcon(icon)
        checkPluginConfigurationDialog.setModal(True)
        self.checkPluginConfigurationButtonBox = QtWidgets.QDialogButtonBox(checkPluginConfigurationDialog)
        self.checkPluginConfigurationButtonBox.setGeometry(QtCore.QRect(30, 176, 341, 32))
        self.checkPluginConfigurationButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.checkPluginConfigurationButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.checkPluginConfigurationButtonBox.setObjectName("checkPluginConfigurationButtonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(checkPluginConfigurationDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 351, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.checkPluginConfigurationHorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.checkPluginConfigurationHorizontalLayout.setObjectName("checkPluginConfigurationHorizontalLayout")
        self.checkPluginConfigurationResultLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.checkPluginConfigurationResultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.checkPluginConfigurationResultLabel.setWordWrap(True)
        self.checkPluginConfigurationResultLabel.setObjectName("checkPluginConfigurationResultLabel")
        self.checkPluginConfigurationHorizontalLayout.addWidget(self.checkPluginConfigurationResultLabel)

        self.retranslateUi(checkPluginConfigurationDialog)
        self.checkPluginConfigurationButtonBox.accepted.connect(checkPluginConfigurationDialog.accept)
        self.checkPluginConfigurationButtonBox.rejected.connect(checkPluginConfigurationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(checkPluginConfigurationDialog)

    def retranslateUi(self, checkPluginConfigurationDialog):
        _translate = QtCore.QCoreApplication.translate
        checkPluginConfigurationDialog.setWindowTitle(_translate("checkPluginConfigurationDialog", "Plugin Configuration Test"))
        self.checkPluginConfigurationResultLabel.setText(_translate("checkPluginConfigurationDialog", "TextLabel"))

import creepy_resources_rc
