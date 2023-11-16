import sys
from PyQt5.QtWidgets import QApplication
from src.controllers.windowController import Window
from src.models.VirtualMachine import Machine


instruccion_actual = 0
instruccion_siguiente = 0
code = """mcd:                        
CargarValor    A, 128                        
CargarValor     B, 244
bucle:                        
Copiar        A, C                        
Restar        C, B                        
SaltarSiCero    fin
SaltarSiNeg    menor                        
Restar        A, B                        
Saltar        bucle                        
menor:                                                
Restar        B,A                        
Saltar        bucle                        
fin:                        
Almacenar    A,50                        
Parar"""
instrucciones_asm = {}

# Inicializar la máquina
machine = Machine(code, instruccion_actual, instruccion_siguiente, use_console=True)




# Inicializar la aplicación
app = QApplication(sys.argv)
window = Window(machine)
window.show()
sys.exit(app.exec())

