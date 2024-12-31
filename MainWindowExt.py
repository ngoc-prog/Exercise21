from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtWidgets
from math import comb, perm

from MODULE1.Exercise21.MainWindow import Ui_MainWindow


class MainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButtonExecute.clicked.connect(self.calculate)

    def calculate(self):
        try:
            # Lấy giá trị từ người dùng
            N = int(self.lineEditInputN.text())
            k = int(self.lineEditInputk.text())

            # Tính toán hoán vị và tổ hợp
            permutation = perm(N, k)
            combination = comb(N, k)

            # Hiển thị kết quả lên giao diện
            self.lineEditA.setText(str(permutation))
            self.lineEditC.setText(str(combination))
        except ValueError:
            # Nếu người dùng nhập sai kiểu dữ liệu
            QtWidgets.QMessageBox.warning(self, "Input Error", "Vui lòng nhập giá trị hợp lệ cho N và K.")

