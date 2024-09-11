"""calcular faturamento"""
import json
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox

def calcular_faturamento(dados):
    """funcao que obtem valores, calcula media e verifica dias acima da media"""
    valores = [item['valor'] for item in dados if item['valor'] > 0]

    if not valores:
        return None, None, 0

    menor = min(valores)
    maior = max(valores)

    media = sum(valores) / len(valores)

    dias_acima_media = sum(1 for valor in valores if valor > media)

    return menor, maior, dias_acima_media

class FaturamentoApp(QWidget):
    """telinha simples"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Análise de Faturamento Diário")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.load_button = QPushButton("Carregar Faturamento (JSON)", self)
        self.load_button.clicked.connect(self.carregar_arquivo)
        layout.addWidget(self.load_button)

        self.result_label = QLabel("Resultados serão exibidos aqui.", self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def carregar_arquivo(self):
        """abre o explorer do sistema para inserir o arquivo JSON com os dados"""
        # um exemplo de arquivo JSON está presente na mesma pasta que esse script
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Selecione o arquivo de Faturamento", "", "JSON Files (*.json);;All Files (*)", options=options)

        if filename:
            try:
                with open(filename, 'r') as file:
                    dados = json.load(file)
                    menor, maior, dias_acima_media = calcular_faturamento(dados)
                    if menor is not None:
                        self.result_label.setText(
                            f"Menor Faturamento: {menor:.2f}\n"
                            f"Maior Faturamento: {maior:.2f}\n"
                            f"Dias acima da média: {dias_acima_media}"
                        )
                    else:
                        self.result_label.setText("Nenhum dia com faturamento válido encontrado.")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao carregar o arquivo: {e}")

if __name__ == "__main__":
    app = QApplication([])
    window = FaturamentoApp()
    window.show()
    app.exec()
