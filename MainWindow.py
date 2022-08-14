from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.uic import loadUi

from Passport import Passport
from constants import UAV
from Survey import Survey
from Photo import Photo
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_window.ui", self)
        
        self.rxCheckBox.stateChanged.connect(self.rxChecked)
        self.A6CheckBox.stateChanged.connect(self.a6Checked)

        self.rxTelemetryBrowse.clicked.connect(self.browseRXTelemetry)
        self.a6000TelemetryBrowse.clicked.connect(self.browseA6000Telemetry)
        self.rxMarksBrowse.clicked.connect(self.browseRXMarks)
        self.a6000MarksBrowse.clicked.connect(self.browseA6000Marks)
        self.rinexBrowse.clicked.connect(self.browseRINEX)

        self.createPassportButton.clicked.connect(self.createPassports)
    
    def rxChecked(self):
        if self.rxCheckBox.isChecked():
            self.rxTelemetryFilename.setEnabled(True)
            self.rxTelemetryBrowse.setEnabled(True)
            self.rxMarksFilename.setEnabled(True)
            self.rxMarksBrowse.setEnabled(True)
            self.a6000MarksFilename.setEnabled(True)
            self.a6000MarksBrowse.setEnabled(True)
            self.rxGPS.setEnabled(True)
        else:
            self.rxTelemetryFilename.setEnabled(False)
            self.rxTelemetryBrowse.setEnabled(False)
            self.rxMarksFilename.setEnabled(False)
            self.rxMarksBrowse.setEnabled(False)
            self.a6000MarksFilename.setEnabled(False)
            self.a6000MarksBrowse.setEnabled(False)
            self.rxGPS.setEnabled(False)
    
    def a6Checked(self):
        if self.A6CheckBox.isChecked():
            self.a6000TelemetryFilename.setEnabled(True)
            self.a6000TelemetryBrowse.setEnabled(True)
            self.a6000MarksFilename.setEnabled(True)
            self.a6000MarksBrowse.setEnabled(True)
            self.rxMarksFilename.setEnabled(True)
            self.rxMarksBrowse.setEnabled(True)
            self.a6GPS.setEnabled(True)
        else:
            self.a6000TelemetryFilename.setEnabled(False)
            self.a6000TelemetryBrowse.setEnabled(False)
            self.a6000MarksFilename.setEnabled(False)
            self.a6000MarksBrowse.setEnabled(False)
            self.rxMarksFilename.setEnabled(False)
            self.rxMarksBrowse.setEnabled(False)
            self.a6GPS.setEnabled(False)
    
    def browseRXTelemetry(self):
        self.rxTelemetryFile = QFileDialog.getOpenFileName(self, 'Телеметрия для камеры Sony RXI RII', '/', 'Текстовые файлы (*.txt)')
        self.rxTelemetryFilename.setText(self.rxTelemetryFile[0])
    
    def browseA6000Telemetry(self):
        self.a6000TelemetryFile = QFileDialog.getOpenFileName(self, 'Телеметрия для камеры Sony A6000', '/', 'Текстовые файлы (*.txt)')
        self.a6000TelemetryFilename.setText(self.a6000TelemetryFile[0])
    
    def browseRXMarks(self):
        self.rxMarksFile = QFileDialog.getOpenFileName(self, 'Метки времени для камеры Sony RXI RII', '/', 'Текстовые файлы (*.marks)')
        self.rxMarksFilename.setText(self.rxMarksFile[0])
    
    def browseA6000Marks(self):
        self.a6000MarksFile = QFileDialog.getOpenFileName(self, 'Метки времени для камеры Sony A6000', '/', 'Текстовые файлы (*.marks)')
        self.a6000MarksFilename.setText(self.a6000MarksFile[0])
    
    def browseRINEX(self):
        self.rinexFile = QFileDialog.getOpenFileName(self, 'Бортовые ГНСС-наблюдения', '/', 'RINEX (*.obs *.**o)')
        self.rinexFilename.setText(self.rinexFile[0])
    
    def createPassports(self):
        if self.rxCheckBox.isChecked():
            survey = Survey(self.rxTelemetryFile[0], self.altitude.text())
            survey.extractDatetimeFromTelemetry()
            groundFrameSize = survey.calcGroundFrameSize(UAV['CAMERAS'][1])
            photoPointsRawArray = survey.createPhotoPointsArray()
            for point in photoPointsRawArray:
                dateTimeArray = point[7].split(' ')
                dateArray = dateTimeArray[0].split('.')
                timeArray = dateTimeArray[1].split(':')
                secondsArray = timeArray[2].split('.')
                survey.addPhotos(Photo(point[0],
                                    float(point[1]),
                                    float(point[2]),
                                    float(point[3]),
                                    float(point[8][:-1]),
                                    float(point[4]),
                                    float(point[5]),
                                    float(point[6]),
                                    datetime(int(dateArray[0]), int(dateArray[1]), int(dateArray[2]), 
                                    int(timeArray[0]), int(timeArray[1]), int(secondsArray[0]), int(secondsArray[1]))
                ))
            survey.splitByRoutes()
            rxPassport = Passport(self.rxTelemetryFile[0], self.objName.text(), self.surveySite.text())
            rxPassport.writeInfo(self.customer.text(), survey.date, survey.time['startTime'], 
                survey.time['endTime'], 'RELIEF_TYPE', '1', 15, 'ROUTES_ORIENTATION', 
                80, 60, 300, 4, 'camera', 'RECEIVER', 'UAV_MODEL')
            rxPassport.closeFile((self.realizerPosition.text(), self.realizerName.text()), (self.controllerPosition(), self.controllerName.text()))
        if self.a6000TelemetryFile:
            a6000Passport = Passport(self.a6000TelemetryFile, self.objName.text(), self.surveySite.text())
            a6000Passport.writeInfo(self.customer.text(), 'survey.date', '14:00', 
                '18:00', 'RELIEF_TYPE', '1', 15, 'ROUTES_ORIENTATION', 
                80, 60, 300, 4, 'camera', 'RECEIVER', 'UAV_MODEL')
            a6000Passport.closeFile((self.realizerPosition.text(), self.realizerName.text()), (self.controllerPosition(), self.controllerName.text()))