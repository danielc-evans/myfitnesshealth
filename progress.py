from PyQt5 import QtCore, QtGui, QtWidgets
import login
import diary
import Plans
import Nutrition
import Profile
import lineGraph
import bmiCalculator
from  AddWeightInformation import AddWeightInformation

import SQLStatements
import images_rc



class Ui_progress(object):

    def __init__(self, userID):
        self.userID = userID


    def setupUi(self, progress):
        #set window parameters
        progress.setFixedSize(1188,730)
        progress.resize(1188, 730)
        progress.setWindowTitle("Home Page")
        progress.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.267, y1:0.642, x2:0.778, y2:0.323864, stop:0 rgba(0, 150, 136, 255), stop:1 rgba(63, 81, 181, 255));""")
        self.progress_2 = QtWidgets.QWidget(progress)
        progress.setCentralWidget(self.progress_2)

        self.frameWhiteHeader = QtWidgets.QFrame(self.progress_2)
        self.frameWhiteHeader.setGeometry(QtCore.QRect(0, 0, 1191, 51))
        self.frameWhiteHeader.setStyleSheet("\n""background-color: rgb(255, 255, 255);")
        self.frameWhiteHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameWhiteHeader.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frameGreyBackground = QtWidgets.QFrame(self.progress_2)
        self.frameGreyBackground.setGeometry(QtCore.QRect(0, 50, 181, 761))
        self.frameGreyBackground.setStyleSheet("background-color: rgb(96, 125, 139);")
        self.frameGreyBackground.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameGreyBackground.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frameGreyHeader2 = QtWidgets.QFrame(self.progress_2)
        self.frameGreyHeader2.setGeometry(QtCore.QRect(180, 50, 1011, 51))
        self.frameGreyHeader2.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.frameGreyHeader = QtWidgets.QFrame(self.frameGreyHeader2)
        self.frameGreyHeader.setGeometry(QtCore.QRect(140, 50, 1011, 51))
        self.frameGreyHeader.setStyleSheet("background-color: rgb(240, 240, 240);")

        #set label for calorie budget
        self.labelCalorieBudget = QtWidgets.QLabel(self.progress_2)
        self.labelCalorieBudget.setGeometry(QtCore.QRect(350, 140, 200, 71))
        self.labelCalorieBudget.setStyleSheet("font: 200 15pt \"Lato\";" "color: rgb(255, 255, 255);""""background-color: transparent;""")
        self.labelCalorieBudget.setText("BMI")




        #set label for weightloss
        self.labelWeightGoalProgress = QtWidgets.QLabel(self.progress_2)
        self.labelWeightGoalProgress.setGeometry(QtCore.QRect(820, 140, 200, 71))
        self.labelWeightGoalProgress.setStyleSheet("font: 75 15pt \"Lato\";" "color: rgb(255, 255, 255);""""background-color: transparent;""")
        self.labelWeightGoalProgress.setText("Weight Goal Progress")

        # set label for static starting weight name
        self.labelStaticStartingWeight = QtWidgets.QLabel(self.progress_2)
        self.labelStaticStartingWeight.setGeometry(QtCore.QRect(800, 300, 200, 30))
        self.labelStaticStartingWeight.setStyleSheet("font: 75 15pt \"Lato\";" "color: rgb(255, 255, 255);""""background-color: transparent;""")
        self.labelStaticStartingWeight.setText("Starting Weight")

        # set label for static current weight name
        self.labelStaticCurrentWeight = QtWidgets.QLabel(self.progress_2)
        self.labelStaticCurrentWeight.setGeometry(QtCore.QRect(800, 400, 200, 71))
        self.labelStaticCurrentWeight.setStyleSheet("font: 75 15pt \"Lato\";" "color: rgb(255, 255, 255);""""background-color: transparent;""")
        self.labelStaticCurrentWeight.setText("Current Weight")



        # set label for current weight value
        self.labelCurrentWeight = QtWidgets.QLabel(self.progress_2)
        self.labelCurrentWeight.setGeometry(QtCore.QRect(980, 400, 300, 80))
        self.labelCurrentWeight.setStyleSheet("font: 75 15pt \"Lato\";" "color: rgb(255, 255, 255);""""background-color: transparent;""")
        self.labelCurrentWeight.setText("0")

        # set label for starting weight value
        self.labelStartingWeight = QtWidgets.QLabel(self.progress_2)
        self.labelStartingWeight.setGeometry(QtCore.QRect(980, 300, 200, 30))
        self.labelStartingWeight.setStyleSheet("font: 75 15pt \"Lato\";" "color: rgb(255, 255, 255);""""text-align: center; background-color: transparent;""")
        self.labelStartingWeight.setText("0")


        #BMI VALUE
        self.BMIValue = QtWidgets.QLabel(self.progress_2)
        self.BMIValue.setGeometry(QtCore.QRect(425, 305, 120, 20))
        self.BMIValue.setStyleSheet("font: 75 15pt \"Lato\";" "color: rgb(255, 255, 255);""""text-align: center; background-color: transparent;""")
        self.BMIValue.setText("0")

        labelCurrentBmi = QtWidgets.QLabel(self.progress_2)
        labelCurrentBmi.setGeometry(QtCore.QRect(300, 305, 120, 20))
        labelCurrentBmi.setStyleSheet("font: 75 15pt \"Lato\";" "color: rgb(255, 255, 255);""""text-align: center; background-color: transparent;""")
        labelCurrentBmi.setText("Current BMI:")



        # set label for static starting weight kg
        self.labelStaticStartingWeightKg = QtWidgets.QLabel(self.progress_2)
        self.labelStaticStartingWeightKg.setGeometry(QtCore.QRect(1050, 300, 300, 30))
        self.labelStaticStartingWeightKg.setStyleSheet("font: 75 15pt \"Lato\";" "color: rgb(255, 255, 255);""""background-color: transparent;""")
        self.labelStaticStartingWeightKg.setText("kg")

        # set label for static current weight kg
        self.labelStaticCurrentWeightKg = QtWidgets.QLabel(self.progress_2)
        self.labelStaticCurrentWeightKg.setGeometry(QtCore.QRect(1050, 400, 300, 80))
        self.labelStaticCurrentWeightKg.setStyleSheet("font: 75 15pt \"Lato\";" "color: rgb(255, 255, 255);""""background-color: transparent;""")
        self.labelStaticCurrentWeightKg.setText("kg")

        #GEOMETRY
        #First Value - X is left or right
        # Second Value Y is up or down
        # Third value is width
        # Fourth value is height

        #set label for member date
        self.labelMember = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelMember.setGeometry(QtCore.QRect(20, 200, 111, 31))
        self.labelMember.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelMember.setText("Member Since:")

        self.labelSteps = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelSteps.setGeometry(QtCore.QRect(60, 320, 41, 41))
        self.labelSteps.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelSteps.setStyleSheet("font: 75 12pt \"Lato\";" "color: rgb(255, 255, 255);""""background-color: transparent;""")
        self.labelSteps.setText("Steps")

        self.labelWater = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelWater.setGeometry(QtCore.QRect(60, 420, 41, 41))
        self.labelWater.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelWater.setStyleSheet("font: 75 12pt \"Lato\";" "color: rgb(255, 255, 255);""""background-color: transparent;""")
        self.labelWater.setText("Water")

        #frame for users photo
        self.frameUserPhoto = QtWidgets.QFrame(self.frameGreyBackground)
        self.frameUserPhoto.setGeometry(QtCore.QRect(30, 40, 120, 120))
        self.frameUserPhoto.setStyleSheet("image: url(:/images/default-user.png);\n""border-radius: 90px;")
        self.frameUserPhoto.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameUserPhoto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameUserPhoto.setLineWidth(27)

        #Photo label
        self.labelPhoto = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelPhoto.setGeometry(QtCore.QRect(30, 40, 120, 120))
        self.labelPhoto.setStyleSheet("background-color: rgba(0,0,0,0%)");

        self.buttonsLeftArrow = QtWidgets.QPushButton(self.frameGreyHeader2)
        self.buttonsLeftArrow.setGeometry(QtCore.QRect(0, 0, 61, 51))
        self.buttonsLeftArrow.setFlat(True)
        self.buttonsLeftArrow.setText("<")

        self.buttonRightArrow = QtWidgets.QPushButton(self.frameGreyHeader2)
        self.buttonRightArrow.setGeometry(QtCore.QRect(950, 0, 61, 51))
        self.buttonRightArrow.setFlat(True)
        self.buttonRightArrow.setText(">")

        #set buttons
        self.buttonProfile = QtWidgets.QPushButton(self.frameWhiteHeader)
        self.buttonProfile.setGeometry(QtCore.QRect(0, 0, 85, 51))
        self.buttonProfile.setStyleSheet("font: 75 12pt \"Lato\";")
        self.buttonProfile.setFlat(True)
        self.buttonProfile.clicked.connect(self.openProfileWindow)
        self.buttonProfile.setText("       Profile |    ")

        self.buttonDiary = QtWidgets.QPushButton(self.frameWhiteHeader)
        self.buttonDiary.setGeometry(QtCore.QRect(88, 0, 90, 51))
        self.buttonDiary.setStyleSheet("font: 75 12pt \"Lato\";")
        self.buttonDiary.setFlat(True)
        self.buttonDiary.clicked.connect(self.openDiaryWindow)
        self.buttonDiary.setText("Diary |       ")

        self.buttonPlans = QtWidgets.QPushButton(self.frameWhiteHeader)
        self.buttonPlans.setGeometry(QtCore.QRect(145, 0, 85, 51))
        self.buttonPlans.setStyleSheet("font: 75 12pt \"Lato\";")
        self.buttonPlans.setFlat(True)
        self.buttonPlans.clicked.connect(self.openPlansWindow)
        self.buttonPlans.setText("        Plans |      ")

        self.buttonProgress = QtWidgets.QPushButton(self.frameWhiteHeader)
        self.buttonProgress.setGeometry(QtCore.QRect(230, 0, 100, 51))
        self.buttonProgress.setStyleSheet("font: 75 12pt \"Lato\";")
        self.buttonProgress.setFlat(True)
        self.buttonProgress.setText("    Progress |   ")

        self.buttonNutrition = QtWidgets.QPushButton(self.frameWhiteHeader)
        self.buttonNutrition.setGeometry(QtCore.QRect(330, 0, 100, 51))
        self.buttonNutrition.setStyleSheet("font: 75 12pt \"Lato\";")
        self.buttonNutrition.setFlat(True)
        self.buttonNutrition.clicked.connect(self.openNutritionWindow)
        self.buttonNutrition.setText("     Nutrition |  ")

        self.signOut = QtWidgets.QPushButton(self.frameWhiteHeader)
        self.signOut.setGeometry(QtCore.QRect(1050, 0, 110, 51))
        self.signOut.setStyleSheet("font: 75 12pt \"Lato\";")
        self.signOut.setFlat(True)
        self.signOut.setText("      Sign Out")

        #Update photo button
        self.buttonUpdatePhoto = QtWidgets.QPushButton(self.frameGreyBackground)
        self.buttonUpdatePhoto.setGeometry(QtCore.QRect(90, 160, 60, 20))
        self.buttonUpdatePhoto.setStyleSheet("background-color: rgb(85, 170, 255);\n""\n""font:  10pt \"SourceSansPro\";\n""color: rgb(255, 255, 255);")
        self.buttonUpdatePhoto.setText("Update")
        self.buttonUpdatePhoto.clicked.connect(self.AddImage)

        self.buttonAddWeight = QtWidgets.QPushButton(self.progress_2)
        self.buttonAddWeight.setGeometry(QtCore.QRect(800, 475, 150, 20))
        self.buttonAddWeight.setStyleSheet("background-color: rgb(85, 170, 255);\n""\n""font:  10pt \"SourceSansPro\";\n""color: rgb(255, 255, 255);")
        self.buttonAddWeight.clicked.connect(self.openWindowWeight)
        self.buttonAddWeight.setText("Update Current Weight")

        # display current weight in progress window
        self.buttonDisplayCurrentWeight = QtWidgets.QPushButton(self.progress_2)
        self.buttonDisplayCurrentWeight.setGeometry(QtCore.QRect(800, 450, 150, 20))
        self.buttonDisplayCurrentWeight.setStyleSheet("background-color: rgb(85, 170, 255);\n""\n""font:  10pt \"SourceSansPro\";\n""color: rgb(255, 255, 255);")
        self.buttonDisplayCurrentWeight.clicked.connect(self.loadCurrentWeight)
        self.buttonDisplayCurrentWeight.setText("Display Current Weight")

        #BMI BUTTON
        #self.buttonBMI = QtWidgets.QPushButton(self.progress_2)
      #  self.buttonBMI.setGeometry(QtCore.QRect(300, 325, 120, 20))
      #  self.buttonBMI.setStyleSheet("background-color: rgb(85, 170, 255);\n""\n""font:  10pt \"SourceSansPro\";\n""color: rgb(255, 255, 255);")
      #  self.buttonBMI.clicked.connect(self.loadAddBMI)
      #  self.buttonBMI.setText("Update your BMI")

        #BMI BUTTON
        self.buttonBMI = QtWidgets.QPushButton(self.progress_2)
        self.buttonBMI.setGeometry(QtCore.QRect(300, 330, 150, 20))
        self.buttonBMI.setStyleSheet("background-color: rgb(85, 170, 255);\n""\n""font:  10pt \"SourceSansPro\";\n""color: rgb(255, 255, 255);")
        self.buttonBMI.clicked.connect(self.loadAddBMI)
        self.buttonBMI.setText("Calculate BMI")

        #display current weight in progress window
        self.buttonShowWeight = QtWidgets.QPushButton(self.progress_2)
        self.buttonShowWeight.setGeometry(QtCore.QRect(800, 330, 150, 20))
        self.buttonShowWeight.setStyleSheet("background-color: rgb(85, 170, 255);\n""\n""font:  10pt \"SourceSansPro\";\n""color: rgb(255, 255, 255);")
        self.buttonShowWeight.clicked.connect(self.loadStartingWeight)
        self.buttonShowWeight.setText("Display Start Weight")

        #open weight progress window
        self.buttonShowWeightProgress = QtWidgets.QPushButton(self.progress_2)
        self.buttonShowWeightProgress.setGeometry(QtCore.QRect(970, 455, 150, 20))
        self.buttonShowWeightProgress.setStyleSheet("background-color: rgb(85, 170, 255);\n""\n""font:  10pt \"SourceSansPro\";\n""color: rgb(255, 255, 255);")
        self.buttonShowWeightProgress.clicked.connect(self.openWeightChanges)
        self.buttonShowWeightProgress.setText("show weight changes")

        #label to show total calories
        self.labelCaloriesFromDB = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelCaloriesFromDB.setGeometry(QtCore.QRect(40, 290, 91, 41))
        self.labelCaloriesFromDB.setStyleSheet("font: 75 12pt \"Lato\";" "color: rgb(255, 255, 255);""""background-color: transparent;""")
        caloriesData = SQLStatements.getTotalCalories(self.userID)
        self.labelCaloriesFromDB.setText(caloriesData)

        self.labelStepsFromDB = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelStepsFromDB.setGeometry(QtCore.QRect(30, 370, 91, 41))

        self.labelWaterFromDB = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelWaterFromDB.setGeometry(QtCore.QRect(40, 460, 91, 41))

        #label to show join date
        self.labelJoinDateFromDB = QtWidgets.QLabel(self.frameGreyBackground)
        self.labelJoinDateFromDB.setGeometry(QtCore.QRect(100, 196, 91, 41))
        self.labelJoinDateFromDB.setStyleSheet("font: 75 12pt \"Lato\";" "color: rgb(255, 255, 255);""""background-color: transparent;""")

        #find join date of user
        Joindate=SQLStatements.getJoinDate(self.userID)

        Joindate = str(Joindate)
        Joindate = (Joindate.replace("[",""))
        Joindate = (Joindate.replace("]", ""))
        Joindate = (Joindate.replace("(", ""))
        Joindate = (Joindate.replace(")", ""))
        Joindate = (Joindate.replace("'", ""))
        Joindate = (Joindate.replace(",", ""))

        self.labelJoinDateFromDB.setText(Joindate)

        self.showImage()
        self.loadCurrentWeight()
        self.loadStartingWeight()
        self.loadBmi()

    def AddImage(self):
       
        fileName = QtWidgets.QFileDialog.getOpenFileName()
        path = fileName[0]

        with open(path, "rb") as f:
            data = f.read()

        SQLStatements.AddImage(data,self.userID)
        self.showImage()
  
    def showImage(self):
        image = SQLStatements.showImage(self.userID)

        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image, 'jpg')
        pixmap5 = pixmap.scaled(120, 120)

        self.labelPhoto.setPixmap(pixmap5)


    #open diary
    def openDiaryWindow(self):
         
        self.window = QtWidgets.QMainWindow()
        self.ui = diary.Ui_Diary(self.userID)
        self.ui.setupUi(self.window)
        self.window.show()

    def openPlansWindow(self):
         
        self.window = QtWidgets.QMainWindow()
        self.ui = Plans.Ui_Plans()
        self.ui.setupUi(self.window)
        self.window.show()

    def openNutritionWindow(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Nutrition.Ui_Nutrition(self.userID)
            self.ui.setupUi(self.window)
            self.window.show()
        except Exception as e:
            print(e)

    def openWeightChanges(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = lineGraph.GraphWindow(self.userID)
            self.ui.setupUi(self.window)
            self.window.show()
        except Exception as e:
            print(e)

    def openProfileWindow(self):
         
        self.window = QtWidgets.QMainWindow()
        self.ui = Profile.Ui_Profile()
        self.ui.setupUi(self.window)
        self.window.show()

    #open plans
    def openPlansWindow(self):
         
        self.window = QtWidgets.QMainWindow()
        self.ui = Plans.Ui_Plans()
        self.ui.setupUi(self.window)
        self.window.show()
        
    #open login
    def openLoginWindow(self):
    
        self.window=QtWidgets.QMainWindow()
        self.ui = login.Ui_LoginWindow()
        self.ui.setupUi(self.window)
        self.window.show()

  #Adding BMI GOES HERE
    def loadAddBMI(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = bmiCalculator.Ui_MainWindow(self.userID)
            self.ui.setupUi(self.window)
            self.window.show()
        except Exception as e:
            print (e)
    #show starting weight in window
    def loadStartingWeight(self):
            
        startingweight = SQLStatements.getStartingWeight(self.userID)
        self.labelStartingWeight.setText(str(startingweight))

    def openWindowWeight(self):
        self.ui = AddWeightInformation(self.userID)
        self.ui.show()



    def loadCurrentWeight(self):
        currentweight = SQLStatements.getCurrentWeight(self.userID)
        self.labelCurrentWeight.setText(str(currentweight))


        if (SQLStatements.usersStartingweightValidation(self.userID) == False):
            startingweight = SQLStatements.getStartingWeight(self.userID)
            print(startingweight)
            SQLStatements.addWeightChange(self.userID, startingweight)

    def loadBmi(self):
        bmi = SQLStatements.getBmi(self.userID)
        bmi = str(bmi)
        self.BMIValue.setText(bmi)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    progress = QtWidgets.QMainWindow()
    ui = Ui_progress()
    ui.setupUi(progress)
    progress.show()
    sys.exit(app.exec_())


