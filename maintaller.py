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
        code = self.textEditCodigoASM.toPlainText()

    def initializeAllInCeros(self):
        for i in range(0, 1024):
            self.table_ram.setItem(i, 0, QTableWidgetItem('0000 0000 0000 0000'))
        for i in range(0, 4):
            self.table_registros.setItem(i, 0, QTableWidgetItem('0000 0000 0000 0000'))
            self.table_registros.setItem(i, 1, QTableWidgetItem('0'))
        for i in range(0, 4):
            self.table_alu.setItem(i, 0, QTableWidgetItem('00'))
            self.table_alu.setItem(i, 1, QTableWidgetItem('0'))
        for i in range(0, 2):
            self.table_unidad_control.setItem(i, 0, QTableWidgetItem('00'))
            self.table_unidad_control.setItem(i, 1, QTableWidgetItem('0'))

    def set_initial_vars(self):
        global variable_a, variable_b
        variable_a = self.table_variables_iniciales.item(0, 0).text()
        variable_b = self.table_variables_iniciales.item(1, 0).text()

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
        global instruccion_actual, instruccion_siguiente

        self.table_variables_iniciales.setDisabled(True)
        self.set_initial_vars()

        instruccion_actual = instruccion_siguiente
        instruccion_siguiente = instruccion_siguiente + 1
        # todo actualizar esto para que use los opcode en vez de otras vainas, hacer un super switch que me verifique que instruccion es y con que celdas o registros
        # todo o en vez de binario, leer el mismo codigo asm con los mismos op code y regex, pero aprovechando el haber guardado las variables en un diccy los saltos, asi queda mas facil
        match instruccion_actual:
            #mcd
            case 0:
                # cargar_A(variable_a)
                self.table_registros.setItem(0, 0, QTableWidgetItem(decimalToBinary(int(variable_a))))
                self.table_registros.setItem(0, 1, QTableWidgetItem(str(variable_a)))

            case 1:
                # cargar_B(variable_b)
                self.table_registros.setItem(1, 0, QTableWidgetItem(decimalToBinary(int(variable_b))))
                self.table_registros.setItem(1, 1, QTableWidgetItem(str(variable_b)))

            #bucle
            case 2:
                # copiar(A,C)
                A = self.table_registros.item(0,1).text()
                self.table_registros.setItem(2, 1, QTableWidgetItem(A))
                self.table_registros.setItem(2, 0, QTableWidgetItem(decimalToBinary(int(A))))

            case 3:
                # restar(C,B)
                B = self.table_registros.item(1, 1).text()
                C = self.table_registros.item(2, 1).text()

                resultado = int(C)-int(B);
                self.table_registros.setItem(2, 1, QTableWidgetItem(str(resultado)))
                self.table_registros.setItem(2, 0, QTableWidgetItem(decimalToBinary(resultado)))

                # Actualizar ALU
                self.actualizar_alu(resultado)

            case 4:
                #SaltarSiCero(fin)
                if int(self.table_alu.item(0, 1).text()) == 1:
                    instruccion_siguiente = 10

            case 5:
                #SaltarSiNeg(menor)
                if int(self.table_alu.item(2, 1).text()) == 1:
                    instruccion_siguiente = 8

            case 6:
                #Restar(A, B)
                A = self.table_registros.item(0, 1).text()
                B = self.table_registros.item(1, 1).text()

                resultado = int(A) - int(B);
                self.table_registros.setItem(0, 1, QTableWidgetItem(str(resultado)))
                self.table_registros.setItem(0, 0, QTableWidgetItem(decimalToBinary(resultado)))

                # Actualizar ALU
                self.actualizar_alu(resultado)

            case 7:
                #Saltar(bucle)
                instruccion_siguiente = 2

            #menor:
            case 8:
                #Restar(B,A)
                A = self.table_registros.item(0, 1).text()
                B = self.table_registros.item(1, 1).text()

                resultado = int(B) - int(A);
                self.table_registros.setItem(1, 1, QTableWidgetItem(str(resultado)))
                self.table_registros.setItem(1, 0, QTableWidgetItem(decimalToBinary(resultado)))

                # Actualizar ALU
                self.actualizar_alu(resultado)

            case 9:
                # Saltar(bucle)
                instruccion_siguiente = 2

            # fin
            case 10:
                #Almacenar A,m
                A = self.table_registros.item(0, 1).text()
                self.table_ram.setItem(13, 0, QTableWidgetItem(A))

            case 11:
                #parar
                self.button_siguiente_instruccion.setDisabled(True)
                self.button_ultima_instruccion.setDisabled(True)

        # actualiza la instruccion actual
        instruccion_actual_ram = self.table_ram.item(instruccion_actual, 0).text()
        self.table_unidad_control.setItem(0, 0, QTableWidgetItem(instruccion_actual_ram))

        # actualiza la siguiente instruccion a correr
        instruccion_siguiente_ram = self.table_ram.item(instruccion_siguiente, 0).text()
        self.table_unidad_control.setItem(1, 0, QTableWidgetItem(instruccion_siguiente_ram))

    @QtCore.pyqtSlot()
    def on_button_ultima_instruccion_clicked(self):
        self.table_variables_iniciales.setDisabled(True)
        self.set_initial_vars()

        while(self.button_siguiente_instruccion.isEnabled()):
            self.on_button_siguiente_instruccion_clicked()

    @QtCore.pyqtSlot()
    def on_button_reiniciar_clicked(self):
        global instruccion_actual, instruccion_siguiente
        self.initializeAllInCeros()
        self.table_variables_iniciales.setDisabled(False)
        instruccion_actual = 0
        instruccion_siguiente = 0
        self.button_siguiente_instruccion.setDisabled(False)
        self.button_ultima_instruccion.setDisabled(False)

    @QtCore.pyqtSlot()
    def on_button_ensamblar_clicked(self):
        assembler.compile()

