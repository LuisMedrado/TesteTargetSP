"""verificação de fibonacci simples"""
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox

def is_fibonacci(n):
    """funcao de checagem"""
    if n < 0:
        return False
    
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

class FibonacciChecker(QWidget):
    """telinha simples pra nao ter que usar o terminal"""
    def __init__(self):
        # que seja feita a herança
        super().__init__()
        
        self.setWindowTitle("Bora ver se esse número faz parte de fibonacci?")
        self.setGeometry(150, 150, 450, 200)
        
        layout = QVBoxLayout()
        
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Insira um número inteiro")
        layout.addWidget(self.input_field)
        
        self.check_button = QPushButton("Verificar", self)
        self.check_button.clicked.connect(self.check_fibonacci)
        layout.addWidget(self.check_button)
        
        self.result_label = QLabel("", self)
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)
    
    def check_fibonacci(self):
        """execucao da checagem e print do resultado"""
        user_input = self.input_field.text()
        
        # tratamento no caso de um input nao inteiro
        try:
            number = int(user_input)
        except ValueError:
            self.show_error()
            return
        
        # tratamento no caso de um input negativo
        if number < 0:
            self.show_error()
            return
        
        # verificar e printar
        if is_fibonacci(number):
            self.result_label.setText(f"{number} pertence à sequência de Fibonacci!")
        else:
            self.result_label.setText(f"{number} não pertence à sequência de Fibonacci.")
    
    # pop up que aparece se der ruim no input
    def show_error(self):
        QMessageBox.critical(self, "Erro", "Por favor, insira um número inteiro válido (0 ou maior).")


if __name__ == "__main__":
    app = QApplication([])
    window = FibonacciChecker()
    window.show()
    app.exec()
