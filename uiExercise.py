from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(450, 240)
        MainWindow.setWindowTitle("Add Information")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.labelFood = QtWidgets.QLabel(self.centralwidget)
        self.labelFood.setGeometry(QtCore.QRect(10, 30, 100, 13))
        self.labelFood.setText("Food")

        self.labelCalories = QtWidgets.QLabel(self.centralwidget)
        self.labelCalories.setGeometry(QtCore.QRect(10, 80, 100, 13))
        self.labelCalories.setText("Calories")

        self.labelGrams = QtWidgets.QLabel(self.centralwidget)
        self.labelGrams.setGeometry(QtCore.QRect(10, 130, 100, 13))
        self.labelGrams.setText("Grams")

        self.lineEditFood = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFood.setGeometry(QtCore.QRect(10, 50, 411, 20))

        self.lineEditCalories = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCalories.setGeometry(QtCore.QRect(10, 100, 411, 20))
        self.onlyInt = QIntValidator()
        self.lineEditCalories.setValidator(self.onlyInt)

        self.lineEditGrams = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditGrams.setGeometry(QtCore.QRect(10, 150, 411, 20))
        self.onlyInt = QIntValidator()
        self.lineEditGrams.setValidator(self.onlyInt)

        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(10, 200 , 75, 23))
        self.addButton.setText("Add")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


