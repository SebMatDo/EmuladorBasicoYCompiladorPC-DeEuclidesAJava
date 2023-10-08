import src.views.pcDesigntaller as pcDesigntaller
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from src.utils.convertions import decimalToBinary
from src.models.assembler import Assembler


class Window(QMainWindow, pcDesigntaller.Ui_MainWindow):

    def __init__(self, code, instrucciones_asm, instruccion_actual, instruccion_siguiente, parent=None):
        super().__init__(parent)
        self.code = code
        self.instrucciones_asm = instrucciones_asm
        self.assembler = Assembler()
        self.instruccion_actual = instruccion_actual
        self.instruccion_siguiente = instruccion_siguiente
        self.setupUi(self)
        self.initializeAllInCeros()
        self.registros = {'A': 0,
                          'B': 1,
                          'C': 2,
                          'D': 3}

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
        # esta funcion coloca true o falso los registros especiales de la alu segun el resultado
        # primero se colocan todos en falso y solo en true el que sea pertinente
        for i in range(0, 4):
            self.table_alu.setItem(i, 0, QTableWidgetItem('00'))
            self.table_alu.setItem(i, 1, QTableWidgetItem('0'))
        if resultado == 0:
            # poner true el C
            self.table_alu.setItem(0, 0, QTableWidgetItem('01'))
            self.table_alu.setItem(0, 1, QTableWidgetItem('1'))
        elif resultado > 0:
            # poner en true el P
            self.table_alu.setItem(1, 0, QTableWidgetItem('01'))
            self.table_alu.setItem(1, 1, QTableWidgetItem('1'))
        elif resultado < 0:
            # poner en true el N
            self.table_alu.setItem(2, 0, QTableWidgetItem('01'))
            self.table_alu.setItem(2, 1, QTableWidgetItem('1'))
        elif type(resultado):
            # poner true el D
            self.table_alu.setItem(3, 0, QTableWidgetItem('01'))
            self.table_alu.setItem(3, 1, QTableWidgetItem('1'))

    @QtCore.pyqtSlot()
    def on_button_siguiente_instruccion_clicked(self):
        self.instruccion_actual = self.instruccion_siguiente
        self.instruccion_siguiente = self.instruccion_siguiente + 1
        print('Instrucción actual: ', self.instrucciones_asm[self.instruccion_actual], 'linea: ',
              self.instruccion_actual)
        # todo actualizar esto para que use los opcode, hacer un super switch que me verifique que instruccion es y con que celdas o registros
        # Como tengo guardadas las cosas en ram, es mas facil operarlas
        self.instruccion_actual_asm = self.instrucciones_asm[self.instruccion_actual][0]
        match self.instruccion_actual_asm:
            case 'Cargar':
                registro = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                celda_ram = self.instrucciones_asm[self.instruccion_actual][2]
                contenido_celda_m = self.table_ram.item(celda_ram,
                                                        0).text()  # me devuelve el contenido de la celda en binario
                self.table_registros.setItem(registro, 0, QTableWidgetItem(decimalToBinary(int(contenido_celda_m))))
                self.table_registros.setItem(registro, 1, QTableWidgetItem(str(contenido_celda_m)))

            case 'CargarValor':
                registro = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                valor = self.instrucciones_asm[self.instruccion_actual][2]
                self.table_registros.setItem(registro, 0, QTableWidgetItem(decimalToBinary(int(valor))))
                self.table_registros.setItem(registro, 1, QTableWidgetItem(str(valor)))

            case 'Almacenar':  # almacena R en M
                registro = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                celda_ram = self.instrucciones_asm[self.instruccion_actual][2]
                contenido_en_registro = self.table_registros.item(registro,
                                                                  0).text()  # me devuelve el contenido del registro en binario
                self.table_ram.setItem(celda_ram, 0, QTableWidgetItem(contenido_en_registro))  # guardo eso en la ram

            case 'SaltarSiCero':
                if int(self.table_alu.item(0, 1).text()) == 1:
                    self.instruccion_siguiente = self.instrucciones_asm[self.instruccion_actual][1]

            case 'SaltarSiNeg':
                if int(self.table_alu.item(2, 1).text()) == 1:
                    self.instruccion_siguiente = self.instrucciones_asm[self.instruccion_actual][1]

            case 'SaltarSiPos':
                if int(self.table_alu.item(1, 1).text()) == 1:
                    self.instruccion_siguiente = self.instrucciones_asm[self.instruccion_actual][1]

            case 'SaltarSiDes':
                if int(self.table_alu.item(3, 1).text()) == 1:
                    self.instruccion_siguiente = self.instrucciones_asm[self.instruccion_actual][1]

            case 'Saltar':
                self.instruccion_siguiente = self.instrucciones_asm[self.instruccion_actual][1]

            case 'Copiar':
                registro_1 = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                registro_2 = self.registros[self.instrucciones_asm[self.instruccion_actual][2]]
                contenido_registro_1 = self.table_registros.item(registro_1, 1).text()
                self.table_registros.setItem(registro_2, 1, QTableWidgetItem(contenido_registro_1))
                self.table_registros.setItem(registro_2, 0,
                                             QTableWidgetItem(decimalToBinary(int(contenido_registro_1))))

            case 'Sumar':  # suma ambos pero guarda en el primero
                registro_1 = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                registro_2 = self.registros[self.instrucciones_asm[self.instruccion_actual][2]]
                contenido_registro_1 = self.table_registros.item(registro_1, 1).text()
                contenido_registro_2 = self.table_registros.item(registro_2, 1).text()
                resultado = int(contenido_registro_1) + int(contenido_registro_2)
                self.table_registros.setItem(registro_1, 1, QTableWidgetItem(str(resultado)))
                self.table_registros.setItem(registro_1, 0, QTableWidgetItem(decimalToBinary(int(resultado))))
                self.actualizar_alu(resultado)

            case 'Restar':  # resta ambos pero guarda en el primero
                registro_1 = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                registro_2 = self.registros[self.instrucciones_asm[self.instruccion_actual][2]]
                contenido_registro_1 = self.table_registros.item(registro_1, 1).text()
                contenido_registro_2 = self.table_registros.item(registro_2, 1).text()
                resultado = int(contenido_registro_1) - int(contenido_registro_2)
                self.table_registros.setItem(registro_1, 1, QTableWidgetItem(str(resultado)))
                self.table_registros.setItem(registro_1, 0, QTableWidgetItem(decimalToBinary(int(resultado))))
                self.actualizar_alu(resultado)

            case 'Mult':  # multiplica ambos pero guarda en el primero
                registro_1 = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                registro_2 = self.registros[self.instrucciones_asm[self.instruccion_actual][2]]
                contenido_registro_1 = self.table_registros.item(registro_1, 1).text()
                contenido_registro_2 = self.table_registros.item(registro_2, 1).text()
                resultado = int(contenido_registro_1) * int(contenido_registro_2)
                self.table_registros.setItem(registro_1, 1, QTableWidgetItem(str(resultado)))
                self.table_registros.setItem(registro_1, 0, QTableWidgetItem(decimalToBinary(int(resultado))))
                self.actualizar_alu(resultado)

            case 'Div':  # divide ambos pero guarda en el primero, es division entera
                registro_1 = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                registro_2 = self.registros[self.instrucciones_asm[self.instruccion_actual][2]]
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
        self.instruccion_actual_ram = self.table_ram.item(self.instruccion_actual, 0).text()
        self.table_unidad_control.setItem(0, 0, QTableWidgetItem(self.instruccion_actual_ram))

        # actualiza la siguiente instruccion a correr
        self.instruccion_siguiente_ram = self.table_ram.item(self.instruccion_siguiente, 0).text()
        self.table_unidad_control.setItem(1, 0, QTableWidgetItem(self.instruccion_siguiente_ram))

        if self.instruccion_siguiente < len(self.instrucciones_asm):
            print('Instrucción siguiente: ', self.instrucciones_asm[self.instruccion_siguiente], 'linea: ',
                  self.instruccion_siguiente)

    @QtCore.pyqtSlot()
    def on_button_ultima_instruccion_clicked(self):
        while (self.button_siguiente_instruccion.isEnabled()):
            self.on_button_siguiente_instruccion_clicked()

    @QtCore.pyqtSlot()
    def on_button_reiniciar_clicked(self):
        self.initializeAllInCeros()
        self.instruccion_actual = 0
        self.instruccion_siguiente = 0
        self.instrucciones_asm = {}
        self.button_siguiente_instruccion.setDisabled(False)
        self.button_ultima_instruccion.setDisabled(False)

    @QtCore.pyqtSlot()
    def on_button_ensamblar_clicked(self):
        self.code = self.textEditCodigoASM.toPlainText()
        self.assembler.compile(self)
