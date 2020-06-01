
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import SQLStatements


class Ui_MainWindow(object):
    def __init__(self, userID):
        self.userID = userID

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 287)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.267, y1:0.642, x2:0.778, y2:0.323864, stop:0 rgba(0, 150, 136, 255), stop:1 rgba(63, 81, 181, 255));""")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("MainWindow")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -20, 391, 61))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelheight_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelheight_2.setGeometry(QtCore.QRect(240, 70, 81, 31))
        self.labelheight_2.setAutoFillBackground(False)
        self.labelheight_2.setStyleSheet("font: 15  \"Lato\";" "color: rgb(255, 255, 255);""""background-color: transparent;""")
        self.labelheight_2.setObjectName("labelheight_2")
        self.labelheight_3 = QtWidgets.QLabel(self.centralwidget)
        self.labelheight_3.setGeometry(QtCore.QRect(240, 130, 81, 31))
        self.labelheight_3.setAutoFillBackground(False)
        self.labelheight_3.setStyleSheet("font: 15  \"Lato\";" "color: rgb(255, 255, 255);""""background-color: transparent;""")
        self.labelheight_3.setObjectName("labelheight_3")

        self.labelTitle = QtWidgets.QLabel(self.frame)
        self.labelTitle.setGeometry(QtCore.QRect(20, 20, 341, 41))
        self.labelTitle.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.labelTitle.setObjectName("labelTitle")

        self.labelheight = QtWidgets.QLabel(self.centralwidget)
        self.labelheight.setGeometry(QtCore.QRect(60, 70, 81, 31))
        self.labelheight.setStyleSheet("font: 15  \"Lato\";" "color: rgb(255, 255, 255);""""background-color: transparent;""")
        self.labelheight.setObjectName("labelheight")

        self.labelweight = QtWidgets.QLabel(self.centralwidget)
        self.labelweight.setGeometry(QtCore.QRect(60, 130, 81, 31))
        self.labelweight.setStyleSheet("font: 15  \"Lato\";" "color: rgb(255, 255, 255);""""background-color: transparent;""")
        self.labelweight.setObjectName("labelweight")

        self.ButtonCalculate = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonCalculate.setGeometry(QtCore.QRect(140, 200, 101, 41))
        self.ButtonCalculate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ButtonCalculate.setObjectName("ButtonCalculate")

        self.lineEditHeight = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditHeight.setGeometry(QtCore.QRect(150, 77, 61, 20))
        self.lineEditHeight.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditHeight.setObjectName("lineEditHeight")

        self.lineEditWeight = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWeight.setGeometry(QtCore.QRect(150, 137, 61, 20))
        self.lineEditWeight.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditWeight.setObjectName("lineEditWeight")

        self.labelTitle.setText("Body Mass Index (BMI) Calculator:")
        self.labelheight.setText("Insert Height:")
        self.labelweight.setText("Insert Weight:")
        self.ButtonCalculate.setText("Calculate")
        self.labelheight_2.setText("inches")
        self.labelheight_3.setText("lbs")

        UsersWeight = SQLStatements.getWeight(self.userID)
        UsersHeight = SQLStatements.getHeight(self.userID)

        UsersWeight = (float(UsersWeight) * 2.2)
        UsersWeight = int(UsersWeight)
        UsersWeight = str(UsersWeight)

        UsersHeight = (float(UsersHeight) * 0.39)
        UsersHeight = int(UsersHeight)
        UsersHeight = str(UsersHeight)

        self.lineEditHeight.setText(UsersHeight)
        self.lineEditWeight.setText(UsersWeight)

        self.ButtonCalculate.clicked.connect(self.ValidationAndResult)



    def ValidationAndResult(self):
        try:

            if str(self.lineEditWeight.text()) =="" and str(self.lineEditHeight.text()) =="":
                QMessageBox.warning(QMessageBox(), 'Cannot Calculate!', "No data was detected. Please fill in the textbox.", QMessageBox.Ok)

            elif str(self.lineEditWeight.text()) =="" and str(self.lineEditHeight.text()) !="":
                QMessageBox.warning(QMessageBox(), 'Cannot Calculate!', "No value for weight was entered. Please enter weight.", QMessageBox.Ok)

            elif str(self.lineEditWeight.text()) =="" and str(self.lineEditHeight.text()) !="":
                QMessageBox.warning(QMessageBox(), 'Cannot Calculate!', "No value for weight was entered. Please enter Height ", QMessageBox.Ok)

            else:
                weight = float(int(self.lineEditWeight.text()) )
                height = float(int(self.lineEditHeight.text()) )

                result = weight / (height * height) * 703
                SQLStatements.changeBmi(result,self.userID)


                if ((result)) < 18.5: QMessageBox.information(QMessageBox(), 'Result', "Your BMI result is: " + str('%.2f' %(result)) + "\n Weight Category: Underweight", QMessageBox.Ok)


                elif ((result)) < 25 and ((result)) >= 18.5: QMessageBox.information(QMessageBox(), 'Result', "Your BMI result is: " + str('%.2f' %(result)) + "\n Weight Category: Healthy weight", QMessageBox.Ok)

                elif ((result)) < 30 and ((result)) >= 25: QMessageBox.information(QMessageBox(), 'Result', "Your BMI result is: " + str('%.2f' %(result)) + "\n Weight Category: Overweight", QMessageBox.Ok)

                else:
                    QMessageBox.information(QMessageBox(), 'Result', "Your BMI result is: " + str('%.2f' %(result)) + "\n Category: Obese", QMessageBox.Ok)

        except Exception as e:
            print(e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
