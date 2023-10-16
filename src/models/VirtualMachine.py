from src.utils.convertions import decimalToBinary
from src.models.Assembler import Assembler


class Machine:

    def __init__(self, code, instrucciones_asm, instruccion_actual, instruccion_siguiente):
        self.windows = []
        self.assembler = Assembler()
        self.code = code
        self.instrucciones_asm = instrucciones_asm
        self.instruccion_actual = instruccion_actual
        self.instruccion_siguiente = instruccion_siguiente
        self.table_ram = ['0000000000000000' for i in range(0, 1024)]
        self.object_code = ['0000000000000000' for i in range(0, 1024)]
        self.table_registros = [['0000000000000000','0'] for i in range(0, 4)]
        self.table_alu = [['00', '0'] for i in range(0, 4)]
        self.table_unidad_control = ['00' for i in range(0, 2)]
        self.initializeAllInCeros()
        self.registros = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    
    def addWindow(self, window):
        self.windows.append(window)

    def initializeAllInCeros(self):
        for i in range(0, 1024):
            self.table_ram[i] = '0000000000000000'
            self.object_code[i] = '0000000000000000'
        for i in range(0, 4):
            self.table_registros[i][0] = '0000000000000000'
            self.table_registros[i][1] = '0'
        for i in range(0, 4):
            self.table_alu[i][0] = '00'
            self.table_alu[i][1] = '0'
        for i in range(0, 2):
            self.table_unidad_control[i] = '00'

    def actualizar_alu(self, resultado):
        # esta funcion coloca true o falso los registros especiales de la alu segun el resultado
        # primero se colocan todos en falso y solo en true el que sea pertinente
        for i in range(0, 4):
            self.table_alu[i][0] = '00'
            self.table_alu[i][1] = '0'
        if resultado == 0:
            # poner true el C
            self.table_alu[0][0] = '01'
            self.table_alu[0][1] = '1'
        elif resultado > 0:
            # poner en true el P
            self.table_alu[1][0] = '01'
            self.table_alu[1][1] = '1'
        elif resultado < 0:
            # poner en true el N
            self.table_alu[2][0] = '01'
            self.table_alu[2][1] = '1'
        elif type(resultado):
            # poner true el D
            self.table_alu[3][0] = '01'
            self.table_alu[3][1] = '1'

    def siguiente_instruccion(self):
        self.instruccion_actual = self.instruccion_siguiente
        self.instruccion_siguiente = self.instruccion_siguiente + 1
        print('Instrucción actual: ', self.instrucciones_asm[self.instruccion_actual], 'linea: ',self.instruccion_actual)
        # todo actualizar esto para que use los opcode, hacer un super switch que me verifique que instruccion es y con que celdas o registros
        # Como tengo guardadas las cosas en ram, es mas facil operarlas
        self.instruccion_actual_asm = self.instrucciones_asm[self.instruccion_actual][0]
        match self.instruccion_actual_asm:
            case 'Cargar':
                registro = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                celda_ram = self.instrucciones_asm[self.instruccion_actual][2]
                contenido_celda_m = self.table_ram[celda_ram]  # me devuelve el contenido de la celda en binario
                self.table_registros[registro][0] = decimalToBinary(int(contenido_celda_m))
                self.table_registros[registro][1] = str(contenido_celda_m)

            case 'CargarValor':
                registro = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                valor = self.instrucciones_asm[self.instruccion_actual][2]
                self.table_registros[registro][0] = decimalToBinary(int(valor))
                self.table_registros[registro][1] = str(valor)

            case 'Almacenar':  # almacena R en M
                registro = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                celda_ram = self.instrucciones_asm[self.instruccion_actual][2]
                contenido_en_registro = self.table_registros[registro][0]  # me devuelve el contenido del registro en binario
                self.table_ram[celda_ram] = contenido_en_registro  #guardo eso en la ram

            case 'SaltarSiCero':
                if int(self.table_alu[0][1]) == 1:
                    self.instruccion_siguiente = self.instrucciones_asm[self.instruccion_actual][1]

            case 'SaltarSiNeg':
                if int(self.table_alu[2][1]) == 1:
                    self.instruccion_siguiente = self.instrucciones_asm[self.instruccion_actual][1]

            case 'SaltarSiPos':
                if int(self.table_alu[1][1]) == 1:
                    self.instruccion_siguiente = self.instrucciones_asm[self.instruccion_actual][1]

            case 'SaltarSiDes':
                if int(self.table_alu[3][1]) == 1:
                    self.instruccion_siguiente = self.instrucciones_asm[self.instruccion_actual][1]

            case 'Saltar':
                self.instruccion_siguiente = self.instrucciones_asm[self.instruccion_actual][1]

            case 'Copiar':
                registro_1 = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                registro_2 = self.registros[self.instrucciones_asm[self.instruccion_actual][2]]
                contenido_registro_1 = self.table_registros[registro_1][1]
                self.table_registros[registro_2][1] = contenido_registro_1
                self.table_registros[registro_2][0] = decimalToBinary(int(contenido_registro_1))

            case 'Sumar':  # suma ambos pero guarda en el primero
                registro_1 = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                registro_2 = self.registros[self.instrucciones_asm[self.instruccion_actual][2]]
                contenido_registro_1 = self.table_registros[registro_1][1]
                contenido_registro_2 = self.table_registros[registro_2][1]
                resultado = int(contenido_registro_1) + int(contenido_registro_2)
                self.table_registros[registro_1][1] = str(resultado)
                self.table_registros[registro_1][0] = decimalToBinary(int(resultado))
                self.actualizar_alu(resultado)

            case 'Restar':  # resta ambos pero guarda en el primero
                registro_1 = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                registro_2 = self.registros[self.instrucciones_asm[self.instruccion_actual][2]]
                contenido_registro_1 = self.table_registros[registro_1][1]
                contenido_registro_2 = self.table_registros[registro_2][1]
                resultado = int(contenido_registro_1) - int(contenido_registro_2)
                self.table_registros[registro_1][1] = str(resultado)
                self.table_registros[registro_1][0] = decimalToBinary(int(resultado))
                self.actualizar_alu(resultado)

            case 'Mult':  # multiplica ambos pero guarda en el primero
                registro_1 = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                registro_2 = self.registros[self.instrucciones_asm[self.instruccion_actual][2]]
                contenido_registro_1 = self.table_registros[registro_1][1]
                contenido_registro_2 = self.table_registros[registro_2][1]
                resultado = int(contenido_registro_1) * int(contenido_registro_2)
                self.table_registros[registro_1][1] = str(resultado)
                self.table_registros[registro_1][0] = decimalToBinary(int(resultado))
                self.actualizar_alu(resultado)

            case 'Div':  # divide ambos pero guarda en el primero, es division entera
                registro_1 = self.registros[self.instrucciones_asm[self.instruccion_actual][1]]
                registro_2 = self.registros[self.instrucciones_asm[self.instruccion_actual][2]]
                contenido_registro_1 = self.table_registros[registro_1][1]
                contenido_registro_2 = self.table_registros[registro_2][1]
                resultado = int(contenido_registro_1) // int(contenido_registro_2)
                self.table_registros[registro_1][1] = str(resultado)
                self.table_registros[registro_1][0] = decimalToBinary(int(resultado))
                self.actualizar_alu(resultado)

            case 'Parar':  # Termina el programa marcandolo como finalizado en la unidad de control
                self.table_unidad_control = ['xx' for i in range(0, 2)]
                return

        # actualiza la instruccion actual
        self.instruccion_actual_ram = self.table_ram[self.instruccion_actual]
        self.table_unidad_control[0] = self.instruccion_actual_ram

        # actualiza la siguiente instruccion a correr
        self.table_unidad_control[1] = str(self.instruccion_siguiente)

        if self.instruccion_siguiente < len(self.instrucciones_asm):
            print('Instrucción siguiente: ', self.instrucciones_asm[self.instruccion_siguiente], 'linea: ', self.instruccion_siguiente)

    def ultima_instruccion(self):
        while (not (self.table_unidad_control[0] == 'xx' and self.table_unidad_control[1] == 'xx')):
            self.siguiente_instruccion()

    def reiniciar(self):
        self.initializeAllInCeros()
        self.instruccion_actual = 0
        self.instruccion_siguiente = 0
        self.instrucciones_asm = {}

    def ensamblar(self, textEditCodigoASM):
        self.code = textEditCodigoASM
        self.assembler.compile(self)
