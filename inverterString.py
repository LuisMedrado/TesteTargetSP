"""inverter uma string"""
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt

def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

class InversaoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inversor de String")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        self.title_label = QLabel("Digite a string para inverter", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        self.input_text = QLineEdit(self)
        layout.addWidget(self.input_text)

        self.btn_inverter = QPushButton("Inverter", self)
        self.btn_inverter.clicked.connect(self.exibir_inversao)
        layout.addWidget(self.btn_inverter)

        self.result_label = QLabel("", self)
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def exibir_inversao(self):
        texto_original = self.input_text.text()
        texto_invertido = inverter_string(texto_original)
        self.result_label.setText(f"String invertida: {texto_invertido}")

if __name__ == "__main__":
    app = QApplication([])

    janela = InversaoApp()
    janela.show()

    app.exec()
