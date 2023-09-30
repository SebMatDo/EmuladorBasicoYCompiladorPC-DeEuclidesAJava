import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot

import pcDesign
global variable_a, variable_b, instruccion_actual

class Window(QMainWindow, pcDesign.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initializeAllInCeros()
        code = self.textEditCodigoASM.toPlainText().split('\n')
        variable_a = self.table_variables_iniciales.item(0, 0).text()
        variable_b = self.table_variables_iniciales.item(1, 0).text()

    def initializeAllInCeros(self):
        for i in range(12,1024):
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

    @QtCore.pyqtSlot()
    def on_button_siguiente_instruccion_clicked(self):
        global instruccion_actual, instruccion_siguiente

        self.table_variables_iniciales.setDisabled(True)
        self.set_initial_vars()

        instruccion_actual = instruccion_siguiente
        instruccion_siguiente = instruccion_siguiente + 1

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

code = []
instruccion_actual = 0
instruccion_siguiente = 0
variable_a = 0
variable_b = 0

def decimalToBinary(n):
    return bin(n).replace("0b", "")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())