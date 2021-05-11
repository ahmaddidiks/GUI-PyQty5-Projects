from PyQt5 import QtWidgets, QtSerialPort, uic
from serial import Serial
import sys, struct, csv


class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        uic.loadUi('/home/didik/GUI-PyQty5-Projects/Servo Control/MainForm.ui', self)

        for info in QtSerialPort.QSerialPortInfo.availablePorts():
            self.com_box.addItem(info.portName())

        self.arduinoSerial = None

        self.connect_btn.clicked.connect(self.onButtonConnect)
        self.save_btn.clicked.connect(self.onButtonSave)
        self.servo1_slider.valueChanged.connect(self.servo1_changed)
        self.servo2_slider.valueChanged.connect(self.servo2_changed)
        self.servo3_slider.valueChanged.connect(self.servo3_changed)
        self.servo4_slider.valueChanged.connect(self.servo4_changed)
        self.servo5_slider.valueChanged.connect(self.servo5_changed)
        self.servo6_slider.valueChanged.connect(self.servo6_changed)
        self.servo7_slider.valueChanged.connect(self.servo7_changed)
        self.servo8_slider.valueChanged.connect(self.servo8_changed)
        self.servo9_slider.valueChanged.connect(self.servo9_changed)
        self.servo10_slider.valueChanged.connect(self.servo10_changed)
        self.servo11_slider.valueChanged.connect(self.servo11_changed)
        self.servo12_slider.valueChanged.connect(self.servo12_changed)

        self.show()

    def onButtonConnect(self):
        if self.connect_btn.text() == "Connect":
            try:
                self.arduinoSerial = Serial(self.com_box.currentText(), int(self.baud_box.currentText()))
                self.connect_btn.setText("Disconnect")
                self.com_box.setEnabled(False)
                self.baud_box.setEnabled(False)
            except Exception as ex:
                self.showErrorDialog(str(ex))
        else:
            if self.arduinoSerial != None: self.arduinoSerial.close()
            self.connect_btn.setText("Connect")
            self.com_box.setEnabled(True)
            self.baud_box.setEnabled(True)

    def onButtonSave(self):
        option = QtWidgets.QFileDialog.Options
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "", "CSV File (*.csv)")
        if fileName:
            with open(fileName, mode="w", newline='') as csvFile:
                csvWriter = csv.writer(csvFile, dialect='excel')
                csvWriter.writerow(["Servo ID", "Angle", "Offset"])
                csvWriter.writerow(["1", self.servo1_slider.value(), self.servo1_offset.text()])
                csvWriter.writerow(["2", self.servo2_slider.value(), self.servo2_offset.text()])
                csvWriter.writerow(["3", self.servo3_slider.value(), self.servo3_offset.text()])
                csvWriter.writerow(["4", self.servo4_slider.value(), self.servo4_offset.text()])
                csvWriter.writerow(["5", self.servo5_slider.value(), self.servo5_offset.text()])
                csvWriter.writerow(["6", self.servo6_slider.value(), self.servo6_offset.text()])
                csvWriter.writerow(["7", self.servo7_slider.value(), self.servo7_offset.text()])
                csvWriter.writerow(["8", self.servo8_slider.value(), self.servo8_offset.text()])
                csvWriter.writerow(["9", self.servo9_slider.value(), self.servo9_offset.text()])
                csvWriter.writerow(["10", self.servo10_slider.value(), self.servo10_offset.text()])
                csvWriter.writerow(["11", self.servo11_slider.value(), self.servo11_offset.text()])
                csvWriter.writerow(["12", self.servo12_slider.value(), self.servo12_offset.text()])

    def servo1_changed(self):
        data = int(self.servo1_slider.value()) + int(self.servo1_offset.text())
        self.sendData(1, data)

    def servo2_changed(self):
        data = int(self.servo2_slider.value()) + int(self.servo2_offset.text())
        self.sendData(2, data)
        
    def servo3_changed(self):
        data = int(self.servo3_slider.value()) + int(self.servo3_offset.text())
        self.sendData(3, data)

    def servo4_changed(self):
        data = int(self.servo4_slider.value()) + int(self.servo4_offset.text())
        self.sendData(4, data)

    def servo5_changed(self):
        data = int(self.servo5_slider.value()) + int(self.servo5_offset.text())
        self.sendData(5, data)

    def servo6_changed(self):
        data = int(self.servo6_slider.value()) + int(self.servo6_offset.text())
        self.sendData(6, data)

    def servo7_changed(self):
        data = int(self.servo7_slider.value()) + int(self.servo7_offset.text())
        self.sendData(7, data)

    def servo8_changed(self):
        data = int(self.servo8_slider.value()) + int(self.servo8_offset.text())
        self.sendData(8, data)
        
    def servo9_changed(self):
        data = int(self.servo9_slider.value()) + int(self.servo9_offset.text())
        self.sendData(9, data)

    def servo10_changed(self):
        data = int(self.servo10_slider.value()) + int(self.servo10_offset.text())
        self.sendData(10, data)

    def servo11_changed(self):
        data = int(self.servo11_slider.value()) + int(self.servo11_offset.text())
        self.sendData(11, data)

    def servo12_changed(self):
        data = int(self.servo12_slider.value()) + int(self.servo12_offset.text())
        self.sendData(12, data)

    def showErrorDialog(self, text):
        QtWidgets.QMessageBox.critical(self, "Error", text)

    def sendData(self, servoId, value):
        if self.arduinoSerial == None: return
        if self.arduinoSerial.is_open:
            data = struct.pack("hh", servoId, value)
            self.arduinoSerial.write(b'$')
            self.arduinoSerial.write(data)


app = QtWidgets.QApplication(sys.argv)
window = MainUI()
app.exec_()
