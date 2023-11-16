import sys
import os
from PyQt5.QtWidgets import QApplication
from src.controllers.windowController import Window
from src.models.VirtualMachine import Machine
from pathlib import Path

from src.models.Lexer import MyLexer
from src.models.Parser import MyParser

instruccion_actual = 0
instruccion_siguiente = 0
code = ''
instrucciones_asm = {}

# Inicializar la máquina
machine = Machine(code, instruccion_actual, instruccion_siguiente, use_console=True)


data_folder = Path(os.getcwd())
file_path = data_folder / "tests/lexer/algoritmoPrueba.lp"
print(file_path)
data = open(file_path,'r').read()

# construir lexer y probarlo
myLex = MyLexer()
myLex.build() # Build the lexer

myPars = MyParser(myLex)
myPars.test(data)

# Inicializar la aplicación
app = QApplication(sys.argv)
window = Window(machine)
window.show()
sys.exit(app.exec())

