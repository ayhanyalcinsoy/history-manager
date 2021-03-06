# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiitem.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HistoryItemWidget(object):
    def setupUi(self, HistoryItemWidget):
        HistoryItemWidget.setObjectName("HistoryItemWidget")
        HistoryItemWidget.resize(661, 48)
        HistoryItemWidget.setMinimumSize(QtCore.QSize(0, 48))
        HistoryItemWidget.setWindowTitle("Form")
        self.gridLayout_3 = QtWidgets.QGridLayout(HistoryItemWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.iconLabel = QtWidgets.QLabel(HistoryItemWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
        self.iconLabel.setSizePolicy(sizePolicy)
        self.iconLabel.resize(QtCore.QSize(24, 24))
        self.iconLabel.setPixmap(QtGui.QIcon.fromTheme("process-stop").pixmap(24, 24))
        self.iconLabel.setObjectName("iconLabel")
        self.gridLayout_2.addWidget(self.iconLabel, 0, 0, 2, 1)
        self.labelLabel = QtWidgets.QLabel(HistoryItemWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLabel.setFont(font)
        self.labelLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.labelLabel.setObjectName("labelLabel")
        self.gridLayout_2.addWidget(self.labelLabel, 0, 1, 1, 1)
        self.typeLabel = QtWidgets.QLabel(HistoryItemWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeLabel.sizePolicy().hasHeightForWidth())
        self.typeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.typeLabel.setFont(font)
        self.typeLabel.setStyleSheet("color:gray;")
        self.typeLabel.setObjectName("typeLabel")
        self.gridLayout_2.addWidget(self.typeLabel, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.restorePB = QtWidgets.QPushButton(HistoryItemWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restorePB.sizePolicy().hasHeightForWidth())
        self.restorePB.setSizePolicy(sizePolicy)
        self.restorePB.setText("")
        icon = QtGui.QIcon.fromTheme("view-calendar")
        self.restorePB.setIcon(icon)
        self.restorePB.setObjectName("restorePB")
        self.gridLayout.addWidget(self.restorePB, 0, 2, 1, 1)
        self.detailsPB = QtWidgets.QPushButton(HistoryItemWidget)
        self.detailsPB.setText("")
        icon1 = QtGui.QIcon.fromTheme("edit-find")
        self.detailsPB.setIcon(icon1)
        self.detailsPB.setObjectName("detailsPB")
        self.gridLayout.addWidget(self.detailsPB, 0, 0, 1, 1)
        self.planPB = QtWidgets.QPushButton(HistoryItemWidget)
        self.planPB.setText("")
        icon2 = QtGui.QIcon.fromTheme("resource-calendar-insert")
        self.planPB.setIcon(icon2)
        self.planPB.setObjectName("planPB")
        self.gridLayout.addWidget(self.planPB, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 2, 1, 1)

        self.retranslateUi(HistoryItemWidget)
        QtCore.QMetaObject.connectSlotsByName(HistoryItemWidget)

    def retranslateUi(self, HistoryItemWidget):
        _translate = QtCore.QCoreApplication.translate
        self.labelLabel.setText(_translate("HistoryItemWidget", "History Date - Time /Label"))
        self.typeLabel.setText(_translate("HistoryItemWidget", "No: Type:"))
        self.restorePB.setToolTip(_translate("HistoryItemWidget", "Take back to this point"))
        self.detailsPB.setToolTip(_translate("HistoryItemWidget", "Details"))
        self.planPB.setToolTip(_translate("HistoryItemWidget", "Show operation plan"))

