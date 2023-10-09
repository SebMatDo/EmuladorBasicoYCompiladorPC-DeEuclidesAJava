import re
from PyQt5.QtWidgets import QTableWidgetItem
from src.utils.convertions import decimalToBinary

class Assembler:
    """Assembler for custom assembly code
    """

    def __init__(self):
        # Define opcodes
        self.opcodes = {
            'Parar': '0000000000000000',
            'Cargar': '0001',
            'CargarValor': '0010',
            'Almacenar': '0011',
            'SaltarSiCero': '010000',
            'SaltarSiNeg': '010001',
            'SaltarSiPos': '010010',
            'SaltarSiDes': '010011',
            'Saltar': '010100',
            'Copiar': '011000000000',
            'Sumar': '011000000001',
            'Restar': '011000000010',
            'Mult': '011000000011',
            'Div': '011000000100'
        }
        self.registros = {
            'A': '00',
            'B': '01',
            'C': '10',
            'D': '11'
        }
        self.basic_regular_expresion = {
            'variable': '\w+',
            'label': '\w+:',
            'valor': '\d+',
            'registro': '(A|B|C|D)'
        }
        self.opcode_regular_expresion = re.compile(
            r'(?P<Parar>Parar)|(?P<Cargar>Cargar%s,%s)|(?P<CargarValor>CargarValor%s,%s)|(?P<Almacenar>Almacenar%s,%s)|'
            r'(?P<SaltarSiCero>SaltarSiCero%s)|(?P<SaltarSiNeg>SaltarSiNeg%s)|(?P<SaltarSiPos>SaltarSiPos%s)|'
            r'(?P<SaltarSiDes>SaltarSiDes%s)|(?P<Saltar>Saltar%s)|(?P<Copiar>Copiar%s,%s)|(?P<Sumar>Sumar%s,%s)|'
            r'(?P<Restar>Restar%s,%s)|(?P<Mult>Mult%s,%s)|(?P<Div>Div%s,%s)|(?P<Label>%s)' %
            (
                self.basic_regular_expresion['registro'], self.basic_regular_expresion['variable'],
                self.basic_regular_expresion['registro'], self.basic_regular_expresion['valor'],
                self.basic_regular_expresion['registro'], self.basic_regular_expresion['variable'],
                self.basic_regular_expresion['variable'],
                self.basic_regular_expresion['variable'],
                self.basic_regular_expresion['variable'],
                self.basic_regular_expresion['variable'],
                self.basic_regular_expresion['variable'],
                self.basic_regular_expresion['registro'], self.basic_regular_expresion['registro'],
                self.basic_regular_expresion['registro'], self.basic_regular_expresion['registro'],
                self.basic_regular_expresion['registro'], self.basic_regular_expresion['registro'],
                self.basic_regular_expresion['registro'], self.basic_regular_expresion['registro'],
                self.basic_regular_expresion['registro'], self.basic_regular_expresion['registro'],
                self.basic_regular_expresion['label'],

            ), re.IGNORECASE
        )

    def compile(self, window):
        #code withouth spaces and divided by line
        refinedCode = window.code.replace(' ','')


        # Initialize dictionary of labels
        # key - label name
        # value - address of the following instruction
        labels = {}

        # diccionario para variables
        relocVariables = {}

        # Initialize address counter for output file
        # address counter counts instructions (not bytes) in the output file
        linea = 0
        # First pass fills in all non-jump commands and builds list of labels
        for statement in self.opcode_regular_expresion.finditer(refinedCode):

            #Va avanzando en las lineas para saber a donde saltar facilmente,  primeramente se llenan variables y labels
            linea += 1
            opname = statement.lastgroup
            match opname:
                case 'Label':
                    # si es un label lo agrega a la tabla de labels junto con la direccion o contador de la siguiente instruccion despues del label
                    value = statement.group().replace(':','')
                    labels[value] = linea - 1 # guarda la linea a la cual hace referencia el label se resta 1 porque contamos desde cero
                    linea -= 1 # disminuye una linea porque el label no se tiene en cuenta como instruccion
                case 'Cargar':
                    # guarda la variable para despues,
                    values = statement.group().replace('Cargar','').split(',')
                    variable = values[1]
                    relocVariables[variable] = 1
                case 'Almacenar':
                    # guarda la variable para despues,
                    values = statement.group().replace('Almacenar', '').split(',')
                    variable = values[1]
                    relocVariables[variable] = 1
                case 'None':
                    print('Error en linea: ', linea)

        # acá es donde se rellena utilizando los datos anteriores.
        # conociendo el numero de instrucciones podemos estar seguros de darle a la variables espacio en ram desde núm de instrucciones + 1

        for variable in relocVariables:
            linea += 1
            relocVariables[variable] = linea # les digo en que posicion de la ram pueden quedar las variables todo convertir a binario

        linea = 0

        # Luego mapea cada linea ya con los diccionarios resueltos y coloca ese resultado en la memoria ram.
        # todo Tambien se guardan las instrucciones en texto para la simulacion de manera: {linea de instrucción: [tipo de instruccion, registro, memoria]}
        for statement in self.opcode_regular_expresion.finditer(refinedCode):
            print(statement)
            opname = statement.lastgroup
            match opname:
                case 'Label':#si es un label, ya sabemos que se ignora
                    linea -= 1
                case 'Cargar':
                    values = statement.group().replace('Cargar','').split(',')
                    registro = values[0]
                    variable = values[1]
                    binario = self.opcodes['Cargar'] + self.registros[registro] + decimalToBinary(relocVariables[variable])
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    window.instrucciones_asm[linea] = ['Cargar',registro,relocVariables[variable]]

                case 'CargarValor':
                    values = statement.group().replace('CargarValor', '').split(',')
                    registro = values[0]
                    valor = values[1]
                    binario = self.opcodes['CargarValor'] + self.registros[registro] + decimalToBinary(int(valor))
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    window.instrucciones_asm[linea] = ['CargarValor', registro, int(valor)]

                case 'Almacenar':
                    values = statement.group().replace('Almacenar', '').split(',')
                    registro = values[0]
                    variable = values[1]
                    binario = self.opcodes['Almacenar'] + self.registros[registro] + decimalToBinary(
                        relocVariables[variable])
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    window.instrucciones_asm[linea] = ['Almacenar', registro, relocVariables[variable]]

                case 'SaltarSiCero':
                    value = statement.group().replace('SaltarSiCero', '')
                    binario = self.opcodes['SaltarSiCero'] + decimalToBinary(
                        labels[value])
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    window.instrucciones_asm[linea] = ['SaltarSiCero', labels[value]]

                case 'SaltarSiNeg':
                    value = statement.group().replace('SaltarSiNeg', '')
                    binario = self.opcodes['SaltarSiNeg']  + decimalToBinary(
                        labels[value])
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    window.instrucciones_asm[linea] = ['SaltarSiNeg', labels[value]]

                case 'SaltarSiPos':
                    value = statement.group().replace('SaltarSiPos', '')
                    binario = self.opcodes['SaltarSiPos'] + decimalToBinary(
                        labels[value])
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    window.instrucciones_asm[linea] = ['SaltarSiPos', labels[value]]

                case 'SaltarSiDes':
                    value = statement.group().replace('SaltarSiDes', '')
                    binario = self.opcodes['SaltarSiDes'] + decimalToBinary(
                        labels[value])
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    window.instrucciones_asm[linea] = ['SaltarSiDes', labels[value]]

                case 'Saltar':
                    value = statement.group().replace('Saltar', '')
                    binario = self.opcodes['Saltar'] + decimalToBinary(
                        labels[value])
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    window.instrucciones_asm[linea] = ['Saltar', labels[value]]

                case 'Copiar':
                    values = statement.group().replace('Copiar', '').split(',')
                    registro1 = values[0]
                    registro2 = values[1]
                    binario = self.opcodes['Copiar'] + self.registros[registro1] + self.registros[registro2]
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    window.instrucciones_asm[linea] = ['Copiar', registro1, registro2]

                case 'Sumar':
                    values = statement.group().replace('Sumar', '').split(',')
                    registro1 = values[0]
                    registro2 = values[1]
                    binario = self.opcodes['Sumar'] + self.registros[registro1] + self.registros[registro2]
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    window.instrucciones_asm[linea] = ['Sumar', registro1, registro2]

                case 'Restar':
                    values = statement.group().replace('Restar', '').split(',')
                    registro1 = values[0]
                    registro2 = values[1]
                    binario = self.opcodes['Restar'] + self.registros[registro1] + self.registros[registro2]
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    window.instrucciones_asm[linea] = ['Restar', registro1, registro2]

                case 'Mult':
                    values = statement.group().replace('Mult', '').split(',')
                    registro1 = values[0]
                    registro2 = values[1]
                    binario = self.opcodes['Mult'] + self.registros[registro1] + self.registros[registro2]
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    window.instrucciones_asm[linea] = ['Mult', registro1, registro2]

                case 'Div':
                    values = statement.group().replace('Div', '').split(',')
                    registro1 = values[0]
                    registro2 = values[1]
                    binario = self.opcodes['Div'] + self.registros[registro1] + self.registros[registro2]
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    window.instrucciones_asm[linea] = ['Div', registro1, registro2]

                case 'Parar':
                    binario = self.opcodes['Parar']
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    window.instrucciones_asm[linea] = ['Parar']

            linea += 1

    def handle_int(self, integer):
        """Convert hexidecimal and binary numbers in strings to integers, if needed
        """
        if isinstance(integer, int):
            val = integer
        else:
            val = int(integer, 0)
        return val

