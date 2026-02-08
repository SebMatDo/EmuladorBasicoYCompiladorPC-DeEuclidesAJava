import sys
from PyQt5.QtWidgets import QApplication
from src.controllers.windowController import Window
from src.models.VirtualMachine import Machine
#from src.models import Lexer

instruccion_actual = 0
instruccion_siguiente = 0
code = ''
instrucciones_asm = {}

# Inicializar la máquina
machine = Machine(code, instruccion_actual, instruccion_siguiente)

# Inicializar la aplicación
app = QApplication(sys.argv)
window = Window(machine)
window.show()
sys.exit(app.exec())

