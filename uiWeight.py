# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lenovo\Downloads\uiWeight.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(398, 233)
        self.labelformUpdateWeight = QtWidgets.QLabel(Dialog)
        self.labelformUpdateWeight.setGeometry(QtCore.QRect(60, 10, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelformUpdateWeight.setFont(font)
        self.labelformUpdateWeight.setObjectName("labelformUpdateWeight")
        self.lineEditUpdateWeight = QtWidgets.QLineEdit(Dialog)
        self.lineEditUpdateWeight.setGeometry(QtCore.QRect(130, 90, 251, 51))
        self.lineEditUpdateWeight.setText("")
        self.lineEditUpdateWeight.setObjectName("lineEditUpdateWeight")
        self.labelformWeightField = QtWidgets.QLabel(Dialog)
        self.labelformWeightField.setGeometry(QtCore.QRect(10, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelformWeightField.setFont(font)
        self.labelformWeightField.setObjectName("labelformWeightField")
        self.formSubmitWeightChange = QtWidgets.QPushButton(Dialog)
        self.formSubmitWeightChange.setGeometry(QtCore.QRect(244, 170, 131, 50))
        self.formSubmitWeightChange.setObjectName("formSubmitWeightChange")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Update Current Weight"))
        self.labelformUpdateWeight.setText(_translate("Dialog", "Set Current Weight"))
        self.labelformWeightField.setText(_translate("Dialog", "Current Weight"))
        self.formSubmitWeightChange.setText(_translate("Dialog", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
