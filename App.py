import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.uic import loadUi

from Passport import Passport

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_window.ui", self)
        self.rxTelemetryBrowse.clicked.connect(self.browseRXTelemetry)
        self.a6000TelemetryBrowse.clicked.connect(self.browseA6000Telemetry)
        self.createPassportButton.clicked.connect(self.createPassports)
    
    def browseRXTelemetry(self):
        fname = QFileDialog.getOpenFileName(self, 'Выберите файл телеметрии для камеры Sony RXI RII', '/', 'Текстовые файлы (*.txt)')
        self.rxTelemetryFilename.setText(fname[0])
        self.rxTelemetryFile = fname[0]
    
    def browseA6000Telemetry(self):
        fname = QFileDialog.getOpenFileName(self, 'Выберите файл телеметрии для камеры Sony A6000', '/', 'Текстовые файлы (*.txt)')
        self.a6000TelemetryFilename.setText(fname[0])
        self.a6000TelemetryFile = fname[0]
    
    def createPassports(self):
        rxPassport = Passport(self.rxTelemetryFile, 'Селитренное городище', '3')
        #a6000Passport = Passport(self.a6000TelemetryFile, 'Селитренное городище', '3')
        rxPassport.writeInfo('CUSTOMER_COMPANY', 'survey.date', '14:00', 
            '18:00', 'RELIEF_TYPE', '1', 15, 'ROUTES_ORIENTATION', 
            80, 60, 300, 4, 'camera', 'RECEIVER', 'UAV_MODEL')
        rxPassport.closeFile(('REALIZER_POSITION', 'REALIZER_FIO'), ('CONTROLER_POSITION', 'CONTROLER_FIO'))

app = QApplication(sys.argv)
mainWindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
sys.exit(app.exec_())
