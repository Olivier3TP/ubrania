import sys
from PyQt6.QtWidgets import QWidget, QApplication
from layout import Ui_Dialog


class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radio_s.toggled.connect(self.button_click)
        self.ui.radio_m.toggled.connect(self.button_click)
        self.ui.radio_l.toggled.connect(self.button_click)
        self.ui.radio_xl.toggled.connect(self.button_click)
        self.ui.radio_paczkomat.toggled.connect(self.button_click)
        self.ui.radio_kurier.toggled.connect(self.button_click)
        self.ui.radio_odbior.toggled.connect(self.button_click)


        self.show()

    def button_click(self):
        rozmiar = ""
        dostawa = ""

        if self.ui.radio_s.isChecked():
            rozmiar = "S"
        elif self.ui.radio_m.isChecked():
            rozmiar = "M"
        elif self.ui.radio_l.isChecked():
            rozmiar = "L"
        elif self.ui.radio_xl.isChecked():
            rozmiar = "XL"

        if self.ui.radio_paczkomat.isChecked():
            dostawa = "Paczkomat"
        elif self.ui.radio_kurier.isChecked():
            dostawa = "Kurier"
        elif self.ui.radio_odbior.isChecked():
            dostawa = "Odbiór osobisty"

        self.ui.wynik_label.setText(f'Rozmiar twojej koszulki to: {rozmiar} i sposób dostawy: {dostawa}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())