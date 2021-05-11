#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QFileDialog, QLabel, QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from datetime import datetime

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("/home/didik/GUI-PyQty5-Projects/santet/santetUI.ui", self)
        self.setWindowTitle("Santet V.01")
        self.lineEdit_atas_nama.textChanged.connect(self.create_atas_nama)
        self.lineEdit_nama_tujuan.textChanged.connect(self.create_nama_tujuan)
        self.lineEdit_alasan_santet.textChanged.connect(self.create_alasan_santet)
        self.checkBox.clicked.connect(self.set_durasi_santet)
        self.comboBox.activated[str].connect(self.set_jenis_santet)
        self.pushButton_mulai.clicked.connect(self.set_button_mulai)
        self.pushButton_berhenti.clicked.connect(self.set_button_berhenti)
        self.pushButton_foto.clicked.connect(self.set_foto)
        
        #initial varialbe
        self.jenis_santet = 'Muncul paku di perut'
        self.durasi_santet = 'NonPermanen'

    def create_atas_nama(self, text):
        self.atas_nama = text

    def create_nama_tujuan(self, text):
        self.nama_tujuan = text

    def create_alasan_santet(self, text):
        self.alasan_santet = text

    def set_jenis_santet(self, text):
        self.jenis_santet = text

    def set_durasi_santet(self, checked):
        if (checked):
            self.durasi_santet = 'Permanen'

        else:
           self.durasi_santet = 'NonPermanen'
    
    def set_button_mulai(self):
        
        try:
            self.content = f"Santet {self.durasi_santet} dengan atas nama {self.atas_nama} ditujukan kepada {self.nama_tujuan} dan jenis santet {self.jenis_santet} dengan alasan '{self.alasan_santet} berhasil dikirmkan, silahkan tunggu hasilnya"
            self.label_status.setText(self.content)
        except Exception as e:
            self.label_status.setText('Penuhi semua persyaratan di atas terlebih dahulu!')

    def set_button_berhenti(self):
        self.content = 'Santet sedang tidak berjalan, Simbah Dukun lagi istirahat'
        self.label_status.setText(self.content)

    def set_foto(self, file_name = None):
        if not file_name:
            file_name, _ = QFileDialog.getOpenFileName(self, 'Pilih Gambar', '/home/didik/Pictures', 'Images (*.png *.jpg *jpeg', options=QFileDialog.DontUseNativeDialog)
            #file_name, _ = QFileDialog.getOpenFileName(self, 'Pilih Gambar', QDir.currentPath(), 'Images (*.png *.jpg *jpeg', options=QFileDialog.DontUseNativeDialog)
            if not file_name:
                return
        self.label_foto.setScaledContents(True)
        self.label_foto.setPixmap(QPixmap(file_name))

app = QApplication(sys.argv)
window = MainUI()
window.setFixedHeight(480)
window.setFixedWidth(640)
window.show()
app.exec_()