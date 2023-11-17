import re
from src.utils.convertions import decimalToBinary

class Assembler:
    """Assembler for custom assembly code
    """

    def __init__(self):
        self.basic_regular_expresion = {
            'variable': '\w+',
            'label': '\w+:',
            'valor': '-?\d+',
            'registro': '(A|B|C|D)'
        }
        self.opcode_regular_expresion = re.compile(
            r'(?P<Parar>Parar)|(?P<Cargar>Cargar%s,%s)|(?P<CargarValor>CargarValor%s,%s)|(?P<Almacenar>Almacenar%s,%s)|'
            r'(?P<SaltarSiCero>SaltarSiCero%s)|(?P<SaltarSiNeg>SaltarSiNeg%s)|(?P<SaltarSiPos>SaltarSiPos%s)|'
            r'(?P<SaltarSiDes>SaltarSiDes%s)|(?P<Saltar>Saltar%s)|(?P<Copiar>Copiar%s,%s)|(?P<Sumar>Sumar%s,%s)|'
            r'(?P<Restar>Restar%s,%s)|(?P<Mult>Mult%s,%s)|(?P<Div>Div%s,%s)|(?P<Label>%s)|(?P<Escribir>Escribir)' %
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

    def compile(self, virtualMachine):
        #code withouth spaces and divided by line
        refinedCode = virtualMachine.code.replace(' ','')


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
                    print('ERROR: El assembler encontró un error en la linea: ', linea)

        # acá es donde se rellena utilizando los datos anteriores.
        # conociendo el numero de instrucciones podemos estar seguros de darle a la variables espacio en ram desde núm de instrucciones + 1

        for variable in relocVariables:
            linea += 1
            (relocVariables[variable]) = linea # les digo en que posicion de la ram pueden quedar las variables todo convertir a binario

        linea = 0

        # Luego mapea cada linea ya con los diccionarios resueltos y coloca ese resultado en la memoria ram.
        # todo Tambien se guardan las instrucciones en texto para la simulacion de manera: {linea de instrucción: [tipo de instruccion, registro, memoria]}
        for statement in self.opcode_regular_expresion.finditer(refinedCode):
            #print(statement)
            opname = statement.lastgroup
            match opname:
                case 'Label':#si es un label, ya sabemos que se ignora
                    linea -= 1
                case 'Cargar':
                    values = statement.group().replace('Cargar','').split(',')
                    registro = values[0]
                    variable = values[1]
                    virtualMachine.object_code[linea] = virtualMachine.opcodes['Cargar'] + virtualMachine.registers[registro] + decimalToBinary(int(variable))

                case 'CargarValor':
                    values = statement.group().replace('CargarValor', '').split(',')
                    registro = values[0]
                    valor = values[1]
                    virtualMachine.object_code[linea] = virtualMachine.opcodes['CargarValor'] + virtualMachine.registers[registro] + decimalToBinary(int(valor))
                    
                case 'Almacenar':
                    values = statement.group().replace('Almacenar', '').split(',')
                    registro = values[0]
                    variable = values[1]
                    #print(values)
                    virtualMachine.object_code[linea] = virtualMachine.opcodes['Almacenar'] + virtualMachine.registers[registro] + decimalToBinary(int(variable))

                case 'SaltarSiCero':
                    value = statement.group().replace('SaltarSiCero', '')
                    virtualMachine.object_code[linea] = virtualMachine.opcodes['SaltarSiCero'] + "{" +str(labels[value]) + "}"
                    
                case 'SaltarSiNeg':
                    value = statement.group().replace('SaltarSiNeg', '')
                    virtualMachine.object_code[linea] = virtualMachine.opcodes['SaltarSiNeg'] + "{" +str(labels[value]) + "}"
                    
                case 'SaltarSiPos':
                    value = statement.group().replace('SaltarSiPos', '')
                    virtualMachine.object_code[linea] = virtualMachine.opcodes['SaltarSiPos'] + "{" +str(labels[value]) + "}"
                    
                case 'SaltarSiDes':
                    value = statement.group().replace('SaltarSiDes', '')
                    virtualMachine.object_code[linea] = virtualMachine.opcodes['SaltarSiDes'] + "{" +str(labels[value]) + "}"
                    
                case 'Saltar':
                    value = statement.group().replace('Saltar', '')
                    virtualMachine.object_code[linea] = virtualMachine.opcodes['Saltar'] + "{" +str(labels[value]) + "}"
                    
                case 'Copiar':
                    values = statement.group().replace('Copiar', '').split(',')
                    registro1 = values[0]
                    registro2 = values[1]
                    virtualMachine.object_code[linea] = virtualMachine.opcodes['Copiar'] + virtualMachine.registers[registro1] + virtualMachine.registers[registro2]
                    

                case 'Sumar':
                    values = statement.group().replace('Sumar', '').split(',')
                    registro1 = values[0]
                    registro2 = values[1]
                    virtualMachine.object_code[linea] = virtualMachine.opcodes['Sumar'] + virtualMachine.registers[registro1] + virtualMachine.registers[registro2]
                    

                case 'Restar':
                    values = statement.group().replace('Restar', '').split(',')
                    registro1 = values[0]
                    registro2 = values[1]
                    virtualMachine.object_code[linea] = virtualMachine.opcodes['Restar'] + virtualMachine.registers[registro1] + virtualMachine.registers[registro2]
                    

                case 'Mult':
                    values = statement.group().replace('Mult', '').split(',')
                    registro1 = values[0]
                    registro2 = values[1]
                    virtualMachine.object_code[linea] = virtualMachine.opcodes['Mult'] + virtualMachine.registers[registro1] + virtualMachine.registers[registro2]
                    

                case 'Div':
                    values = statement.group().replace('Div', '').split(',')
                    registro1 = values[0]
                    registro2 = values[1]
                    virtualMachine.object_code[linea] = virtualMachine.opcodes['Div'] + virtualMachine.registers[registro1] + virtualMachine.registers[registro2]
                    
                case 'Escribir':
                    virtualMachine.object_code[linea] = virtualMachine.opcodes['Escribir'] + '00'

                case 'Parar':
                    virtualMachine.object_code[linea] = virtualMachine.opcodes['Parar']
                    
            linea += 1

    def handle_int(self, integer):
        """Convert hexidecimal and binary numbers in strings to integers, if needed
        """
        if isinstance(integer, int):
            val = integer
        else:
            val = int(integer, 0)
        return val

