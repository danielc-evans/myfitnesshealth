from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import SQLStatements
import login
import signUp
import images2_rc_rc


class Ui_userInfoWindow(object):

    #receive variables from other form
    def __init__(self, email, password, num):
        self.email = email
        self.password = password
        self.num = num

    def setupUi(self, userInfoWindow):
        #set user window
        userInfoWindow.setFixedSize(993,600)
        userInfoWindow.resize(993, 600)
        userInfoWindow.setWindowTitle("Personal Information")
        userInfoWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.267, y1:0.642, x2:0.778, y2:0.323864, stop:0 rgba(0, 150, 136, 255), stop:1 rgba(63, 81, 181, 255));")
        self.centralwidget = QtWidgets.QWidget(userInfoWindow)
        userInfoWindow.setCentralWidget(self.centralwidget)

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(460, 30, 411, 491))
        self.frame_2.setStyleSheet("""border-image: url(:/images2/mfh.png);""")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)

        self.whiteBackground = QtWidgets.QFrame(self.centralwidget)
        self.whiteBackground.setGeometry(QtCore.QRect(90, 30, 371, 491))
        self.whiteBackground.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.whiteBackground.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.whiteBackground.setFrameShadow(QtWidgets.QFrame.Raised)

        self.labelDOB = QtWidgets.QLabel(self.whiteBackground)
        self.labelDOB.setGeometry(QtCore.QRect(70, 330, 101, 31))
        self.labelDOB.setStyleSheet("color: rgb(126, 126, 126);""font: 13pt \"MS Shell Dlg 2\";")
        self.labelDOB.setText("Date of Birth")

        self.labelDetails = QtWidgets.QLabel(self.whiteBackground)
        self.labelDetails.setGeometry(QtCore.QRect(140, 30, 121, 51))
        self.labelDetails.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.labelDetails.setText("My details")

        self.lineEditFirstName = QtWidgets.QLineEdit(self.whiteBackground)
        self.lineEditFirstName.setGeometry(QtCore.QRect(70, 90, 251, 31))
        self.lineEditFirstName.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";""")
        self.lineEditFirstName.setClearButtonEnabled(True)
        self.lineEditFirstName.setPlaceholderText("First Name")

        self.lineEditlastName = QtWidgets.QLineEdit(self.whiteBackground)
        self.lineEditlastName.setGeometry(QtCore.QRect(70, 150, 251, 31))
        self.lineEditlastName.setAutoFillBackground(False)
        self.lineEditlastName.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";\n""")
        self.lineEditlastName.setClearButtonEnabled(True)
        self.lineEditlastName.setPlaceholderText("Last Name")

        self.lineEditHeight = QtWidgets.QLineEdit(self.whiteBackground)
        self.lineEditHeight.setGeometry(QtCore.QRect(70, 210, 251, 31))
        self.lineEditHeight.setAutoFillBackground(False)
        self.lineEditHeight.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.lineEditHeight.setClearButtonEnabled(True)
        self.lineEditHeight.setPlaceholderText("Height (cm)")

        self.lineEditWeight = QtWidgets.QLineEdit(self.whiteBackground)
        self.lineEditWeight.setGeometry(QtCore.QRect(70, 270, 251, 31))
        self.lineEditWeight.setAutoFillBackground(False)
        self.lineEditWeight.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.lineEditWeight.setClearButtonEnabled(True)
        self.lineEditWeight.setPlaceholderText("Weight (kg)")

        self.dateEdit = QtWidgets.QDateEdit(self.whiteBackground)
        self.dateEdit.setGeometry(QtCore.QRect(190, 330, 131, 31))

        self.buttonSubmit = QtWidgets.QPushButton(self.whiteBackground)
        self.buttonSubmit.setGeometry(QtCore.QRect(130, 390, 121, 41))
        self.buttonSubmit.setStyleSheet("background-color: rgb(85, 170, 255);""font: 12pt \"MS Shell Dlg 2\";""color: rgb(255, 255, 255);")
        self.buttonSubmit.setFlat(False)
        self.buttonSubmit.clicked.connect(self.addUsersinfo)
        self.buttonSubmit.setText("Submit")

    def addUsersinfo(self):
        try:
            #take inputs as variables
            e = self.email
            pw = self.password
            pn = self.num
            fn = self.lineEditFirstName.text()
            sn = self.lineEditlastName.text()
            dateOfBirth = self.dateEdit.text()
            w = self.lineEditWeight.text()
            h = self.lineEditHeight.text()
            sw = w

            #if a user is added
            if (SQLStatements.addUserInfo(e, pw, pn, fn, sn, dateOfBirth, w, h, sw) == 'True'):

                #show message box and open login window
                QMessageBox.about(QMessageBox(), 'Success', 'you have been added to the database.')
                self.openLoginWindow()
                #if it doesnt work
            elif (SQLStatements.addUserInfo(e, pw, pn, fn, sn, dateOfBirth, w, h, sw) == 'checkFailed'):
                #show message box
                QMessageBox.warning(QMessageBox(), 'Error', 'Email exists')
                #reopen sign in window
                self.openSignInWindow()

            else:
                QMessageBox.warning(QMessageBox(), 'Error', 'Could not add you to the database.')

        except Exception as e:
            print(e)
    #open the login window
    def openLoginWindow(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = login.Ui_LoginWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    #open the signUp window
    def openSignInWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = signUp.Ui_signUpWindow()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    userInfoWindow = QtWidgets.QMainWindow()
    ui = Ui_userInfoWindow()
    ui.setupUi(userInfoWindow)
    userInfoWindow.show()
    sys.exit(app.exec_())
