import os
from pathlib import Path
from src.models.Lexer import MyLexer
from src.models.Parser import MyParser

class Compiler:
    def __init__(self):
        self.myLex = MyLexer()
        self.myPars = MyParser(self.myLex)

    def compile(self, code):

        # Si no se le pasa código, se toma el de un archivo
        if code == '':
            data_folder = Path(os.getcwd())
            file_path = data_folder / "tests/lexer/algoritmoPrueba.lp"
            print(file_path)
            data = open(file_path,'r').read()
            code = data

        self.myLex.build() # Build the lexer
        self.myPars.test(code) # construir lexer y probarlo

        return self.myPars.resultAsm