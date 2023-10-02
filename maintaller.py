import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import re
import pcDesigntaller



global variable_a, variable_b, instruccion_actual, code

class Window(QMainWindow, pcDesigntaller.Ui_MainWindow):

    def __init__(self, parent=None):
        global code
        super().__init__(parent)
        self.setupUi(self)
        self.initializeAllInCeros()
        self.registros = {'A' : 0,
                          'B' : 1,
                          'C' : 2,
                          'D' : 3}

    def initializeAllInCeros(self):
        for i in range(0, 1024):
            self.table_ram.setItem(i, 0, QTableWidgetItem('0000000000000000'))
        for i in range(0, 4):
            self.table_registros.setItem(i, 0, QTableWidgetItem('0000000000000000'))
            self.table_registros.setItem(i, 1, QTableWidgetItem('0'))
        for i in range(0, 4):
            self.table_alu.setItem(i, 0, QTableWidgetItem('00'))
            self.table_alu.setItem(i, 1, QTableWidgetItem('0'))
        for i in range(0, 2):
            self.table_unidad_control.setItem(i, 0, QTableWidgetItem('00'))
            self.table_unidad_control.setItem(i, 1, QTableWidgetItem('0'))

    def actualizar_alu(self, resultado):
        #esta funcion coloca true o falso los registros especiales de la alu segun el resultado
        #primero se colocan todos en falso y solo en true el que sea pertinente
        for i in range(0, 4):
            self.table_alu.setItem(i, 0, QTableWidgetItem('00'))
            self.table_alu.setItem(i, 1, QTableWidgetItem('0'))
        if resultado == 0:
            #poner true el C
            self.table_alu.setItem(0, 0, QTableWidgetItem('01'))
            self.table_alu.setItem(0, 1, QTableWidgetItem('1'))
        elif resultado > 0:
            #poner en true el P
            self.table_alu.setItem(1, 0, QTableWidgetItem('01'))
            self.table_alu.setItem(1, 1, QTableWidgetItem('1'))
        elif resultado < 0:
            #poner en true el N
            self.table_alu.setItem(2, 0, QTableWidgetItem('01'))
            self.table_alu.setItem(2, 1, QTableWidgetItem('1'))
        elif type(resultado):
            #poner true el D
            self.table_alu.setItem(3, 0, QTableWidgetItem('01'))
            self.table_alu.setItem(3, 1, QTableWidgetItem('1'))

    @QtCore.pyqtSlot()
    def on_button_siguiente_instruccion_clicked(self):
        global instruccion_actual, instruccion_siguiente, instrucciones_asm

        instruccion_actual = instruccion_siguiente
        instruccion_siguiente = instruccion_siguiente + 1
        print('Instrucción actual: ', instrucciones_asm[instruccion_actual], 'linea: ', instruccion_actual)
        # todo actualizar esto para que use los opcode, hacer un super switch que me verifique que instruccion es y con que celdas o registros
        # Como tengo guardadas las cosas en ram, es mas facil operarlas
        instruccion_actual_asm = instrucciones_asm[instruccion_actual][0]
        match instruccion_actual_asm:
            case 'Cargar':
                registro = self.registros[instrucciones_asm[instruccion_actual][1]]
                celda_ram = instrucciones_asm[instruccion_actual][2]
                contenido_celda_m = self.table_ram.item(celda_ram, 0).text() # me devuelve el contenido de la celda en binario
                self.table_registros.setItem(registro, 0, QTableWidgetItem(decimalToBinary(int(contenido_celda_m))))
                self.table_registros.setItem(registro, 1, QTableWidgetItem(str(contenido_celda_m)))

            case 'CargarValor':
                registro = self.registros[instrucciones_asm[instruccion_actual][1]]
                valor = instrucciones_asm[instruccion_actual][2]
                self.table_registros.setItem(registro, 0, QTableWidgetItem(decimalToBinary(int(valor))))
                self.table_registros.setItem(registro, 1, QTableWidgetItem(str(valor)))

            case 'Almacenar': # almacena R en M
                registro = self.registros[instrucciones_asm[instruccion_actual][1]]
                celda_ram = instrucciones_asm[instruccion_actual][2]
                contenido_en_registro = self.table_registros.item(registro, 0).text()  # me devuelve el contenido del registro en binario
                self.table_ram.setItem(celda_ram, 0, QTableWidgetItem(contenido_en_registro)) # guardo eso en la ram

            case 'SaltarSiCero':
                if int(self.table_alu.item(0, 1).text()) == 1:
                    instruccion_siguiente = instrucciones_asm[instruccion_actual][1]

            case 'SaltarSiNeg':
                if int(self.table_alu.item(2, 1).text()) == 1:
                    instruccion_siguiente = instrucciones_asm[instruccion_actual][1]

            case 'SaltarSiPos':
                if int(self.table_alu.item(1, 1).text()) == 1:
                    instruccion_siguiente = instrucciones_asm[instruccion_actual][1]

            case 'SaltarSiDes':
                if int(self.table_alu.item(3, 1).text()) == 1:
                    instruccion_siguiente = instrucciones_asm[instruccion_actual][1]

            case 'Saltar':
                instruccion_siguiente = instrucciones_asm[instruccion_actual][1]

            case 'Copiar':
                registro_1 = self.registros[instrucciones_asm[instruccion_actual][1]]
                registro_2 = self.registros[instrucciones_asm[instruccion_actual][2]]
                contenido_registro_1 = self.table_registros.item(registro_1, 1).text()
                self.table_registros.setItem(registro_2, 1, QTableWidgetItem(contenido_registro_1))
                self.table_registros.setItem(registro_2, 0, QTableWidgetItem(decimalToBinary(int(contenido_registro_1))))

            case 'Sumar': #suma ambos pero guarda en el primero
                registro_1 = self.registros[instrucciones_asm[instruccion_actual][1]]
                registro_2 = self.registros[instrucciones_asm[instruccion_actual][2]]
                contenido_registro_1 = self.table_registros.item(registro_1, 1).text()
                contenido_registro_2 = self.table_registros.item(registro_2, 1).text()
                resultado = int(contenido_registro_1) + int(contenido_registro_2)
                self.table_registros.setItem(registro_1, 1, QTableWidgetItem(str(resultado)))
                self.table_registros.setItem(registro_1, 0, QTableWidgetItem(decimalToBinary(int(resultado))))
                self.actualizar_alu(resultado)

            case 'Restar':  # resta ambos pero guarda en el primero
                registro_1 = self.registros[instrucciones_asm[instruccion_actual][1]]
                registro_2 = self.registros[instrucciones_asm[instruccion_actual][2]]
                contenido_registro_1 = self.table_registros.item(registro_1, 1).text()
                contenido_registro_2 = self.table_registros.item(registro_2, 1).text()
                resultado = int(contenido_registro_1) - int(contenido_registro_2)
                self.table_registros.setItem(registro_1, 1, QTableWidgetItem(str(resultado)))
                self.table_registros.setItem(registro_1, 0, QTableWidgetItem(decimalToBinary(int(resultado))))
                self.actualizar_alu(resultado)

            case 'Mult':  # multiplica ambos pero guarda en el primero
                registro_1 = self.registros[instrucciones_asm[instruccion_actual][1]]
                registro_2 = self.registros[instrucciones_asm[instruccion_actual][2]]
                contenido_registro_1 = self.table_registros.item(registro_1, 1).text()
                contenido_registro_2 = self.table_registros.item(registro_2, 1).text()
                resultado = int(contenido_registro_1) * int(contenido_registro_2)
                self.table_registros.setItem(registro_1, 1, QTableWidgetItem(str(resultado)))
                self.table_registros.setItem(registro_1, 0, QTableWidgetItem(decimalToBinary(int(resultado))))
                self.actualizar_alu(resultado)

            case 'Div':  # divide ambos pero guarda en el primero, es division entera
                registro_1 = self.registros[instrucciones_asm[instruccion_actual][1]]
                registro_2 = self.registros[instrucciones_asm[instruccion_actual][2]]
                contenido_registro_1 = self.table_registros.item(registro_1, 1).text()
                contenido_registro_2 = self.table_registros.item(registro_2, 1).text()
                resultado = int(contenido_registro_1) // int(contenido_registro_2)
                self.table_registros.setItem(registro_1, 1, QTableWidgetItem(str(resultado)))
                self.table_registros.setItem(registro_1, 0, QTableWidgetItem(decimalToBinary(int(resultado))))
                self.actualizar_alu(resultado)

            case 'Parar':  # Termina el programa haciendo que los botones no se pueda dar siguiente
                self.button_siguiente_instruccion.setDisabled(True)
                self.button_ultima_instruccion.setDisabled(True)

        # actualiza la instruccion actual
        instruccion_actual_ram = self.table_ram.item(instruccion_actual, 0).text()
        self.table_unidad_control.setItem(0, 0, QTableWidgetItem(instruccion_actual_ram))

        # actualiza la siguiente instruccion a correr
        instruccion_siguiente_ram = self.table_ram.item(instruccion_siguiente, 0).text()
        self.table_unidad_control.setItem(1, 0, QTableWidgetItem(instruccion_siguiente_ram))

        if instruccion_siguiente < len(instrucciones_asm):
            print('Instrucción siguiente: ', instrucciones_asm[instruccion_siguiente], 'linea: ', instruccion_siguiente)

    @QtCore.pyqtSlot()
    def on_button_ultima_instruccion_clicked(self):
        while(self.button_siguiente_instruccion.isEnabled()):
            self.on_button_siguiente_instruccion_clicked()

    @QtCore.pyqtSlot()
    def on_button_reiniciar_clicked(self):
        global instruccion_actual, instruccion_siguiente, instrucciones_asm
        self.initializeAllInCeros()
        instruccion_actual = 0
        instruccion_siguiente = 0
        instrucciones_asm = {}
        self.button_siguiente_instruccion.setDisabled(False)
        self.button_ultima_instruccion.setDisabled(False)


    @QtCore.pyqtSlot()
    def on_button_ensamblar_clicked(self):
        global code
        code = self.textEditCodigoASM.toPlainText()
        assembler.compile()

