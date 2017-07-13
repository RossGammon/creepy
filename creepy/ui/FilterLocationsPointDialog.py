# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filterLocationsPointDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FilteLocationsPointDialog(object):
    def setupUi(self, FilteLocationsPointDialog):
        FilteLocationsPointDialog.setObjectName("FilteLocationsPointDialog")
        FilteLocationsPointDialog.resize(758, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/creepy/marker"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FilteLocationsPointDialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(FilteLocationsPointDialog)
        self.buttonBox.setGeometry(QtCore.QRect(390, 520, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(FilteLocationsPointDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 731, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.containerLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.containerLayout.setObjectName("containerLayout")
        self.titleLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setTextFormat(QtCore.Qt.RichText)
        self.titleLabel.setObjectName("titleLabel")
        self.containerLayout.addWidget(self.titleLabel)
        self.webView = QtWebKitWidgets.QWebView(self.verticalLayoutWidget)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.containerLayout.addWidget(self.webView)
        self.controlsContainerLayout = QtWidgets.QHBoxLayout()
        self.controlsContainerLayout.setObjectName("controlsContainerLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.controlsContainerLayout.addItem(spacerItem)
        self.radiusLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radiusLabel.sizePolicy().hasHeightForWidth())
        self.radiusLabel.setSizePolicy(sizePolicy)
        self.radiusLabel.setTextFormat(QtCore.Qt.RichText)
        self.radiusLabel.setObjectName("radiusLabel")
        self.controlsContainerLayout.addWidget(self.radiusLabel)
        self.radiusSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radiusSpinBox.sizePolicy().hasHeightForWidth())
        self.radiusSpinBox.setSizePolicy(sizePolicy)
        self.radiusSpinBox.setMaximum(1000)
        self.radiusSpinBox.setObjectName("radiusSpinBox")
        self.controlsContainerLayout.addWidget(self.radiusSpinBox)
        self.radiusUnitComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radiusUnitComboBox.sizePolicy().hasHeightForWidth())
        self.radiusUnitComboBox.setSizePolicy(sizePolicy)
        self.radiusUnitComboBox.setObjectName("radiusUnitComboBox")
        self.controlsContainerLayout.addWidget(self.radiusUnitComboBox)
        self.containerLayout.addLayout(self.controlsContainerLayout)

        self.retranslateUi(FilteLocationsPointDialog)
        self.buttonBox.accepted.connect(FilteLocationsPointDialog.accept)
        self.buttonBox.rejected.connect(FilteLocationsPointDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FilteLocationsPointDialog)

    def retranslateUi(self, FilteLocationsPointDialog):
        _translate = QtCore.QCoreApplication.translate
        FilteLocationsPointDialog.setWindowTitle(_translate("FilteLocationsPointDialog", "Filter Locations By Place"))
        self.titleLabel.setText(_translate("FilteLocationsPointDialog", "<html><head/><body><p><span style=\" font-size:9pt;\">Drop a </span><span style=\" font-size:9pt; font-weight:600; color:#ff0000;\">pin</span><span style=\" font-size:9pt;\"> on the map for your point of interest</span></p></body></html>"))
        self.radiusLabel.setText(_translate("FilteLocationsPointDialog", "<html><head/><body><p><span style=\" font-size:9pt;\">Distance from the POI :</span></p></body></html>"))

from PyQt5 import QtWebKitWidgets
import creepy_resources_rc
