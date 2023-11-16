import src.views.pcDesigntaller as pcDesigntaller
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from src.models.VirtualMachine import Machine


class Window(QMainWindow, pcDesigntaller.Ui_MainWindow):

    def __init__(self, machine : Machine, parent : pcDesigntaller.Ui_MainWindow = None):
        super().__init__(parent)
        self.machine = machine
        machine.addWindow(self)
        self.setupUi(self)
        self.updateStateMachine()

    #Actualiza el estado de la máquina que se muestra con la máquina emulada
    def updateStateMachine(self):
        for window in self.machine.windows:
            [window.table_ram.setItem(i, 0, QTableWidgetItem(window.machine.table_ram[i])) for i in range(0, 1024)]
            [window.table_registros.setItem(i, 0, QTableWidgetItem(window.machine.table_registros[i][0])) for i in range(0, 4)]
            [window.table_registros.setItem(i, 1, QTableWidgetItem(str(window.machine.table_registros[i][1]))) for i in range(0, 4)]
            [window.table_alu.setItem(i, 0, QTableWidgetItem(window.machine.table_alu[i][0])) for i in range(0, 4)] 
            [window.table_alu.setItem(i, 1, QTableWidgetItem(str(window.machine.table_alu[i][1]))) for i in range(0, 4)]
            [window.table_unidad_control.setItem(i, 0, QTableWidgetItem(window.machine.table_unidad_control[i])) for i in range(0, 2)]
            window.textEditCodigoObjeto.setText("".join([window.machine.object_code[i]+"\n" for i in range(0, 1024)]))
            window.textEditCodigoASM.setText(window.machine.code)
            window.table_ram.selectRow(window.machine.instruccion_actual) if window.machine.instruccion_actual > 0 else 0

            if window.machine.use_console:
                window.textEditConsola.setText(window.machine.console.IO.getvalue())
                cursor_console = self.textEditConsola.textCursor()
                cursor_console.movePosition(cursor_console.End)
                self.textEditConsola.setTextCursor(cursor_console)
                self.textEditConsola.ensureCursorVisible()


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

    @QtCore.pyqtSlot()
    def on_button_enlazar_cargar_clicked(self):
        for window in self.machine.windows:
            self.machine.enlazar_cargar(window.spinBox_pos_enlazar.value())
        self.updateStateMachine()
    
    @QtCore.pyqtSlot()
    def on_button_compilar_clicked(self):
        self.machine.compile(self.textEditCodigoFuente.toPlainText())
        self.updateStateMachine()
