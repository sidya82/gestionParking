# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creationParking.ui'
#
# Created: Mon Jan  5 16:57:56 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CreaParking(object):
    def setupUi(self, CreaParking):
        CreaParking.setObjectName(_fromUtf8("CreaParking"))
        CreaParking.resize(400, 300)
        self.layoutWidget = QtGui.QWidget(CreaParking)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 270, 201, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btn_annuler = QtGui.QPushButton(self.layoutWidget)
        self.btn_annuler.setObjectName(_fromUtf8("btn_annuler"))
        self.horizontalLayout_2.addWidget(self.btn_annuler)
        self.btn_valider = QtGui.QPushButton(self.layoutWidget)
        self.btn_valider.setObjectName(_fromUtf8("btn_valider"))
        self.horizontalLayout_2.addWidget(self.btn_valider)
        self.layoutWidget1 = QtGui.QWidget(CreaParking)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 230, 275, 25))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.nbPlacesTotal = QtGui.QLabel(self.layoutWidget1)
        self.nbPlacesTotal.setObjectName(_fromUtf8("nbPlacesTotal"))
        self.horizontalLayout_3.addWidget(self.nbPlacesTotal)
        self.tableWidget = QtGui.QTableWidget(CreaParking)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 321, 121))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.btn_addRow = QtGui.QPushButton(CreaParking)
        self.btn_addRow.setGeometry(QtCore.QRect(350, 120, 41, 27))
        self.btn_addRow.setObjectName(_fromUtf8("btn_addRow"))
        self.btn_rmRow = QtGui.QPushButton(CreaParking)
        self.btn_rmRow.setGeometry(QtCore.QRect(350, 160, 41, 27))
        self.btn_rmRow.setObjectName(_fromUtf8("btn_rmRow"))
        self.layoutWidget2 = QtGui.QWidget(CreaParking)
        self.layoutWidget2.setGeometry(QtCore.QRect(52, 12, 291, 56))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEdit_nom = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEdit_nom.setObjectName(_fromUtf8("lineEdit_nom"))
        self.verticalLayout_2.addWidget(self.lineEdit_nom)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(CreaParking)
        QtCore.QMetaObject.connectSlotsByName(CreaParking)
        CreaParking.setTabOrder(self.lineEdit_nom, self.tableWidget)
        CreaParking.setTabOrder(self.tableWidget, self.btn_addRow)
        CreaParking.setTabOrder(self.btn_addRow, self.btn_rmRow)
        CreaParking.setTabOrder(self.btn_rmRow, self.btn_annuler)
        CreaParking.setTabOrder(self.btn_annuler, self.btn_valider)

    def retranslateUi(self, CreaParking):
        CreaParking.setWindowTitle(_translate("CreaParking", "Creation Parking", None))
        self.btn_annuler.setText(_translate("CreaParking", "Annuler", None))
        self.btn_valider.setText(_translate("CreaParking", "Valider", None))
        self.label_4.setText(_translate("CreaParking", "Nombre Places Total : ", None))
        self.nbPlacesTotal.setText(_translate("CreaParking", "TextLabel", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("CreaParking", "Hauteur", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("CreaParking", "Longueur", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("CreaParking", "Nombre", None))
        self.btn_addRow.setText(_translate("CreaParking", "+", None))
        self.btn_rmRow.setText(_translate("CreaParking", "-", None))
        self.label.setText(_translate("CreaParking", "Nom :", None))
