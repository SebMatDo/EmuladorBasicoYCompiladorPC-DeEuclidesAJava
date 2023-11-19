import re
from src.utils.convertions import decimalToBinary, binaryToDec, isNum
from src.models.Assembler import Assembler
from src.models.LinkerLoader import LinkerLoader
from src.models.consola import CapturadorSalida
from src.models.Compiler import Compiler
from src.models.InputConsola import InputConsola

class Machine:

    def __init__(self, code, instruccion_actual, instruccion_siguiente, use_console = True):
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
            'Div': '011000000100',
            'Escribir': '1111',
            'LeerIO': '0111'
        }
        self.registers = {
            'A': '00',
            'B': '01',
            'C': '10',
            'D': '11'
        }
        self.windows = []
        self.assembler = Assembler()
        self.likerLoader= LinkerLoader()
        self.compiler = Compiler()
        self.use_console = use_console
        if use_console:
            self.console = CapturadorSalida()
        self.input = InputConsola()
        self.code = code
        self.hight_level_code = ''
        self.instruccion_actual = instruccion_actual
        self.instruccion_siguiente = instruccion_siguiente
        self.table_ram = ['0000000000000000' for i in range(0, 1024)]
        self.object_code = ['0000000000000000' for i in range(0, 1024)]
        self.table_registros = [['0000000000000000','0'] for i in range(0, 4)]
        self.table_alu = [['00', '0'] for i in range(0, 4)]
        self.table_unidad_control = ['00' for i in range(0, 2)]
        self.initializeAllInCeros()
        self.registros = {'00': 0, '01': 1, '10': 2, '11': 3}
    
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
        elif resultado > 0 and resultado <= 512:
            # poner en true el P
            self.table_alu[1][0] = '01'
            self.table_alu[1][1] = '1'
        elif resultado < 0:
            # poner en true el N
            self.table_alu[2][0] = '01'
            self.table_alu[2][1] = '1'
        elif resultado > 512:
            # poner true el D overflow
            self.table_alu[3][0] = '01'
            self.table_alu[3][1] = '1'
            print('ERROR: LA MAQUINA SE HA DESBORDADO, las instrucciones seguirán su orden pero el resultado puede ser erroneo')

    def siguiente_instruccion(self): 

        self.instruccion_actual = self.instruccion_siguiente
        self.instruccion_siguiente = self.instruccion_siguiente + 1
        instruccion_actual_completa = self.table_ram[self.instruccion_actual]
        
        for instruction in self.opcodes.items():
            if re.search(f"^{instruction[1]}", instruccion_actual_completa):
                self.instruccion_actual_type = instruction[0]
                instruccion_actual_completa = re.sub(f"^{instruction[1]}", "", instruccion_actual_completa)
                break

        # print('Instrucción actual: ', self.instruccion_actual_type, 'linea: ',self.instruccion_actual, 'Instruccion completa: ', instruccion_actual_completa)
        # Como tengo guardadas las cosas en ram, es mas facil operarlas

        #Obtengo el registro en caso de que las operaciones involucren un registro en el primer argumento
        if instruccion_actual_completa[:2]:
            registro = instruccion_actual_completa[:2]
            indexRegistro = self.registros[registro]

        if len(instruccion_actual_completa[:2]) == 2 and len(instruccion_actual_completa[2:4]) == 2:
            registro_1 = self.registros[instruccion_actual_completa[:2]]
            registro_2 = self.registros[instruccion_actual_completa[2:4]]
            contenido_registro_1 = self.table_registros[registro_1][1]
            contenido_registro_2 = self.table_registros[registro_2][1]

        match self.instruccion_actual_type:
            case 'Cargar':
                contenido_celda_m = self.table_ram[binaryToDec(instruccion_actual_completa[2:])]  # me devuelve el contenido de la celda en binario
                self.table_registros[indexRegistro][0] = contenido_celda_m
                self.table_registros[indexRegistro][1] = binaryToDec(contenido_celda_m)

            case 'CargarValor':
                valor = instruccion_actual_completa[2:]
                self.table_registros[indexRegistro][0] = valor
                self.table_registros[indexRegistro][1] = binaryToDec(valor)

            case 'Almacenar': 
                celda_ram_index = binaryToDec(instruccion_actual_completa[2:])
                contenido_en_registro = self.table_registros[indexRegistro][0]  # me devuelve el contenido del registro en binario
                self.table_ram[celda_ram_index] = contenido_en_registro  #guardo eso en la ram

            case 'SaltarSiCero':
                if int(self.table_alu[0][1]) == 1:
                    self.instruccion_siguiente = binaryToDec(instruccion_actual_completa)

            case 'SaltarSiNeg':
                if int(self.table_alu[2][1]) == 1:
                    self.instruccion_siguiente = binaryToDec(instruccion_actual_completa)

            case 'SaltarSiPos':
                if int(self.table_alu[1][1]) == 1:
                    self.instruccion_siguiente = binaryToDec(instruccion_actual_completa)

            case 'SaltarSiDes':
                if int(self.table_alu[3][1]) == 1:
                    self.instruccion_siguiente = binaryToDec(instruccion_actual_completa)

            case 'Saltar':
                self.instruccion_siguiente = binaryToDec(instruccion_actual_completa)

            case 'Copiar':
                registro_1 = self.registros[instruccion_actual_completa[:2]]
                registro_2 = self.registros[instruccion_actual_completa[2:]]
                self.table_registros[registro_2][1] = self.table_registros[registro_1][1]
                self.table_registros[registro_2][0] = self.table_registros[registro_1][0]

            case 'Sumar':  # suma ambos pero guarda en el primero
                resultado = int(contenido_registro_1) + int(contenido_registro_2)
                self.table_registros[registro_1][1] = str(resultado)
                self.table_registros[registro_1][0] = decimalToBinary(int(resultado))
                self.actualizar_alu(resultado)

            case 'Restar':  # resta ambos pero guarda en el primero
                resultado = int(contenido_registro_1) - int(contenido_registro_2)
                self.table_registros[registro_1][1] = str(resultado)
                self.table_registros[registro_1][0] = decimalToBinary(int(resultado))
                self.actualizar_alu(resultado)

            case 'Mult':  # multiplica ambos pero guarda en el primero
                resultado = int(contenido_registro_1) * int(contenido_registro_2)
                self.table_registros[registro_1][1] = str(resultado)
                self.table_registros[registro_1][0] = decimalToBinary(int(resultado))
                self.actualizar_alu(resultado)

            case 'Div':  # divide ambos pero guarda en el primero, es division entera
                resultado = int(contenido_registro_1) // int(contenido_registro_2)
                self.table_registros[registro_1][1] = str(resultado)
                self.table_registros[registro_1][0] = decimalToBinary(int(resultado))
                self.actualizar_alu(resultado)

            case 'Parar':  # Termina el programa marcandolo como finalizado en la unidad de control
                self.table_unidad_control[0] = '1111111111111111'
                self.table_unidad_control[1] = '1111111111111111'
                return

            case 'Escribir':  # printea el registro A en decimal supongo
                print('Salida: ', self.table_registros[0][1])
            
            case 'LeerIO':  # lee el input y lo guarda en el registro A
                # Verifica si el valor en el input es un número
                if not isNum(self.input.get_input()):
                    print('ERROR: EL INPUT NO ES UN NUMERO, SE HA PUESTO UN 0')
                    self.table_registros[0][1] = '0'
                    self.table_registros[0][0] = '0000000000000000'
                else:
                    self.table_registros[0][1] = self.input.get_input()
                    self.table_registros[0][0] = decimalToBinary(int(self.table_registros[0][1]))


        # actualiza la instruccion actual
        self.instruccion_actual_ram = self.table_ram[self.instruccion_actual]
        self.table_unidad_control[0] = self.instruccion_actual_ram

        # actualiza la siguiente instruccion a correr
        self.table_unidad_control[1] = str(self.instruccion_siguiente)

    def ultima_instruccion(self):
        while (not (self.table_unidad_control[0] == '1111111111111111' and self.table_unidad_control[1] == '1111111111111111')):
            self.siguiente_instruccion()

    def reiniciar(self):
        self.initializeAllInCeros()
        self.instruccion_actual = 0
        self.instruccion_siguiente = 0


    def ensamblar(self, textEditCodigoASM):
        self.code = textEditCodigoASM
        self.assembler.compile(self)

    def enlazar_cargar(self, startPoint):
        self.likerLoader.linkLoad(self, startPoint)
        
    def compile(self, hight_level_code):
        self.hight_level_code = hight_level_code
        self.code = self.compiler.compile(hight_level_code)

    def leer_input(self, input_leido):
        self.input.set_input(input_leido)
        return self.input.get_input()