# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filterLocationsCustomDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FilterLocationsCustomDialog(object):
    def setupUi(self, FilterLocationsCustomDialog):
        FilterLocationsCustomDialog.setObjectName("FilterLocationsCustomDialog")
        FilterLocationsCustomDialog.resize(1202, 403)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/creepy/calendar-day.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FilterLocationsCustomDialog.setWindowIcon(icon)
        FilterLocationsCustomDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(FilterLocationsCustomDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.containerLayout = QtWidgets.QVBoxLayout()
        self.containerLayout.setObjectName("containerLayout")
        self.titleLabel = QtWidgets.QLabel(FilterLocationsCustomDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setObjectName("titleLabel")
        self.containerLayout.addWidget(self.titleLabel)
        self.fieldsContainerLayout = QtWidgets.QHBoxLayout()
        self.fieldsContainerLayout.setObjectName("fieldsContainerLayout")
        self.hoursOfDayContainer = QtWidgets.QVBoxLayout()
        self.hoursOfDayContainer.setObjectName("hoursOfDayContainer")
        self.hoursOfDayLabel = QtWidgets.QLabel(FilterLocationsCustomDialog)
        self.hoursOfDayLabel.setObjectName("hoursOfDayLabel")
        self.hoursOfDayContainer.addWidget(self.hoursOfDayLabel)
        self.hoursOfDayListWidget = QtWidgets.QListWidget(FilterLocationsCustomDialog)
        self.hoursOfDayListWidget.setObjectName("hoursOfDayListWidget")
        self.hoursOfDayContainer.addWidget(self.hoursOfDayListWidget)
        self.fieldsContainerLayout.addLayout(self.hoursOfDayContainer)
        self.daysOfWeekContainer = QtWidgets.QVBoxLayout()
        self.daysOfWeekContainer.setObjectName("daysOfWeekContainer")
        self.daysOfWeekLayout = QtWidgets.QVBoxLayout()
        self.daysOfWeekLayout.setObjectName("daysOfWeekLayout")
        self.daysOfWeekLabel = QtWidgets.QLabel(FilterLocationsCustomDialog)
        self.daysOfWeekLabel.setObjectName("daysOfWeekLabel")
        self.daysOfWeekLayout.addWidget(self.daysOfWeekLabel)
        self.daysOfWeekListWidget = QtWidgets.QListWidget(FilterLocationsCustomDialog)
        self.daysOfWeekListWidget.setObjectName("daysOfWeekListWidget")
        self.daysOfWeekLayout.addWidget(self.daysOfWeekListWidget)
        self.daysOfWeekContainer.addLayout(self.daysOfWeekLayout)
        self.fieldsContainerLayout.addLayout(self.daysOfWeekContainer)
        self.monthsOfYearContainer = QtWidgets.QVBoxLayout()
        self.monthsOfYearContainer.setObjectName("monthsOfYearContainer")
        self.monthsOfYearLayout = QtWidgets.QVBoxLayout()
        self.monthsOfYearLayout.setObjectName("monthsOfYearLayout")
        self.monthsOfYearLabel = QtWidgets.QLabel(FilterLocationsCustomDialog)
        self.monthsOfYearLabel.setTextFormat(QtCore.Qt.AutoText)
        self.monthsOfYearLabel.setObjectName("monthsOfYearLabel")
        self.monthsOfYearLayout.addWidget(self.monthsOfYearLabel)
        self.monthsOfYearListWidget = QtWidgets.QListWidget(FilterLocationsCustomDialog)
        self.monthsOfYearListWidget.setObjectName("monthsOfYearListWidget")
        self.monthsOfYearLayout.addWidget(self.monthsOfYearListWidget)
        self.monthsOfYearContainer.addLayout(self.monthsOfYearLayout)
        self.fieldsContainerLayout.addLayout(self.monthsOfYearContainer)
        self.containerLayout.addLayout(self.fieldsContainerLayout)
        self.verticalLayout.addLayout(self.containerLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(FilterLocationsCustomDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(FilterLocationsCustomDialog)
        self.buttonBox.accepted.connect(FilterLocationsCustomDialog.accept)
        self.buttonBox.rejected.connect(FilterLocationsCustomDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FilterLocationsCustomDialog)

    def retranslateUi(self, FilterLocationsCustomDialog):
        _translate = QtCore.QCoreApplication.translate
        FilterLocationsCustomDialog.setWindowTitle(_translate("FilterLocationsCustomDialog", "Filter Locations By Date"))
        self.titleLabel.setText(_translate("FilterLocationsCustomDialog", "<html><head/><body><p><span style=\" font-size:9pt;\">Select the custom filtering options</span></p></body></html>"))
        self.hoursOfDayLabel.setText(_translate("FilterLocationsCustomDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Hours in the day</span></p></body></html>"))
        self.daysOfWeekLabel.setText(_translate("FilterLocationsCustomDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Days of the week</span></p></body></html>"))
        self.monthsOfYearLabel.setText(_translate("FilterLocationsCustomDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Months of the year</span></p></body></html>"))

import creepy_resources_rc
