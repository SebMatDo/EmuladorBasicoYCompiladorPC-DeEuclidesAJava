import sys
from PyQt5.QtWidgets import QApplication
from src.controllers.windowController import Window
from src.models.VirtualMachine import Machine
import os
from pathlib import Path

instruccion_actual = 0
instruccion_siguiente = 0
code = ""
instrucciones_asm = {}

# Inicializar la máquina
machine = Machine(code, instruccion_actual, instruccion_siguiente, use_console=False)


data_folder = Path(os.getcwd())
file_path = data_folder / "tests/lexer/algoritmoPrueba.lp"
print(file_path)
data = open(file_path,'r').read()

machine.compile(data)




# # Inicializar la aplicación
# app = QApplication(sys.argv)
# window = Window(machine)
# window.show()
# sys.exit(app.exec())

