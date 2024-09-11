""""calcular percentual de representacao de cada estado"""
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

def calcular_percentuais(faturamento):
    total = sum(faturamento.values())
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}
    return percentuais

class FaturamentoApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Percentual de Faturamento por Estado")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        self.title_label = QLabel("Faturamento Mensal por Estado (%)", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        self.btn_calcular = QPushButton("Calcular Percentuais", self)
        self.btn_calcular.clicked.connect(self.exibir_percentuais)
        layout.addWidget(self.btn_calcular)

        self.result_label = QLabel("", self)
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def exibir_percentuais(self):
        percentuais = calcular_percentuais(faturamento)
        resultado_texto = ""
        for estado, percentual in percentuais.items():
            resultado_texto += f"{estado}: {percentual:.2f}%\n"
        self.result_label.setText(resultado_texto)

if __name__ == "__main__":
    app = QApplication([])

    janela = FaturamentoApp()
    janela.show()

    app.exec()
