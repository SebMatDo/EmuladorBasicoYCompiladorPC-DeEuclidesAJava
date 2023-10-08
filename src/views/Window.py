import src.views.pcDesigntaller as pcDesigntaller
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from src.models.VirtualMachine import Machine


class Window(QMainWindow, pcDesigntaller.Ui_MainWindow):

    def __init__(self, machine : Machine, parent : pcDesigntaller.Ui_MainWindow = None):
        super().__init__(parent)
        self.machine = machine
        self.setupUi(self)
        self.updateStateMachine()

    #Actualiza el estado de la máquina que se muestra con la máquina emulada
    def updateStateMachine(self):
        [self.table_ram.setItem(i, 0, QTableWidgetItem(self.machine.table_ram[i])) for i in range(0, 1024)]
        [self.table_registros.setItem(i, 0, QTableWidgetItem(self.machine.table_registros[i][0])) for i in range(0, 4)]
        [self.table_registros.setItem(i, 1, QTableWidgetItem(str(self.machine.table_registros[i][1]))) for i in range(0, 4)]
        [self.table_alu.setItem(i, 0, QTableWidgetItem(self.machine.table_alu[i][0])) for i in range(0, 4)] 
        [self.table_alu.setItem(i, 1, QTableWidgetItem(str(self.machine.table_alu[i][1]))) for i in range(0, 4)]
        [self.table_unidad_control.setItem(i, 0, QTableWidgetItem(self.machine.table_unidad_control[i])) for i in range(0, 2)]

    def initializeAllInCeros(self):
        self.machine.initializeAllInCeros()
        self.updateStateMachine()

    def actualizar_alu(self, resultado):
        self.machine.actualizar_alu(resultado)
        self.updateStateMachine()

    @QtCore.pyqtSlot()
    def on_button_siguiente_instruccion_clicked(self):
        self.machine.siguiente_instruccion()
        self.updateStateMachine()

    @QtCore.pyqtSlot()
    def on_button_ultima_instruccion_clicked(self):
        self.machine.ultima_instruccion()
        self.updateStateMachine()

    @QtCore.pyqtSlot()
    def on_button_reiniciar_clicked(self):
        self.machine.reiniciar()
        self.updateStateMachine()

    @QtCore.pyqtSlot()
    def on_button_ensamblar_clicked(self):
        self.machine.ensamblar(self.textEditCodigoASM.toPlainText())
        self.updateStateMachine()
