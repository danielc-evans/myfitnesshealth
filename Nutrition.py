from datetime import date

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import Qt

import SQLStatements




class Ui_Nutrition(object):

        def __init__(self, userID):
            self.userID = userID

        def setupUi(self, progress):
            #set window title
            progress.setWindowTitle("Nutrition")
            progress.resize(1188, 730)
            progress.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.267, y1:0.642, x2:0.778, y2:0.323864, stop:0 rgba(0, 150, 136, 255), stop:1 rgba(63, 81, 181, 255));\n""")
            self.progress_2 = QtWidgets.QWidget(progress)
            QtCore.QMetaObject.connectSlotsByName(progress)
            progress.setCentralWidget(self.create_piechart())


        def create_piechart(self):

                Date = date.today()

                breakfastData = SQLStatements.getTotalBreakfastCalories(self.userID, Date)
                breakfastData = str(breakfastData)
                breakfastData = (breakfastData.replace("[", ""))
                breakfastData = (breakfastData.replace("]", ""))
                breakfastData = (breakfastData.replace("(", ""))
                breakfastData = (breakfastData.replace(")", ""))
                breakfastData = (breakfastData.replace(",", ""))
                breakfastData = int(breakfastData)

                lunchData = SQLStatements.getTotalLunchCalories(self.userID, Date)
                lunchData = str(lunchData)
                lunchData = (lunchData.replace("[", ""))
                lunchData = (lunchData.replace("]", ""))
                lunchData = (lunchData.replace("(", ""))
                lunchData = (lunchData.replace(")", ""))
                lunchData = (lunchData.replace(",", ""))
                lunchData = int(lunchData)

                dinnerData = SQLStatements.getTotalDinnerCalories(self.userID, Date)
                dinnerData = str(dinnerData)
                dinnerData = (dinnerData.replace("[", ""))
                dinnerData = (dinnerData.replace("]", ""))
                dinnerData = (dinnerData.replace("(", ""))
                dinnerData = (dinnerData.replace(")", ""))
                dinnerData = (dinnerData.replace(",", ""))
                dinnerData = int(dinnerData)

                snackData = SQLStatements.getTotalSnacksCalories(self.userID, Date)
                snackData = str(snackData)
                snackData = (snackData.replace("[", ""))
                snackData = (snackData.replace("]", ""))
                snackData = (snackData.replace("(", ""))
                snackData = (snackData.replace(")", ""))
                snackData = (snackData.replace(",", ""))
                snackData = int(snackData)

                series = QPieSeries()
                series.append("Breakfast calories", breakfastData)
                series.append("Lunch calories", lunchData)
                series.append("Dinner calories", dinnerData)
                series.append("Snack calories", snackData)


                labelFont = QFont("Sans Serif", )
                labelFont.setPixelSize(16)
        
                slice = QPieSlice()
                slice.setLabelFont(labelFont)
                slice = series.slices()[0]
                slice.setExploded(True)
                slice.setLabelVisible(True)
                slice.setPen(QPen(Qt.green, 2))
                slice.setBrush(Qt.green)

                slice = QPieSlice()
                slice.setLabelFont(labelFont)
                slice = series.slices()[1]
                slice.setExploded(True)
                slice.setLabelVisible(True)
                slice.setPen(QPen(Qt.white, 2))
                slice.setBrush(Qt.white)

                slice = QPieSlice()
                slice.setLabelFont(labelFont)
                slice = series.slices()[2]
                slice.setExploded(True)
                slice.setLabelVisible(True)
                slice.setPen(QPen(Qt.yellow, 2))
                slice.setBrush(Qt.yellow)

                slice = QPieSlice()
                slice.setLabelFont(labelFont)
                slice = series.slices()[3]
                slice.setExploded(True)
                slice.setLabelVisible(True)
                slice.setPen(QPen(Qt.yellow, 2))
                slice.setBrush(Qt.yellow)

                chart = QChart()
                chart.legend().hide()
                chart.addSeries(series)
                chart.createDefaultAxes()
                chart.setAnimationOptions(QChart.SeriesAnimations)
                chart.setTitle("Daily Calories")
                chart.setTheme(QChart.ChartThemeBlueCerulean)

                chart.setBackgroundVisible(False)
                # Title Font size
                font = QFont("Sans Serif", )
                font.setPixelSize(18)
                chart.setTitleFont(font)



                chart.legend().setVisible(True)
                chart.legend().setAlignment(Qt.AlignBottom)
                chartview = QChartView(chart)
                chartview.setRenderHint(QPainter.Antialiasing)
                return chartview



            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    progress = QtWidgets.QMainWindow()
    ui = Ui_Nutrition()
    ui.setupUi(progress)
    progress.show()
    sys.exit(app.exec_())