instruccion_actual = 0
instruccion_siguiente = 0
variable_a = 0
variable_b = 0
code = ''
instrucciones_asm = {}

def decimalToBinary(n):
    return format(n, '010b')

# Assembler

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

    def compile(self):
        global code
        global instrucciones_asm

        #code withouth spaces and divided by line
        refinedCode = code.replace(' ','')


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
                    instrucciones_asm[linea] = ['Cargar',registro,relocVariables[variable]]

                case 'CargarValor':
                    values = statement.group().replace('CargarValor', '').split(',')
                    registro = values[0]
                    valor = values[1]
                    binario = self.opcodes['CargarValor'] + self.registros[registro] + decimalToBinary(int(valor))
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    instrucciones_asm[linea] = ['CargarValor', registro, int(valor)]

                case 'Almacenar':
                    values = statement.group().replace('Almacenar', '').split(',')
                    registro = values[0]
                    variable = values[1]
                    binario = self.opcodes['Almacenar'] + self.registros[registro] + decimalToBinary(
                        relocVariables[variable])
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    instrucciones_asm[linea] = ['Almacenar', registro, relocVariables[variable]]

                case 'SaltarSiCero':
                    value = statement.group().replace('SaltarSiCero', '')
                    binario = self.opcodes['SaltarSiCero'] + decimalToBinary(
                        labels[value])
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    instrucciones_asm[linea] = ['SaltarSiCero', labels[value]]

                case 'SaltarSiNeg':
                    value = statement.group().replace('SaltarSiNeg', '')
                    binario = self.opcodes['SaltarSiNeg']  + decimalToBinary(
                        labels[value])
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    instrucciones_asm[linea] = ['SaltarSiNeg', labels[value]]

                case 'SaltarSiPos':
                    value = statement.group().replace('SaltarSiPos', '')
                    binario = self.opcodes['SaltarSiPos'] + decimalToBinary(
                        labels[value])
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    instrucciones_asm[linea] = ['SaltarSiPos', labels[value]]

                case 'SaltarSiDes':
                    value = statement.group().replace('SaltarSiDes', '')
                    binario = self.opcodes['SaltarSiDes'] + decimalToBinary(
                        labels[value])
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    instrucciones_asm[linea] = ['SaltarSiDes', labels[value]]

                case 'Saltar':
                    value = statement.group().replace('Saltar', '')
                    binario = self.opcodes['Saltar'] + decimalToBinary(
                        labels[value])
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    instrucciones_asm[linea] = ['Saltar', labels[value]]

                case 'Copiar':
                    values = statement.group().replace('Copiar', '').split(',')
                    registro1 = values[0]
                    registro2 = values[1]
                    binario = self.opcodes['Copiar'] + self.registros[registro1] + self.registros[registro2]
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    instrucciones_asm[linea] = ['Copiar', registro1, registro2]

                case 'Sumar':
                    values = statement.group().replace('Sumar', '').split(',')
                    registro1 = values[0]
                    registro2 = values[1]
                    binario = self.opcodes['Sumar'] + self.registros[registro1] + self.registros[registro2]
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    instrucciones_asm[linea] = ['Sumar', registro1, registro2]

                case 'Restar':
                    values = statement.group().replace('Restar', '').split(',')
                    registro1 = values[0]
                    registro2 = values[1]
                    binario = self.opcodes['Restar'] + self.registros[registro1] + self.registros[registro2]
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    instrucciones_asm[linea] = ['Restar', registro1, registro2]

                case 'Mult':
                    values = statement.group().replace('Mult', '').split(',')
                    registro1 = values[0]
                    registro2 = values[1]
                    binario = self.opcodes['Mult'] + self.registros[registro1] + self.registros[registro2]
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    instrucciones_asm[linea] = ['Mult', registro1, registro2]

                case 'Div':
                    values = statement.group().replace('Div', '').split(',')
                    registro1 = values[0]
                    registro2 = values[1]
                    binario = self.opcodes['Div'] + self.registros[registro1] + self.registros[registro2]
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    instrucciones_asm[linea] = ['Div', registro1, registro2]

                case 'Parar':
                    binario = self.opcodes['Parar']
                    window.table_ram.setItem(0, linea, QTableWidgetItem(binario))
                    instrucciones_asm[linea] = ['Parar']

            linea += 1

    def handle_int(self, integer):
        """Convert hexidecimal and binary numbers in strings to integers, if needed
        """
        if isinstance(integer, int):
            val = integer
        else:
            val = int(integer, 0)
        return val


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    assembler = Assembler()
    window.show()
    sys.exit(app.exec())