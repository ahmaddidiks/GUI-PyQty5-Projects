import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtSerialPort, QtCore
from PyQt5.QtWidgets import QDialog, QApplication

class mainApp(QDialog):
    def __init__(self):
        super(mainApp, self).__init__()
        loadUi("/home/didik/GUI-PyQty5-Projects/Serial Arduino LED Control V2/serialV2.ui", self)
        #self.setWindowTitle("HELLO!")
        self.sendON = '1'
        self.sendOFF = '0'
        self.on_btn.clicked.connect(self.onButton)
        self.off_btn.clicked.connect(self.offButton)
        self.connect_btn.clicked.connect(self.on_toggled)

        self.serial = QtSerialPort.QSerialPort(
            '/dev/ttyUSB0',
            baudRate=QtSerialPort.QSerialPort.Baud9600,
        )

    def offButton(self):
        if(self.serial.isOpen()):
            self.label.setText("LED OFF")
            self.serial.write(self.sendOFF.encode())
        else:
            self.label.setText("Disconnected")    

    def onButton(self):
        #send 1 to serial
        #set LED ON display
        if(self.serial.isOpen()):
            self.label.setText("LED ON")
            self.serial.write(self.sendON.encode())
        else:
            self.label.setText("Disconnected")            
    
    @QtCore.pyqtSlot()
    def receive(self):
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode()
            text = text.rstrip('\r\n')
            self.output_te.append(text)

    @QtCore.pyqtSlot()
    def send(self):
        self.serial.write(self.message_le.text().encode())

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
        else:
            self.connect_btn.setText("Connect!")

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