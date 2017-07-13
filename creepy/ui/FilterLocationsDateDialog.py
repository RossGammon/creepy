# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filterLocationsDateDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FilterLocationsDateDialog(object):
    def setupUi(self, FilterLocationsDateDialog):
        FilterLocationsDateDialog.setObjectName("FilterLocationsDateDialog")
        FilterLocationsDateDialog.resize(928, 403)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/creepy/calendar"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FilterLocationsDateDialog.setWindowIcon(icon)
        FilterLocationsDateDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(FilterLocationsDateDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.containerLayout = QtWidgets.QVBoxLayout()
        self.containerLayout.setObjectName("containerLayout")
        self.titleLabel = QtWidgets.QLabel(FilterLocationsDateDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setObjectName("titleLabel")
        self.containerLayout.addWidget(self.titleLabel)
        self.calendarContainerLayout = QtWidgets.QHBoxLayout()
        self.calendarContainerLayout.setObjectName("calendarContainerLayout")
        self.startDateContainer = QtWidgets.QVBoxLayout()
        self.startDateContainer.setObjectName("startDateContainer")
        self.startDateLabel = QtWidgets.QLabel(FilterLocationsDateDialog)
        self.startDateLabel.setTextFormat(QtCore.Qt.AutoText)
        self.startDateLabel.setObjectName("startDateLabel")
        self.startDateContainer.addWidget(self.startDateLabel)
        self.stardateCalendarWidget = QtWidgets.QCalendarWidget(FilterLocationsDateDialog)
        self.stardateCalendarWidget.setObjectName("stardateCalendarWidget")
        self.startDateContainer.addWidget(self.stardateCalendarWidget)
        self.calendarContainerLayout.addLayout(self.startDateContainer)
        self.endDateContainer = QtWidgets.QVBoxLayout()
        self.endDateContainer.setObjectName("endDateContainer")
        self.endDateLabel = QtWidgets.QLabel(FilterLocationsDateDialog)
        self.endDateLabel.setObjectName("endDateLabel")
        self.endDateContainer.addWidget(self.endDateLabel)
        self.endDateCalendarWidget = QtWidgets.QCalendarWidget(FilterLocationsDateDialog)
        self.endDateCalendarWidget.setObjectName("endDateCalendarWidget")
        self.endDateContainer.addWidget(self.endDateCalendarWidget)
        self.calendarContainerLayout.addLayout(self.endDateContainer)
        self.containerLayout.addLayout(self.calendarContainerLayout)
        self.timeContainerLayout = QtWidgets.QHBoxLayout()
        self.timeContainerLayout.setObjectName("timeContainerLayout")
        self.startDateTimeEdit = QtWidgets.QTimeEdit(FilterLocationsDateDialog)
        self.startDateTimeEdit.setObjectName("startDateTimeEdit")
        self.timeContainerLayout.addWidget(self.startDateTimeEdit)
        self.endDateTimeEdit = QtWidgets.QTimeEdit(FilterLocationsDateDialog)
        self.endDateTimeEdit.setObjectName("endDateTimeEdit")
        self.timeContainerLayout.addWidget(self.endDateTimeEdit)
        self.containerLayout.addLayout(self.timeContainerLayout)
        self.verticalLayout.addLayout(self.containerLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(FilterLocationsDateDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(FilterLocationsDateDialog)
        self.buttonBox.accepted.connect(FilterLocationsDateDialog.accept)
        self.buttonBox.rejected.connect(FilterLocationsDateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FilterLocationsDateDialog)

    def retranslateUi(self, FilterLocationsDateDialog):
        _translate = QtCore.QCoreApplication.translate
        FilterLocationsDateDialog.setWindowTitle(_translate("FilterLocationsDateDialog", "Filter Locations By Date"))
        self.titleLabel.setText(_translate("FilterLocationsDateDialog", "<html><head/><body><p><span style=\" font-size:9pt;\">Select the start and end dates and times ( </span><span style=\" font-size:9pt; color:#ff0000;\">Note</span><span style=\" font-size:9pt;\"> that the selected dates are </span><span style=\" font-size:9pt; font-weight:600;\">UTC</span><span style=\" font-size:9pt;\"> ! )</span></p></body></html>"))
        self.startDateLabel.setText(_translate("FilterLocationsDateDialog", "<b>Start Date</b>"))
        self.endDateLabel.setText(_translate("FilterLocationsDateDialog", "<b>End Date</b>"))
        self.startDateTimeEdit.setDisplayFormat(_translate("FilterLocationsDateDialog", "hh:mm:ss AP"))

import creepy_resources_rc
