from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import login
import userInfo
import sys

class Ui_signUpWindow(object):

    def setupUi(self, signUpWindow):

        # main window stuff
        signUpWindow.setWindowTitle("Sign Up")
        signUpWindow.setFixedSize(993,600)
        signUpWindow.resize(993, 600)
        signUpWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.267, y1:0.642, x2:0.778, y2:0.323864, stop:0 rgba(0, 150, 136, 255), stop:1 rgba(63, 81, 181, 255));")
        self.centralwidget = QtWidgets.QWidget(signUpWindow)
        signUpWindow.setCentralWidget(self.centralwidget)

        #white background
        self.whiteBackground = QtWidgets.QFrame(self.centralwidget)
        self.whiteBackground.setGeometry(QtCore.QRect(110, 40, 371, 491))
        self.whiteBackground.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.whiteBackground.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.whiteBackground.setFrameShadow(QtWidgets.QFrame.Raised)
        self.whiteBackground.setObjectName("whiteBackground")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(480, 40, 411, 491))
        self.frame.setStyleSheet("border-image: url(:/images/mfh.png) 0 0 0 0 stretch stretch;""")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # signUp.py title
        self.labelSignUp = QtWidgets.QLabel(self.whiteBackground)
        self.labelSignUp.setGeometry(QtCore.QRect(150, 30, 81, 51))
        self.labelSignUp.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.labelSignUp.setText("Sign up")

        self.labelHaveAccount = QtWidgets.QLabel(self.whiteBackground)
        self.labelHaveAccount.setGeometry(QtCore.QRect(100, 370, 191, 31))
        self.labelHaveAccount.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.labelHaveAccount.setText("Already have an account?")

        # email input
        self.lineEditEmail = QtWidgets.QLineEdit(self.whiteBackground)
        self.lineEditEmail.setGeometry(QtCore.QRect(70, 100, 251, 31))
        self.lineEditEmail.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";""")
        self.lineEditEmail.setClearButtonEnabled(True)
        self.lineEditEmail.setPlaceholderText("Email")

        # password input
        self.lineEditPassword = QtWidgets.QLineEdit(self.whiteBackground)
        self.lineEditPassword.setGeometry(QtCore.QRect(70, 150, 251, 31))
        self.lineEditPassword.setAutoFillBackground(False)
        self.lineEditPassword.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.lineEditPassword.setClearButtonEnabled(True)
        self.lineEditPassword.setPlaceholderText("Password")

        # retype password input
        self.lineEditReType = QtWidgets.QLineEdit(self.whiteBackground)
        self.lineEditReType.setGeometry(QtCore.QRect(70, 200, 251, 31))
        self.lineEditReType.setAutoFillBackground(False)
        self.lineEditReType.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.lineEditReType.setClearButtonEnabled(True)
        self.lineEditReType.setPlaceholderText("Re type Password")

        # phone number input
        self.lineEditNumber = QtWidgets.QLineEdit(self.whiteBackground)
        self.lineEditNumber.setGeometry(QtCore.QRect(70, 250, 251, 31))
        self.lineEditNumber.setAutoFillBackground(False)
        self.lineEditNumber.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.lineEditNumber.setClearButtonEnabled(True)

        #ensure only numbers can be entered
        self.onlyInt = QIntValidator()
        self.lineEditNumber.setValidator(self.onlyInt)
        self.lineEditNumber.setPlaceholderText("Contact number")

        # login button
        self.buttonSignUp = QtWidgets.QPushButton(self.whiteBackground)
        self.buttonSignUp.setGeometry(QtCore.QRect(130, 300, 121, 41))
        self.buttonSignUp.setStyleSheet("background-color: rgb(85, 170, 255);""font: 12pt \"MS Shell Dlg 2\";""color: rgb(255, 255, 255);")
        self.buttonSignUp.setFlat(False)
        self.buttonSignUp.setText("Sign up")
        self.buttonSignUp.clicked.connect(self.openUserInfoWindow)

        self.buttonSignIn = QtWidgets.QPushButton(self.whiteBackground)
        self.buttonSignIn.setGeometry(QtCore.QRect(160, 400, 75, 23))
        self.buttonSignIn.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";""color: rgb(85, 170, 255);")
        self.buttonSignIn.setFlat(True)
        self.buttonSignIn.clicked.connect(self.openLoginWindow)
        self.buttonSignIn.setText("Sign in")

    #open login window
    def openLoginWindow(self):
        try:
             self.window=QtWidgets.QMainWindow()
             self.ui = login.Ui_LoginWindow()
             self.ui.setupUi(self.window)
            # signUpWindow.hide()
             self.window.show()

        except Exception as e:
            print(e)

    #open users additional info window
    def openUserInfoWindow(self):
        try:
            #take inputs as variables
            password = self.lineEditPassword.text()
            passwordCheck = self.lineEditReType.text()

            #if passwords dont match
            if (password != passwordCheck):
                #send a message box to tell user
                QMessageBox.warning(QMessageBox(), 'Error', 'Passwords do not match')
            else:

                self.window=QtWidgets.QMainWindow()

                # take inputs as variables
                self.email=self.lineEditEmail.text()
                self.password = self.lineEditPassword.text()
                self.num = self.lineEditNumber.text()

                #open new window sending variables
                self.ui = userInfo.Ui_userInfoWindow(self.email,self.password,self.num)
                self.ui.setupUi(self.window)
                #signUpWindow.close()
                self.window.show()

        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    signUpWindow = QtWidgets.QMainWindow()
    ui = Ui_signUpWindow()
    ui.setupUi(signUpWindow)
    signUpWindow.show()
    sys.exit(app.exec_())