instruccion_actual = 0
instruccion_siguiente = 0
variable_a = 0
variable_b = 0
code = []

def decimalToBinary(n):
    return bin(n).replace("0b", "")

# Assembler

class Assembler:
    """Assembler for custom assembly code
    """

    def __init__(self):
        # Define opcodes
        self.opcodes = {
            'Parar': '0000 0000 0000 0000',
            'Cargar': '0001',
            'CargarValor': '0010',
            'Almacenar': '0011',
            'SaltarSiCero': '0100 00',
            'SaltarSiNeg': '0100 01',
            'SaltarSiPos': '0100 10',
            'SaltarSiDes': '0100 11',
            'Saltar': '0101 00',
            'Copiar': '0110 0000 0000',
            'Sumar': '0110 0000 0001',
            'Restar': '0110 000 0010',
            'Mult': '0110 0000 0011',
            'Div': '0110 0000 0100'
        }
        self.regular_expresion = {'variable': re.compile(r'\w+'), 'label': re.compile(r'a-zA-Z:')}

    def compile(self):
        global code

        print(self.regular_expresion['variable'])

        #code withouth spaces and divided by line
        refinedCode = code.replace(" ", "")
        refinedCode = code.split('\n')


        # Initialize dictionary of labels
        # key - label name
        # value - address of the following instruction
        labels = {}

        # Initialize dictionary of jump instructions
        # key - instruction address
        # value - label to jump to
        jumps = {}

        # diccionario para variables
        relocVariables = {}

        # Initialize address counter for output file
        # address counter counts instructions (not bytes) in the output file
        address = 0

        # First pass fills in all non-jump commands and builds list of labels
        for statement in refinedCode:
            print(statement)
            # verifica si la instruccion se reconoce por la expresion regular o si no envia error

            # si la reconoció, la divide por comas
            refinedStatement = statement.split(',')
            opname = refinedStatement[0]

            # si es un label lo agrega a la tabla de labels junto con la direccion o contador de la siguiente instruccion despues del label
            if opname == 'label':
                labels[statement.label] = address

            # si lo reconocido no es un label entonces mira si existe una nueva variable


        # Second pass fills in jump instructions
        #primero resuelve los jumps para poner la celda a donde saltan, el adress.
        for jump in jumps:
            # Resolve jump destination
            address = labels[jumps[jump]]
            # Generate new instruction

        # luego debe resolver las variables relocalitableVariables, sabiendo el numero ded instrucciones sumarle de a 1 a las variables segun el orden como fueron
        # apareciendo.

        # Luego mapea cada linea ya con los diccionarios resueltos y pone todo ese resultado en la memoria ram.



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