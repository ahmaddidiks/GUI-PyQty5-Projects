import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtSerialPort, QtCore
from PyQt5.QtWidgets import QDialog, QApplication

class mainApp(QDialog):
    def __init__(self):
        super(mainApp, self).__init__()
        loadUi("/home/didik/GUI-PyQty5-Projects/Serial Arduino LED Control V3/serialV3.ui", self)
        #self.setWindowTitle("HELLO!")
        self.sendON = '1'
        self.sendOFF = '0'
        self.switch_btn.clicked.connect(self.switchButton)
        self.connect_btn.clicked.connect(self.on_toggled)

        self.serial = QtSerialPort.QSerialPort(
            '/dev/ttyUSB0',
            baudRate=QtSerialPort.QSerialPort.Baud9600,
        )

    @QtCore.pyqtSlot(bool)
    def switchButton(self, checked):
        if(self.serial.isOpen()):
            if checked:
                self.label.setText("LED OFF")
                self.serial.write(self.sendOFF.encode())
                self.switch_btn.setText("Turn ON LED!")
            else:
                self.label.setText("LED ON")
                self.serial.write(self.sendON.encode())
                self.switch_btn.setText("Turn OFF LED!")
        else:
            self.label.setText("Disconnected")           

    @QtCore.pyqtSlot(bool)
    def on_toggled(self, checked):
         
        #self.connect_btn.setText("Disconnect" if checked else "Connect")
        if checked:
            if not self.serial.isOpen():
                if not self.serial.open(QtCore.QIODevice.ReadWrite):
                    self.connect_btn.setChecked(False)
        else:
            self.serial.close()
            self.label.setText("Disconnected") 
        if checked and self.serial.isOpen():
            self.label.setText("Connected")
            self.connect_btn.setText("Disconnect!")
            self.switch_btn.setText("Turn ON LED!")
        else:
            self.connect_btn.setText("Connect!")
            self.switch_btn.setText("Connect LED first!")

#main


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.setFixedWidth(240)
widget.setFixedHeight(180)

window = mainApp()
widget.addWidget(window)
widget.setFixedWidth(240)
widget.setFixedHeight(180)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")