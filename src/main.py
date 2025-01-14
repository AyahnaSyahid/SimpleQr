from PyQt5.QtWidgets import QApplication, \
						    QWidget, \
							QFileDialog, \
							QPlainTextEdit, \
							QPushButton, \
							QMessageBox, \
                            QHBoxLayout, \
                            QVBoxLayout, \
                            QLabel
from PyQt5.QtCore import Qt
import segno

class Ui(QWidget):
    
    def __init__(self):
        super().__init__(None)
        lay = QVBoxLayout(self)
        self.lab = QLabel("Masukkan text:")
        self.textEdit = QPlainTextEdit(self)
        self.textEdit.setTabChangesFocus(True)
        self.saveButton = QPushButton(self)
        self.saveButton.setText("Save")
        lay.addWidget(self.lab)
        lay.addWidget(self.textEdit)
        lay.addWidget(self.saveButton, 0, Qt.AlignRight)
        self.setLayout(lay)
        
        self.saveButton.clicked.connect(self._save_as_action)
    
    def _save_as_action(self):
        data = self.textEdit.toPlainText();
        if not len(data):
            QMessageBox.error(self, "Kesalahan", "Anda belum memasukkan data")
        savePath, _ = QFileDialog.getSaveFileName(self, "Pilih direktori", "qr.svg", "SVG (*.svg)")
        if savePath:
            try:
                qr = segno.make_qr(self.textEdit.toPlainText(), error='l')
                qr.save(savePath, border=4, omitsize=True)
            except:
                QMessageBox.error(self, "Kesalahan", "Tidak dapat menyimpan file")
                return
            QMessageBox.information(self, "Berhasil", "File telah di simpan")

if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationDisplayName("QR Maker")
    ui = Ui()
    ui.show()
    app.exec()