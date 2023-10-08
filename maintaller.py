import sys
from PyQt5.QtWidgets import QApplication
from src.views.Window import Window

instruccion_actual = 0
instruccion_siguiente = 0
code = ''
instrucciones_asm = {}

# Inicializar la aplicación
app = QApplication(sys.argv)
window = Window(code, instrucciones_asm, instruccion_actual, instruccion_siguiente)
window.show()
sys.exit(app.exec())