from PyQt5 import QtCore, QtGui, QtWidgets
import SQLStatements
from AddBreakfastInformation import formBreakfast
from AddLunchInformation import formLunch
from AddDinnerInformation import formDinner
from AddSnackInformation import formSnack
from AddExerciseInformation import formExercise
import progress


class Ui_Diary(object):

    def __init__(self, userID):
        self.userID = userID

    def setupUi(self, progress):
        #set window title
        progress.setWindowTitle("Diary")
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
        UserName = SQLStatements.getUserName(self.userID)
        self.labelName.setText(UserName)
        #set labels
        self.labelBreakfast = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelBreakfast.setGeometry(QtCore.QRect(50, 250, 81, 30))
        self.labelBreakfast.setStyleSheet("font: 75 10pt \"Lato\";" "color: rgb(255, 255, 255);")
        self.labelBreakfast.setText("Breakfast")
        self.labelBreakfastValue = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelBreakfastValue.setGeometry(QtCore.QRect(60, 275, 41, 31))
        self.labelBreakfastValue.setStyleSheet("\n""color: rgb(255, 255, 255);\n""text-align: center;")
        self.labelBreakfastValue.setText("0")

        self.labelLunch = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelLunch.setGeometry(QtCore.QRect(50, 310, 81, 20))
        self.labelLunch.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelLunch.setStyleSheet("font: 75 10pt \"Lato\";" "color: rgb(255, 255, 255);""text-align: centre;")
        self.labelLunch.setText("Lunch")
        self.labelLunchValue = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelLunchValue.setGeometry(QtCore.QRect(60, 345, 41, 31))
        self.labelLunchValue.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelLunchValue.setText("0")

        self.labelDinner = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelDinner.setGeometry(QtCore.QRect(50, 385, 81, 20))
        self.labelDinner.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelDinner.setStyleSheet("font: 75 10pt \"Lato\";""color: rgb(255, 255, 255);""text-align: centre;")
        self.labelDinner.setText("Dinner")
        self.labelDinnerValue = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelDinnerValue.setGeometry(QtCore.QRect(60, 415, 41, 31))
        self.labelDinnerValue.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelDinnerValue.setText("0")

        self.labelSnacks = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelSnacks.setGeometry(QtCore.QRect(50, 450, 81, 21))
        self.labelSnacks.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelSnacks.setStyleSheet("font: 75 10pt \"Lato\";" "color: rgb(255, 255, 255);""text-align: centre;")
        self.labelSnacks.setText("Snacks")
        self.labelSnacksValue = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelSnacksValue.setGeometry(QtCore.QRect(60, 490, 51, 21))
        self.labelSnacksValue.setStyleSheet("\n""color: rgb(255, 255, 255);")
        self.labelSnacksValue.setText("0")

        self.labelExercise = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelExercise.setGeometry(QtCore.QRect(50, 525, 75, 30))
        self.labelExercise.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelExercise.setStyleSheet("font: 75 10pt \"Lato\";" "color: rgb(255, 255, 255);""text-align: centre;")
        self.labelExercise.setText("Exercise")
        self.labelExerciseValue = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelExerciseValue.setGeometry(QtCore.QRect(60, 565, 41, 21))
        self.labelExerciseValue.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelExerciseValue.setText("0")

        self.labelBreakfastHeader = QtWidgets.QLabel(self.progress_2)
        self.labelBreakfastHeader.setGeometry(QtCore.QRect(210, 120, 281, 21))
        self.labelBreakfastHeader.setStyleSheet("font: 75 7pt \"Lato\";" "background-color: rgb(255, 255, 255);")

        self.labelLunchHeader = QtWidgets.QLabel(self.progress_2)
        self.labelLunchHeader.setGeometry(QtCore.QRect(870, 120, 281, 21))
        self.labelLunchHeader.setStyleSheet("font: 75 7pt \"Lato\";" "background-color: rgb(255, 255, 255);")

        self.labelDinnerHeader = QtWidgets.QLabel(self.progress_2)
        self.labelDinnerHeader.setGeometry(QtCore.QRect(210, 450, 281, 21))
        self.labelDinnerHeader.setStyleSheet("font: 75 7pt \"Lato\";" "background-color: rgb(255, 255, 255);")

        self.labelSnackHeader = QtWidgets.QLabel(self.progress_2)
        self.labelSnackHeader.setGeometry(QtCore.QRect(870, 450, 281, 21))
        self.labelSnackHeader.setStyleSheet("font: 75 7pt \"Lato\";" "background-color: rgb(255, 255, 255);")

        self.labelExerciseHeader = QtWidgets.QLabel(self.progress_2)
        self.labelExerciseHeader.setGeometry(QtCore.QRect(540, 300, 281, 21))
        self.labelExerciseHeader.setStyleSheet("font: 75 7pt \"Lato\";" "background-color: rgb(255, 255, 255);")
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
        #set table widgets
        self.tableWidgetBreakfast = QtWidgets.QTableWidget(self.progress_2)
        self.tableWidgetBreakfast.setGeometry(QtCore.QRect(210, 140, 281, 171))
        self.tableWidgetBreakfast.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetBreakfast.setLineWidth(1)
        self.tableWidgetBreakfast.setMidLineWidth(0)
        #max row count
        self.tableWidgetBreakfast.setRowCount(200)
        #max column count
        self.tableWidgetBreakfast.setColumnCount(3)

        self.tableWidgetExercise = QtWidgets.QTableWidget(self.progress_2)
        self.tableWidgetExercise.setGeometry(QtCore.QRect(540, 320, 281, 171))
        self.tableWidgetExercise.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetExercise.setLineWidth(1)
        self.tableWidgetExercise.setMidLineWidth(0)
        self.tableWidgetExercise.setRowCount(200)
        self.tableWidgetExercise.setColumnCount(2)

        self.tableWidgetlunch = QtWidgets.QTableWidget(self.progress_2)
        self.tableWidgetlunch.setGeometry(QtCore.QRect(870, 140, 281, 171))
        self.tableWidgetlunch.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetlunch.setLineWidth(1)
        self.tableWidgetlunch.setMidLineWidth(0)
        self.tableWidgetlunch.setRowCount(200)
        self.tableWidgetlunch.setColumnCount(3)

        self.tableWidgetSnacks = QtWidgets.QTableWidget(self.progress_2)
        self.tableWidgetSnacks.setGeometry(QtCore.QRect(870, 470, 281, 171))
        self.tableWidgetSnacks.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetSnacks.setLineWidth(1)
        self.tableWidgetSnacks.setMidLineWidth(0)
        self.tableWidgetSnacks.setRowCount(200)
        self.tableWidgetSnacks.setColumnCount(3)

        self.tableWidgetDinner = QtWidgets.QTableWidget(self.progress_2)
        self.tableWidgetDinner.setGeometry(QtCore.QRect(210, 470, 281, 171))
        self.tableWidgetDinner.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetDinner.setLineWidth(1)
        self.tableWidgetDinner.setMidLineWidth(0)
        self.tableWidgetDinner.setRowCount(200)
        self.tableWidgetDinner.setColumnCount(3)

        self.buttonUpdateBreakfast = QtWidgets.QPushButton(self.progress_2)
        self.buttonUpdateBreakfast.setGeometry(QtCore.QRect(350, 118, 75, 23))
        self.buttonUpdateBreakfast.setStyleSheet("font: 75 8pt \"Lato\";" "font-weight: bold;")
        self.buttonUpdateBreakfast.setFlat(True)
        self.buttonUpdateBreakfast.setText("Update")


        self.buttonUpdateLunch = QtWidgets.QPushButton(self.progress_2)
        self.buttonUpdateLunch.setGeometry(QtCore.QRect(1020, 118, 75, 23))
        self.buttonUpdateLunch.setStyleSheet("font: 75 8pt \"Lato\";" "font-weight: bold;")
        self.buttonUpdateLunch.setFlat(True)
        self.buttonUpdateLunch.setText("Update")

        self.buttonUpdateDinner = QtWidgets.QPushButton(self.progress_2)
        self.buttonUpdateDinner.setGeometry(QtCore.QRect(350, 448, 75, 23))
        self.buttonUpdateDinner.setStyleSheet("font: 75 8pt \"Lato\";" "font-weight: bold;")
        self.buttonUpdateDinner.setFlat(True)
        self.buttonUpdateDinner.setText("Update")

        self.buttonUpdateSnacks = QtWidgets.QPushButton(self.progress_2)
        self.buttonUpdateSnacks.setGeometry(QtCore.QRect(1010, 448, 75, 23))
        self.buttonUpdateSnacks.setStyleSheet("font: 75 8pt \"Lato\";" "font-weight: bold;")
        self.buttonUpdateSnacks.setFlat(True)

        self.buttonUpdateExercise = QtWidgets.QPushButton(self.progress_2)
        self.buttonUpdateExercise.setGeometry(QtCore.QRect(680, 298, 75, 23))
        self.buttonUpdateExercise.setStyleSheet("font: 75 8pt \"Lato\";" "font-weight: bold;")
        self.buttonUpdateExercise.setFlat(True)
        self.buttonUpdateExercise.setText("Update")

        self.buttonAddBreakfast = QtWidgets.QPushButton(self.progress_2)
        self.buttonAddBreakfast.setGeometry(QtCore.QRect(450, 118, 41, 23))
        self.buttonAddBreakfast.setStyleSheet("font: 75 8pt \"Lato\";" "font-weight: bold;")
        self.buttonAddBreakfast.setFlat(True)
        self.buttonAddBreakfast.setText("Add")

        self.buttonAddLunch = QtWidgets.QPushButton(self.progress_2)
        self.buttonAddLunch.setGeometry(QtCore.QRect(1110, 118, 41, 23))
        self.buttonAddLunch.setStyleSheet("font: 75 8pt \"Lato\";" "font-weight: bold;")

        self.buttonAddLunch.setFlat(True)
        self.buttonAddLunch.setText("Add")

        self.buttonAddDinner = QtWidgets.QPushButton(self.progress_2)
        self.buttonAddDinner.setGeometry(QtCore.QRect(450, 448, 41, 23))
        self.buttonAddDinner.setStyleSheet("font: 75 8pt \"Lato\";" "font-weight: bold;")
        self.buttonAddDinner.setFlat(True)

        self.buttonAddSnacks = QtWidgets.QPushButton(self.progress_2)
        self.buttonAddSnacks.setGeometry(QtCore.QRect(1110, 448, 41, 23))
        self.buttonAddSnacks.setStyleSheet("font: 75 8pt \"Lato\";" "font-weight: bold;")
        self.buttonAddSnacks.setFlat(True)

        self.buttonAddExercise = QtWidgets.QPushButton(self.progress_2)
        self.buttonAddExercise.setGeometry(QtCore.QRect(780, 298, 41, 23))
        self.buttonAddExercise.setStyleSheet("font: 75 8pt \"Lato\";" "font-weight: bold;")
        self.buttonAddExercise.setFlat(True)
        self.buttonAddExercise.setText("Add")

        self.dateEdit = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit.setGeometry(QtCore.QRect(410, 10, 181, 31))
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.labelBreakfastHeader.raise_()
        self.frameWhiteHeader.raise_()
        self.frameGreyBackground.raise_()
        self.frame_2.raise_()
        self.tableWidgetBreakfast.raise_()
        self.tableWidgetExercise.raise_()
        self.tableWidgetlunch.raise_()
        self.tableWidgetSnacks.raise_()
        self.tableWidgetDinner.raise_()
        self.buttonUpdateBreakfast.raise_()
        self.buttonAddBreakfast.raise_()
        self.labelLunchHeader.raise_()
        self.buttonUpdateLunch.raise_()
        self.buttonAddLunch.raise_()
        self.labelExerciseHeader.raise_()
        self.buttonUpdateExercise.raise_()
        self.buttonAddExercise.raise_()
        self.labelDinnerHeader.raise_()
        self.buttonUpdateDinner.raise_()
        self.buttonAddDinner.raise_()
        self.labelSnackHeader.raise_()
        self.buttonUpdateSnacks.raise_()
        self.buttonAddSnacks.raise_()

        self.labelBreakfast.setText("Breakfast")
        self.labelLunch.setText("Lunch")
        self.labelSnacks.setText("Snacks")
        self.labelBreakfastHeader.setText("  Breakfast")
        self.labelLunchHeader.setText("  Lunch")
        self.labelExerciseHeader.setText("Exercise")
        self.labelDinnerHeader.setText("  Dinner")
        self.buttonAddDinner.setText("Add")
        self.labelSnackHeader.setText("  Snacks")
        self.buttonUpdateSnacks.setText("Update")
        self.buttonAddSnacks.setText("Add")

        self.buttonUpdateBreakfast.clicked.connect(self.loadBreakfastData)
        self.buttonUpdateLunch.clicked.connect(self.loadLunchData)
        self.buttonUpdateDinner.clicked.connect(self.loadDinnerData)
        self.buttonUpdateSnacks.clicked.connect(self.loadSnacksData)
        self.buttonUpdateExercise.clicked.connect(self.loadExerciseData)

        self.buttonAddBreakfast.clicked.connect(self.openWindowDiary)
        self.buttonAddLunch.clicked.connect(self.openWindowLunch)
        self.buttonAddDinner.clicked.connect(self.openWindowDinner)
        self.buttonAddSnacks.clicked.connect(self.openWindowSnack)
        self.buttonAddExercise.clicked.connect(self.openWindowExercise)
        #self.buttonProgress.clicked.connect(self.openProgressWindow)


    def loadBreakfastData(self):
            try:
                # imput data from db into table
                    Date = self.dateEdit.date().toString(QtCore.Qt.ISODate)
                    result = SQLStatements.getBreakfastInfo(self.userID,Date)
                    self.tableWidgetBreakfast.setRowCount(0)
                    self.tableWidgetBreakfast.setHorizontalHeaderLabels(['Food', 'Calories', 'Grams'])
                    for row_number, row_data in enumerate(result):
                            self.tableWidgetBreakfast.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                    self.tableWidgetBreakfast.setItem(row_number, column_number,
                                                             QtWidgets.QTableWidgetItem(str(data)))
                    #set total calories amount
                    data = SQLStatements.getTotalBreakfastCalories(self.userID,Date)
                    tot = 0
                    for row in data:
                        tot += row[0]
                    self.labelBreakfastValue.setText(str(tot))

            except Exception as e:
                    print(e)

    

    def loadLunchData(self):
        try:
            Date = self.dateEdit.date().toString(QtCore.Qt.ISODate)
            result = SQLStatements.getlunchInfo(self.userID,Date)
            self.tableWidgetlunch.setRowCount(0)
            self.tableWidgetlunch.setHorizontalHeaderLabels(['Food', 'Calories', 'Grams'])
            for row_number, row_data in enumerate(result):
                    self.tableWidgetlunch.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                            self.tableWidgetlunch.setItem(row_number, column_number,
                                                          QtWidgets.QTableWidgetItem(str(data)))

            data = SQLStatements.getTotalLunchCalories(self.userID,Date)
            tot = 0
            for row in data:
                tot += row[0]
            self.labelLunchValue.setText(str(tot))

        except Exception as e: print(e)

    def loadDinnerData(self):
        try:
            Date = self.dateEdit.date().toString(QtCore.Qt.ISODate)
            result = SQLStatements.getDinnerInfo(self.userID,Date)
            self.tableWidgetDinner.setRowCount(0)
            self.tableWidgetDinner.setHorizontalHeaderLabels(['Food', 'Calories', 'Grams'])
            for row_number, row_data in enumerate(result):
                    self.tableWidgetDinner.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                            self.tableWidgetDinner.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


            data = SQLStatements.getTotalDinnerCalories(self.userID,Date)
            tot = 0
            for row in data:
                tot += row[0]
            self.labelDinnerValue.setText(str(tot))
        except Exception as e: print(e)

    def loadSnacksData(self):
        try:
            Date = self.dateEdit.date().toString(QtCore.Qt.ISODate)
            result = SQLStatements.getSnackInfo(self.userID,Date)
            self.tableWidgetSnacks.setRowCount(0)
            self.tableWidgetSnacks.setHorizontalHeaderLabels(['Food', 'Calories', 'Grams'])
            for row_number, row_data in enumerate(result):
                    self.tableWidgetSnacks.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                            self.tableWidgetSnacks.setItem(row_number, column_number,
                                                           QtWidgets.QTableWidgetItem(str(data)))

            data = SQLStatements.getTotalSnacksCalories(self.userID,Date)
            tot = 0
            for row in data:
                tot += row[0]
            self.labelSnacksValue.setText(str(tot))
        except Exception as e:
            print(e)

    def loadExerciseData(self):
        try:
            Date = self.dateEdit.date().toString(QtCore.Qt.ISODate)
            result = SQLStatements.getExerciseInfo(self.userID,Date)
            self.tableWidgetExercise.setRowCount(0)
            self.tableWidgetExercise.setHorizontalHeaderLabels(['Exercise', 'Calories lost'])
            for row_number, row_data in enumerate(result):
                    self.tableWidgetExercise.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                            self.tableWidgetExercise.setItem(row_number, column_number,
                                                             QtWidgets.QTableWidgetItem(str(data)))

            data = SQLStatements.getTotalExerciseCalories(self.userID)
            tot = 0
            for row in data:
                tot += row[0]
            self.labelExerciseValue.setText(str(tot))
        except Exception as e: print(e)

    def openWindowDiary(self):
        try:
            self.ui = formBreakfast(self.userID)
            self.ui.show()
        except Exception as e:
            print(e)

    def openWindowLunch(self):

            self.ui = formLunch(self.userID)
            self.ui.show()

    def openWindowDinner(self):

            self.ui = formDinner(self.userID)
            self.ui.show()

    def openWindowSnack(self):

            self.ui = formSnack(self.userID)
            self.ui.show()

    def openWindowExercise(self):
        try:
            self.ui = formExercise(self.userID)
            self.ui.show()
        except Exception as e:
            print(e)

        except Exception as e:
            print(e)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    progress = QtWidgets.QMainWindow()
    ui = Ui_Diary()
    ui.setupUi(progress)
    progress.show()
    sys.exit(app.exec_())
