from PyQt5 import QtCore, QtGui, QtWidgets
import SQLStatements




class Ui_Profile(object):


        def setupUi(self, progress):
            #set window title
            progress.setWindowTitle("Profile")
            progress.resize(1188, 730)
            progress.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.267, y1:0.642, x2:0.778, y2:0.323864, stop:0 rgba(0, 150, 136, 255), stop:1 rgba(63, 81, 181, 255));\n""")
            self.progress_2 = QtWidgets.QWidget(progress)
            QtCore.QMetaObject.connectSlotsByName(progress)
            progress.setCentralWidget(self.progress_2)

            self.frameWhiteHeader = QtWidgets.QFrame(self.progress_2)
            self.frameWhiteHeader.setGeometry(QtCore.QRect(0, 0, 1191, 51))
            self.frameWhiteHeader.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.frameWhiteHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frameWhiteHeader.setFrameShadow(QtWidgets.QFrame.Raised)

            self.frameGreyBackground = QtWidgets.QFrame(self.progress_2)
            self.frameGreyBackground.setGeometry(QtCore.QRect(0, 50, 181, 761))
            self.frameGreyBackground.setStyleSheet("background-color: rgb(96, 125, 139);")
            self.frameGreyBackground.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frameGreyBackground.setFrameShadow(QtWidgets.QFrame.Raised)

            self.frame_2 = QtWidgets.QFrame(self.progress_2)
            self.frame_2.setGeometry(QtCore.QRect(180, 50, 1011, 51))
            self.frame_2.setStyleSheet("background-color: rgb(224, 224, 224);")
            self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)

            self.frameGreyHeader = QtWidgets.QFrame(self.frame_2)
            self.frameGreyHeader.setGeometry(QtCore.QRect(140, 50, 1011, 51))
            self.frameGreyHeader.setStyleSheet("background-color: rgb(240, 240, 240);")
            self.frameGreyHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frameGreyHeader.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frameGreyHeader.setObjectName("frameGreyHeader")

            self.frameUserPhoto = QtWidgets.QFrame(self.frameGreyBackground)
            self.frameUserPhoto.setGeometry(QtCore.QRect(30, 40, 120, 120))
            self.frameUserPhoto.setStyleSheet("image: url(:/images/default-user.png);\n""border-radius: 90px;")
            self.frameUserPhoto.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.frameUserPhoto.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frameUserPhoto.setLineWidth(27)

            self.labelName = QtWidgets.QLabel(self.frameGreyBackground)
            self.labelName.setGeometry(QtCore.QRect(50, 170, 100, 21))
            self.labelName.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n""color: rgb(255, 255, 255);")
         
            #set buttons
            self.buttonProfile = QtWidgets.QPushButton(self.frameWhiteHeader)
            self.buttonProfile.setGeometry(QtCore.QRect(0, 0, 85, 51))
            self.buttonProfile.setStyleSheet("font: 75 10pt \"Lato\";")
            self.buttonProfile.setFlat(True)
            self.buttonProfile.setText("       Profile |    ")

            self.buttonDiary = QtWidgets.QPushButton(self.frameWhiteHeader)
            self.buttonDiary.setGeometry(QtCore.QRect(88, 0, 90, 51))
            self.buttonDiary.setStyleSheet("font: 75 10pt \"Lato\";")
            self.buttonDiary.setFlat(True)
            self.buttonDiary.setText("Diary |       ")

            self.buttonPlans = QtWidgets.QPushButton(self.frameWhiteHeader)
            self.buttonPlans.setGeometry(QtCore.QRect(145, 0, 85, 51))
            self.buttonPlans.setStyleSheet("font: 75 10pt \"Lato\";")
            self.buttonPlans.setFlat(True)
            self.buttonPlans.setText("        Plans |      ")

            self.buttonProgress = QtWidgets.QPushButton(self.frameWhiteHeader)
            self.buttonProgress.setGeometry(QtCore.QRect(230, 0, 100, 51))
            self.buttonProgress.setStyleSheet("font: 75 10pt \"Lato\";")
            self.buttonProgress.setFlat(True)
            self.buttonProgress.setText("    Progress |   ")

            self.buttonNutrition = QtWidgets.QPushButton(self.frameWhiteHeader)
            self.buttonNutrition.setGeometry(QtCore.QRect(330, 0, 100, 51))
            self.buttonNutrition.setStyleSheet("font: 75 10pt \"Lato\";")
            self.buttonNutrition.setFlat(True)
            self.buttonNutrition.setText("     Nutrition |  ")

            self.signOut = QtWidgets.QPushButton(self.frameWhiteHeader)
            self.signOut.setGeometry(QtCore.QRect(1050, 0, 110, 51))
            self.signOut.setStyleSheet("font: 75 10pt \"Lato\";")
            self.signOut.setFlat(True)
            self.signOut.setText("      Sign Out")

            self.buttonLeftArrow = QtWidgets.QPushButton(self.frame_2)
            self.buttonLeftArrow.setGeometry(QtCore.QRect(0, 0, 61, 51))
            self.buttonLeftArrow.setStyleSheet("border: 1px solid #C8C8C8;")
            self.buttonLeftArrow.setFlat(True)
            self.buttonLeftArrow.setText("<")

            self.buttonRightArrow = QtWidgets.QPushButton(self.frame_2)
            self.buttonRightArrow.setGeometry(QtCore.QRect(950, 0, 61, 51))
            self.buttonRightArrow.setStyleSheet("border: 1px solid #C8C8C8;")
            self.buttonRightArrow.setFlat(True)
            self.buttonRightArrow.setText(">")

            self.frameGreyHeader = QtWidgets.QFrame(self.frame_2)
            self.frameGreyHeader.setGeometry(QtCore.QRect(140, 50, 1011, 51))
            self.frameGreyHeader.setStyleSheet("background-color: rgb(240, 240, 240);")
            self.frameGreyHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frameGreyHeader.setFrameShadow(QtWidgets.QFrame.Raised)

            self.dateEdit = QtWidgets.QDateEdit(self.frame_2)
            self.dateEdit.setGeometry(QtCore.QRect(410, 10, 181, 31))
            self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

            self.frameWhiteHeader.raise_()
            self.frameGreyBackground.raise_()
            self.frame_2.raise_()
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    progress = QtWidgets.QMainWindow()
    ui = Ui_Profile()
    ui.setupUi(progress)
    progress.show()
    sys.exit(app.exec_())
