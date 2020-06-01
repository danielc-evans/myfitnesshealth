import sys
from PyQt5.QtWidgets import QMessageBox
import ui
from PyQt5 import QtWidgets
import SQLStatements


class formExercise(QtWidgets.QMainWindow):

    def __init__(self, userID):
        super().__init__()

        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.userID = userID
        # Label content
        self.ui.labelFood.setText("Exercise")
        self.ui.labelCalories.setText("Calories Lost")
        self.ui.labelGrams.hide()
        self.ui.lineEditGrams.hide()

        # Add button which is connected to the 'addToDb' function
        self.ui.addButton.clicked.connect(self.addToDb)
        self.ui.addButton.clicked.connect(self.close)

        self.show()

    def addToDb(self):
        try:
            # Adding variable names to the text boxes on add information windows
            Exercise = self.ui.lineEditFood.text()
            Calories = self.ui.lineEditCalories.text()
            # Stores the user ID as a variable and removes the excess string
            UserID = self.userID
            UserID = str(UserID)
            UserID = (UserID.replace("(", ""))
            UserID = (UserID.replace(")", ""))
            UserID = (UserID.replace(",", ""))
            # Validation Check.
            if (SQLStatements.addExercise(Exercise, Calories, UserID) == 'True'):
                QMessageBox.about(QMessageBox(), 'Success', 'added to the database.')
            else:
                QMessageBox.warning(QMessageBox(), 'Error', 'Could not be added')

        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = formExercise()
    sys.exit(app.exec_())
