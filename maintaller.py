import sys
from PyQt5.QtWidgets import QApplication
from src.views.Window import Window
from src.models.VirtualMachine import Machine

instruccion_actual = 0
instruccion_siguiente = 0
code = ''
instrucciones_asm = {}

# Inicializar la máquina
machine = Machine(code, instrucciones_asm, instruccion_actual, instruccion_siguiente)

# Inicializar la aplicación
app = QApplication(sys.argv)
window = Window(machine)
window.show()
sys.exit(app.exec())