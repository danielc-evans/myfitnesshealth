import unittest

from PyQt5 import QtCore, QtWidgets, QtTest
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QMessageBox

import signUp
import SQLStatements
from progress import Ui_progress


class Ui_LoginWindow(object):

    def setupUi(self,LoginWindow):
        #set login window
        LoginWindow.setFixedSize(993,600)
        LoginWindow.resize(993, 600)
        LoginWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.267, y1:0.642, x2:0.778, y2:0.323864, stop:0 rgba(0, 150, 136, 255), stop:1 rgba(63, 81, 181, 255));")
        LoginWindow.setWindowTitle("Login")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        LoginWindow.setCentralWidget(self.centralwidget)

        #white panel
        self.frameWhite = QtWidgets.QFrame(self.centralwidget)
        self.frameWhite.setGeometry(QtCore.QRect(90, 50, 331, 441))
        self.frameWhite.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frameWhite.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameWhite.setFrameShadow(QtWidgets.QFrame.Raised)

        #frame for photo
        self.framePhoto = QtWidgets.QFrame(self.centralwidget)
        self.framePhoto.setGeometry(QtCore.QRect(410, 50, 511, 441))
        self.framePhoto.setStyleSheet("background-image: url(:/images/mfh2.png);")
        self.framePhoto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePhoto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePhoto.raise_()
        self.frameWhite.raise_()

        #update Photo
        self.labelUpdatePhoto = QtWidgets.QLabel(self.frameWhite)
        self.labelUpdatePhoto.setGeometry(QtCore.QRect(410, 150, 511, 441))
        self.labelUpdatePhoto.setText("hi")

        #login label
        self.labelLogin = QtWidgets.QLabel(self.frameWhite)
        self.labelLogin.setGeometry(QtCore.QRect(140, 10, 71, 51))
        self.labelLogin.setStyleSheet("font: 75 20pt \"SourceSansPro\";")
        self.labelLogin.setText("Login")

        #label for if user has an account
        self.labelQuestion = QtWidgets.QLabel(self.frameWhite)
        self.labelQuestion.setGeometry(QtCore.QRect(80, 340, 191, 31))
        self.labelQuestion.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.labelQuestion.setText("Do not have an account?")

        #sign up button
        self.buttonSignUp = QtWidgets.QPushButton(self.frameWhite)
        self.buttonSignUp.setGeometry(QtCore.QRect(140, 370, 75, 23))
        self.buttonSignUp.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n""color: rgb(85, 170, 255);")
        self.buttonSignUp.setFlat(True)
        self.buttonSignUp.clicked.connect(self.openSignInWindow)
        self.buttonSignUp.setText("Sign Up")

        #login page button
        self.buttonLogin = QtWidgets.QPushButton(self.frameWhite)
        self.buttonLogin.setGeometry(QtCore.QRect(110, 190, 121, 41))
        self.buttonLogin.setStyleSheet("background-color: rgb(85, 170, 255);\n""\n""font: 75 20pt \"SourceSansPro\";\n""color: rgb(255, 255, 255);")
        self.buttonLogin.setFlat(False)
        self.buttonLogin.clicked.connect(self.login)
        self.buttonLogin.setText("Login")

        #text box for email
        self.lineEditEmail = QtWidgets.QLineEdit(self.frameWhite)
        self.lineEditEmail.setGeometry(QtCore.QRect(50, 70, 251, 31))
        self.lineEditEmail.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.lineEditEmail.setPlaceholderText("Email")

        #text box for password
        self.lineEditPassword = QtWidgets.QLineEdit(self.frameWhite)
        self.lineEditPassword.setGeometry(QtCore.QRect(50, 130, 251, 31))
        self.lineEditPassword.setAutoFillBackground(False)
        self.lineEditPassword.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.lineEditPassword.setPlaceholderText("Password")



    def login(self):
        try:
            #taking inputs as variables
            email = self.lineEditEmail.text()
            passwordInput = self.lineEditPassword.text()
            passwordInput = ("('"+passwordInput+"',)")

            if (SQLStatements.getUserID(email) == "NoUser"):
                #if a user doesnt exist send a message box
                QMessageBox.warning(QMessageBox(), 'Error', 'User does not exist!')


            else:
                #taking inputs as variables
                userID = SQLStatements.getUserID(email)
                passwordCheck = SQLStatements.checkPassword(userID)
                passwordCheckString = str(passwordCheck)

                #if passwords do not match
                if (passwordInput != passwordCheckString):
                    #tell user
                    QMessageBox.warning(QMessageBox(), 'Error', 'Password incorrect!')
                else:
                    #open progress window
                    self.openProgressWindow(userID)

        except Exception as e:
            print(e)
    #function to open sign in window
    def openSignInWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = signUp.Ui_signUpWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    #function to open progress window
    def openProgressWindow(self,userID):
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_progress(userID)
            self.ui.setupUi(self.window)
            self.window.show()
        except Exception as e:
            print (e)

    def test_defaults(self):

        lineEditEmail="pat@gmail.com"
        self.lineEditPassword = "1234"
        self.form.passwordLineEdit.setText('123456')
        QtTest.QTest.mouseClick(self.buttonLogin, QtCore.Qt.LeftButton)



if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())