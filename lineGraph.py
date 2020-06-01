from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import Qt
import SQLStatements



class GraphWindow(object):

    def __init__(self, userID):
        self.userID = userID

    def setupUi(self, progress):
        # set window title
        progress.setWindowTitle("Nutrition")
        progress.resize(1188, 730)
        progress.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.267, y1:0.642, x2:0.778, y2:0.323864, stop:0 rgba(0, 150, 136, 255), stop:1 rgba(63, 81, 181, 255));\n""")
        self.progress_2 = QtWidgets.QWidget(progress)
        QtCore.QMetaObject.connectSlotsByName(progress)
        progress.setCentralWidget(self.create_piechart())

    def create_piechart(self):
        series = QLineSeries()

        weights = SQLStatements.getallWeightChanges(self.userID)
        print(weights)



        weights = str(weights)
        weights = weights.replace("(", "")
        weights = weights.replace(")", "")
        weights = weights.replace(",", "")
        weights = weights.replace("[", "")
        weights = weights.replace("]", "")

        weightsTable = weights.split()

        print(weightsTable)

        count = 0
        for x in weightsTable:
            x = int(float(x))
            print(x)
            series.append(count, x)
            count=count+2

        chart = QChart()

        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Weight Change over time")
        chart.setTheme(QChart.ChartThemeBlueCerulean)
        chart.setBackgroundVisible(False)


        #Title Font size
        font = QFont("Sans Serif", )
        font.setPixelSize(18)
        chart.setTitleFont(font)

        # X Axis Settings
        axisX = QValueAxis()
        axisX.setTitleText("Time")

        # Y Axis Settings
        axisY = QValueAxis()
        axisY.setTitleText("Weight (KG)")

        # Customize axis label font
        Lfont = QFont("Sans Serif")
        Lfont.setPixelSize(16)
        axisX.setLabelsFont(Lfont)
        axisY.setLabelsFont(Lfont)

        #add Axis
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)



        return chartview


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    progress = QtWidgets.QMainWindow()
    ui = GraphWindow()
    ui.setupUi(progress)
    progress.show()
    sys.exit(app.exec_())
