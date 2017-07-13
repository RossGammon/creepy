# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pluginRatesCheckDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_checkPluginRatesDialog(object):
    def setupUi(self, checkPluginRatesDialog):
        checkPluginRatesDialog.setObjectName("checkPluginRatesDialog")
        checkPluginRatesDialog.resize(963, 300)
        self.checkPluginRatesButtonBox = QtWidgets.QDialogButtonBox(checkPluginRatesDialog)
        self.checkPluginRatesButtonBox.setGeometry(QtCore.QRect(600, 250, 341, 32))
        self.checkPluginRatesButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.checkPluginRatesButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.checkPluginRatesButtonBox.setObjectName("checkPluginRatesButtonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(checkPluginRatesDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 951, 231))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.checkPluginRatesHorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.checkPluginRatesHorizontalLayout.setObjectName("checkPluginRatesHorizontalLayout")
        self.checkPluginRatesLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.checkPluginRatesLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.checkPluginRatesLabel.setObjectName("checkPluginRatesLabel")
        self.checkPluginRatesHorizontalLayout.addWidget(self.checkPluginRatesLabel)

        self.retranslateUi(checkPluginRatesDialog)
        self.checkPluginRatesButtonBox.accepted.connect(checkPluginRatesDialog.accept)
        self.checkPluginRatesButtonBox.rejected.connect(checkPluginRatesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(checkPluginRatesDialog)

    def retranslateUi(self, checkPluginRatesDialog):
        _translate = QtCore.QCoreApplication.translate
        checkPluginRatesDialog.setWindowTitle(_translate("checkPluginRatesDialog", "Plugin API Rate Limit Information"))
        self.checkPluginRatesLabel.setText(_translate("checkPluginRatesDialog", "TextLabel"))

