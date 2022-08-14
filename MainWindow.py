from os import path

from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.uic import loadUi
from ErrorMessage import ErrorMessage
from calc_offsets import calc_offsets

from catalogToArray import catalogToArray
from offsets import offsets
from splitRMS import splitRMS
from transform import transformCoord


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,  self).__init__()
        loadUi("dialog.ui", self)
        self.chooseTelemetryFilePath.clicked.connect(self.browseTelemetry)
        self.chooseCentersFilePath.clicked.connect(self.browseCenters)
        for camera in offsets:
            self.cameraComboBox.addItem(camera)
        self.checkBox.stateChanged.connect(self.checked)
        crs_list = ['МСК-30 (зона 1)', 'МСК-30 (зона 2)', 'UTM (зона 38)', 'UTM (зона 39)']
        for crs in crs_list:
            self.sourceCRSComboBox.addItem(crs)
            self.targetCRSComboBox.addItem(crs)
        self.startButton.clicked.connect(self.startCalculation)
    
    def browseTelemetry(self):
        self.telemetryFilename = QFileDialog.getOpenFileName(self, 
            'Выберите файл телеметрии', '/', 'Текстовые файлы (*.txt)')
        print(self.telemetryFilename)
        self.telemetryFilePath.setText(self.telemetryFilename[0])
    
    def browseCenters(self):
        self.centersFilename = QFileDialog.getOpenFileName(self, 
            'Выберите каталог координат центров фотографирования', 
            path.split(self.telemetryFilename[0])[0], 
            'Текстовые файлы (*.txt *.csv)')
        self.centersFilePath.setText(self.centersFilename[0])
    
    def checked(self):
        if self.checkBox.isChecked():
            self.sourceCRSComboBox.setEnabled(True)
            self.targetCRSComboBox.setEnabled(True)
        else:
            self.sourceCRSComboBox.setEnabled(False)
            self.targetCRSComboBox.setEnabled(False)
    
    def startCalculation(self):
        self.startButton.setEnabled(False)
        centers = catalogToArray(self.centersFilename[0], ';', 
            ['name', 'nord', 'east', 'elev', 'time', 'rmsxy', 'rmsh'], 0)
        telemetry = catalogToArray(self.telemetryFilename[0], '\t', 
            ['name', 'nord', 'east', 'elevBaro', 'roll', 'pitch', 'yaw', 
             'time', 'elevGPS'], 6)
        if len(centers) == len(telemetry):
            for i in range(len(centers)):
                telemetry[i]['nord'] = centers[i]['nord']
                telemetry[i]['east'] = centers[i]['east']
                telemetry[i]['elev'] = centers[i]['elev']
                rms = splitRMS(centers[i]['rmsxy'])
                telemetry[i]['rmsx'] = rms
                telemetry[i]['rmsy'] = rms
                telemetry[i]['rmsh'] = centers[i]['rmsh']
                telemetry[i]['yaw'] = telemetry[i]['yaw']
                telemetry[i].pop('elevBaro')
                telemetry[i].pop('elevGPS')
                offCoords = calc_offsets(telemetry[i], offsets[str(self.cameraComboBox.currentText())])
                if self.checkBox.isChecked():
                    transformedCoords = transformCoord(offCoords[1], offCoords[0], self.sourceCRSComboBox.currentText(), self.targetCRSComboBox.currentText())
                    telemetry[i]['nord'] = transformedCoords[1]
                    telemetry[i]['east'] = transformedCoords[0]
                else:
                    telemetry[i]['nord'] = offCoords[0]
                    telemetry[i]['east'] = offCoords[1]
                telemetry[i]['elev'] = offCoords[2]
        else:
            print('Количество снимков в файлах не совпадает')
            self.errorMessage = ErrorMessage()
            self.errorMessage.show()
        
        with open(path.join(path.split(self.telemetryFilename[0])[0], 'telemetry_offsets.txt'), 'w') as result:
            result.write('\t'.join(telemetry[0].keys()) + '\n')
            for point in telemetry:
                array = []
                for item in point.values():
                    array.append(str(item))
                result.write('\t'.join(array) + '\n')
        
        self.startButton.setEnabled(True)
