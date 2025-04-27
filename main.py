import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QComboBox, QSpinBox,
    QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QMessageBox, QMenuBar, QAction
)
from PyQt5.QtCore import Qt

class TrackerBelajar(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tracker Belajar Harian - Yeni Septiani Putri F1D022027")
        self.setGeometry(100, 100, 500, 400)
        self.setupUI()

    def setupUI(self):
        # Label Nama dan NIM
        self.label_nama = QLabel("Nama: Yeni Septiani Putri")
        self.label_nim = QLabel("NIM: F1D022027")
        self.label_nama.setStyleSheet("font-weight: bold; color: navy;")
        self.label_nim.setStyleSheet("font-weight: bold; color: navy;")

        # Input Form
        self.input_kegiatan = QLineEdit()
        self.input_kegiatan.setPlaceholderText("Masukkan kegiatan belajar")

        self.combo_materi = QComboBox()
        self.combo_materi.addItems(["Matematika", "IPA", "Bahasa Indonesia", "Bahasa Inggris", "Sejarah"])

        self.spin_durasi = QSpinBox()
        self.spin_durasi.setRange(1, 10)
        self.spin_durasi.setSuffix(" jam")

        # Tombol Tambah
        self.btn_tambah = QPushButton("Tambah Kegiatan")
        self.btn_tambah.clicked.connect(self.tambahKegiatan)

        # Output List
        self.list_kegiatan = QListWidget()

        # Menu Bar
        self.menubar = QMenuBar(self)
        menu = self.menubar.addMenu("Menu")
        info_action = QAction("Info Aplikasi", self)
        info_action.triggered.connect(self.showInfo)
        menu.addAction(info_action)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.menubar)
        layout.addWidget(self.label_nama)
        layout.addWidget(self.label_nim)

        form_layout = QHBoxLayout()
        form_layout.addWidget(self.input_kegiatan)
        form_layout.addWidget(self.combo_materi)
        form_layout.addWidget(self.spin_durasi)

        layout.addLayout(form_layout)
        layout.addWidget(self.btn_tambah)
        layout.addWidget(self.list_kegiatan)

        self.setLayout(layout)

    def tambahKegiatan(self):
        kegiatan = self.input_kegiatan.text()
        materi = self.combo_materi.currentText()
        durasi = self.spin_durasi.value()

        if kegiatan.strip() == "":
            QMessageBox.warning(self, "Peringatan", "Kegiatan tidak boleh kosong!")
            return

        hasil = f"{kegiatan} - {materi} ({durasi} jam)"
        self.list_kegiatan.addItem(hasil)
        self.input_kegiatan.clear()

    def showInfo(self):
        QMessageBox.information(self, "Tentang Aplikasi", "Aplikasi ini digunakan untuk mencatat kegiatan belajar harian.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TrackerBelajar()
    window.show()
    sys.exit(app.exec_())
